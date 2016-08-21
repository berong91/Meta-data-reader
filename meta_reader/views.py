import os.path
from os import listdir
from os.path import isfile, join

import pytz
import simplejson
from django.http import HttpResponse
from django.utils import timezone
from django.utils.datetime_safe import datetime

from meta_reader.models import Source, Record


def index(request):
    message = reload_sources()
    
    # Print records list
    for obj in Record.objects.all():
        message += r"{0}__{1}__{2}__{3}__{4}__{5}__{6})__{7}<br/>".format(
            obj.id,
            obj.source_id,
            obj.date.strftime('%b %d, %Y %H:%M:%S'),
            obj.action,
            obj.rating,
            obj.submit_type,
            obj.filename,
            obj.colour
        )
    
    return HttpResponse(message)


def reload_sources():
    """
    Return the records table
    :HttpResponse: Http Response message
    """
    data_path = os.path.abspath("data/")
    utc = pytz.UTC
    message = ""
    # Generate 2D array with first column is source name, 2nd column is source absolute path
    list_detected_sources = []
    for f in listdir(data_path):
        p = join(data_path, f);
        if isfile(p):
            list_detected_sources.append([f, p])
    
    # Delete non exist source
    Source.objects.exclude(source_name__in=[x[0] for x in list_detected_sources]).delete()
    
    for iteration in list_detected_sources:
        update_flag = False;
        file_name = iteration[0]
        file_path = iteration[1]
        
        current_date_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).replace(tzinfo=utc)
        
        source, created = Source.objects.get_or_create(
            source_name=file_name,
            defaults=dict(source_name=file_name, date_added=datetime.now(timezone.utc),
                          date_modified=current_date_modified),
        )
        
        source_date_modified = source.date_modified
        if created or source_date_modified != current_date_modified:
            update_flag = True  # trigger update if create new source or date modified is changed
        
        # Import data
        if update_flag:
            try:
                with open(file_path, 'r') as data_file:
                    data = simplejson.load(data_file)
                for o in data:
                    tmp_date = datetime.strptime(o['date'], '%b %d, %Y %H:%M:%S').replace(tzinfo=utc)
                    record = Record(
                        source_id=file_path,
                        date=tmp_date,
                        filename=o["filename"],
                        action=o["action"],
                        rating=o["rating"],
                        submit_type=o["submit-type"],
                    )
                    record.save()
                
                message += r"Add {0} to Source list success<br/>".format(file_name)
            
            except Exception as e:
                message += r"Error when adding {0} to Source list<br/>{1}<br/>".format(file_name, e.message)
        
        # Testing script to check Source insert success
        tmp_src = Source.objects.get(source_name=file_name)
        message += r"{0}<br/>{1}<br/>{2}<br/><br/>".format(
            tmp_src.source_name,
            tmp_src.date_added.strftime('%b %d, %Y %H:%M:%S'),
            tmp_src.date_modified.strftime(
                '%b %d, %Y %H:%M:%S')
        )
    return message
