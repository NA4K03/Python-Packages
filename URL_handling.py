import urllib
from urllib.request import urlopen
import urllib.error
import urllib.parse


class WebsiteUrl:

    # urllib.request is a Python module for fetching URLs
    # It is capable of fetching URLs using a variety of different protocols

    def init(self, link):
        self.link = link


    # bits is used to read the bytes from the link


    def open_link(self, bits):
        with urlopen(self.link) as f:
            print(f.read(bits).decode('utf-8'))


    # For sending data to URL we use POST request.

    def post_link(self, values):
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')
        req_1 = urllib.request.Request(self.link, data)
        with urlopen(req_1) as g:
            print(g.read().decode('utf-8'))


    # If we do not pass the data urllib uses GET request

    def get_link(self, params):
        data = urllib.parse.urlencode(params)
        url = f"{self.link} {data}"
        with urllib.request.urlopen(url) as f:
            print(f.read().decode('utf-8'))
    """
    When an error is raised the server responds by returning an 
    HTTP error code and an error page. You can use the HTTPError 
    instance as a response on the page returned
    """

    def error_link(self, req):
        try:
            urllib.request.urlopen(req)
        except HTTPError as e:
            print(e.code)