import os.path
from os import listdir
from os.path import isfile, join

import pytz
import simplejson
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.utils.datetime_safe import datetime

from meta_reader.models import Source, Record


def index(request):
    """
    Return the index page
    :param request: HTTPRequest
    :return: index page
    """
    message = reload_sources()
    index_context = {
        'status': message,
        'records': Record.objects.all(),
    }
    return render(request, 'meta_reader/index.html', index_context)


def update(request):
    """
    Get an updated list of records
    :param request: HttpRequest
    :return: List records in JSON
    """
    message = reload_sources()
    
    records = Record.objects.all()
    
    data = serializers.serialize('json', records)
    
    index_context = {
        'status': message,
        'records': data,
    }
    
    return JsonResponse(index_context, safe=False)


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
    tmp_lst = [x[0] for x in list_detected_sources]
    lst_all = Source.objects.all()
    
    list_source_not_found = lst_all.exclude(source_name__in=list(tmp_lst))
    list_source_not_found.delete()
    
    # Start to process each files in the data folder
    for iterator in list_detected_sources:
        update_flag = False;
        file_name = iterator[0]
        file_path = iterator[1]
        
        # Open file and process if file is correct
        with open(file_path, 'r') as data_file:
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
                    data = simplejson.load(data_file)
                    for o in data:
                        tmp_date = datetime.strptime(o['date'], '%b %d, %Y %H:%M:%S').replace(tzinfo=utc)
                        record = Record(
                            source_id=file_name,
                            date=tmp_date,
                            filename=o["filename"],
                            action=o["action"],
                            rating=o["rating"],
                            submit_type=o["submit-type"],
                        )
                        record.save()
                    message += r"Update source {0} to database successfully<br/>".format(file_name)
                
                except Exception as e:
                    message += r"Error when updating source {0} to database: {1}<br/><br/>".format(
                        file_name,
                        e.message
                    )
        
        # Testing script to check Source insert success
        tmp_src = Source.objects.get(source_name=file_name)
        message += r"Source: {0}<ul><li>Date added: {1}</li><li>Last modified: {2}</li></ul>".format(
            tmp_src.source_name,
            tmp_src.date_added.strftime('%b %d, %Y %H:%M:%S'),
            tmp_src.date_modified.strftime('%b %d, %Y %H:%M:%S'),
        )
    
    return message
