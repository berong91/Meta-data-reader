import os.path
from datetime import datetime
from os import listdir
from os.path import isfile, join

import simplejson
from django.http import HttpResponse

from meta_reader.models import Source


def index(request):
    data_path = os.path.abspath("data/")
    # file_list = [f for f in listdir(data_path)  if isfile(path)]
    
    file_list = []
    for f in listdir(data_path):
        p = join(data_path, f);
        if isfile(p):
            tmp_lst = [f, p]
            file_list.append(tmp_lst)
    
    for iteration in file_list:
        file_name = iteration[0]
        file_path = iteration[1]
        time_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
        
        source, created = Source.objects.get_or_create(
            source_name=file_name,
            defaults=dict(source_name=file_name, date_added=datetime.now(),
                          date_modified=time_modified),
        )
        
        if created:
            source.save()
        else:
            message = r"%s<br/>%s<br/>%s" % (source.source_name,
                                            source.date_added.strftime('%b %d, %Y %H:%M:%S'),
                                            source.date_modified.strftime('%b %d, %Y %H:%M:%S'))
            return HttpResponse(message)
        
        with open(file_path, 'r') as data_file:
            data = simplejson.load(data_file);
            
            for o in data:
                record = o;
    
    return HttpResponse("Hello worldddddddddd")
