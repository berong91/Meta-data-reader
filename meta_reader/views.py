from django.core.serializers import json
from django.http import HttpResponse
from meta_reader.models import Source, Record

import simplejson, time, os.path
from os import listdir
from os.path import isfile, join

def index(request):
    data_path = os.path.abspath("data/")
    # file_list = [f for f in listdir(data_path)  if isfile(path)]
    
    file_list = []
    for f in listdir(data_path):
        p = join(data_path, f);
        if isfile(p):
            tmp_lst = [f, p]
            file_list.append( tmp_lst )
    
    
    for iteration in file_list:
        file_name = iteration[0]
        file_path = iteration[1]
        time_modified = time.ctime(os.path.getmtime( file_path ))
        
        source, created = Source.objects.get_or_create(
        )
        
        with open(file_path, 'r') as data_file:
            data = simplejson.load(data_file);
            
            for o in data:
                record = o;
    
    return HttpResponse("Hello, world. You're at the index.")

