from django.shortcuts import render,redirect
import requests
from django.http import JsonResponse
from django.urls import reverse
from flask import jsonify
import pandas as pd
import requests_cache
import requests
import json
requests_cache.install_cache('swapi_cache', backend='sqlite', expire_after=180)
# Create your views here.


api_base_url = 'https://swapi.dev/api'
head_request = requests.head(api_base_url)
get_request = requests.get(api_base_url)

#http status code checking function to confirm successfull communication with web api / web server
def check_status(r):
    if r.status_code == 200:
        print("URL: ",r.url)
        print('STATUS_CODE: ',r.status_code)
        print('Content-type: ',r.headers['content-type'])
        return r.text

    else:
        print('[!] HTTP {0} calling ({1})'.format(r.status_code,api_base_url))
        return None

#JSON object notation conversion and formatting function to make json proccessible and much more readable
def json_print(payload):
    a = json.dumps(payload,indent=4,sort_keys=True)
    return a

#Converting JSON to Dictionaries
search_dict = json.loads(check_status(get_request))
title = list(search_dict.keys())



def home(request):
    return render(request,'index.html',{'title':title})

def search(request,slug):
    url = "https://swapi.dev/api/{}/".format(slug)
    json1='Empty'
    index=[]
    values=[]
    html='Empty'
    search_dict={'results':None}
    if request.method=='POST':
        try:
            name = request.POST.get('name')
            if name == 'all':
                search_request = requests.get(url)
                search_dict = json.loads(check_status(search_request))
                values = search_dict['results']
                #print(values)
                df = pd.DataFrame(data=search_dict['results'])
                df = df.fillna(' ')
                html = df.to_html(border=5,index=False,col_space=100,justify='left',classes='mt-4')
            else:
                url = url + '?search=' + name
                search_request = requests.get(url)
                search_dict = json.loads(check_status(search_request))
                values = search_dict['results']
                df = pd.DataFrame(data=search_dict['results'])
                df = df.fillna(' ')
                html = df.to_html(border=5,index=False, col_space=100, justify='left', classes='mt-4',escape='True')
        except:
            name=None
    return render(request,'detail.html',{'title':title,'slug':slug,'html':html})




