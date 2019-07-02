## Hodoko test excercise JSON endpoint

You must have django installed in order to run this application.

# Installation

This software was built on a Ubuntu Linux 18.04 LTS machine

Installation can be done as follows:

`sudo -H pip3 install Django==2.2.2`

Once that is installed, you can run this application as follows

`python3 manage.py runserver 0.0.0.0:8000` 

This will allow you to query the API at the IP of the machine
it is being run on at the given port, in this case 8000.

# Code

This website has two apps, one is 'books' the other is 'authors'

Each of these has a 'views.py' that contains the code which 
handles the requests.

Upon request it simply goes and downloads the source JSON from a hardcoded
URL (which in a real scenario would be made configurable) sorts the data
according to user request and then returns it.

# Tests

It can be queried in any browser or via a script.  If you had a python
script you may want to query it as follows:

```python
#!/usr/bin/env python3

import requests
import json
import sys
from collections import OrderedDict

# download given 'url' and
# return JSON data
def download(url):
    r = requests.get(url)
    return json.loads(r.content.decode())
   
def test_download_books(url):
    api_books = '/books'
    data = download(url + api_books)
    if len(data) == 0:
        print("No '/books' were returned")
    else:
        print("'/books' was succesfully returned")

def main():
    url = sys.argv[1]
    print(url)
    if len(url) == 0:
        print('Please provide a base url to test')
        sys.exit()
    test_download_books(url)

if __name__ == "__main__":
    main()

```

This sample actually can serve as a test, but it also shows
how you would query this API using python.

This sample test script could be run as follows
`./test.py "192.168.0.5:8000"`

It would simply test if '/books' was available.
For each enpoint you could add a test as such.

More extensive tests could be written that checked the schema of the return JSON
and whether the JSON returned is what is expected for each case. 

I am aware that Django also has testing facilities and unit testing,
however I do not see how for this simple JSON endpoints this would be useful.

# Apps

There are two apps that are part of this site.

- books
- authors

The books app provides a JSON api for books data
The data can be queried by title and by published date

The authors app provides JSON api for books ordered by author

# Endpoints

The following endpoints are available for use:

`/books`
`/books/title/0`
`/books/title/1`
`/books/published/0`
`/books/published/1`
`/authors`

For 'title' and 'published' the 0 means in 'ascending' order and the 1 means in 'descending' order.
