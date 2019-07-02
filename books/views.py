from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

url = 'https://hokodo-frontend-interview.netlify.com/data.json' 
# download given 'url' and
# return JSON data
def download(url):
    r = requests.get(url)
    return json.loads(r.content.decode())

# Index page, show data directly as downloaded ('/books')
def index(request):
    data = download(url)
    return HttpResponse(json.dumps(data), content_type="application/json")

# Authors collection
def author(request):
    data = download(url)
    return HttpResponse(json.dumps(data), content_type="application/json")

# Sort 'published' in asc or desc order
def published_date(request, order):
    # reverse = desc; (1 = desc, 0 = asc)
    return HttpResponse(json.dumps(sort_data("published", order)), content_type="application/json")

# Sort 'title' in asc or desc order
def title(request, order):
    return HttpResponse(json.dumps(sort_data("title", order)), content_type="application/json")

# take a dictionary key and an order boolean (int 0,1) 
# and sort data of 'dict_key' in 'order'
def sort_data(dict_key, order):
    data = download(url)
    return sorted(data["books"], key=lambda item: item[dict_key], reverse=order)
