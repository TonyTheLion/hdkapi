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

# Sort by author
def sort_per_author(data):
    ret = dict()
    # List of authors only
    authors = [ x["author"] for x in data["books"]] 
    for b in data["books"]:
        # Look in the 'authors' list, using 'set' such that all items are unique
        for z in list(set(authors)):
            if b["author"] == z:
                if not z in ret:
                    ret[z] = [b]
                else:
                    ret[z].append(b)

    return ret

# Index page, show data directly as downloaded ('/authors')
def index(request):
    data = download(url)
    auths = sort_per_author(data)
    return HttpResponse(json.dumps(auths), content_type="application/json")
