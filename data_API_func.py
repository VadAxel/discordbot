import urllib.request
import json

#API tillkallas.
def data_API_func(url):
    url_response = urllib.request.urlopen(url)
    data_response = url_response.read() 
    jsonData_response = json.loads(data_response)
    return jsonData_response
