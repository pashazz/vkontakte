#coding: utf-8

from contextlib import closing
import http.client

# urllib2 doesn't support timeouts for python 2.5 so
# custom function is used for making http requests

def post(url, data, headers, timeout, secure=False):
    host_port = url.split('/')[2]
    timeout_set = False
    connection = http.client.HTTPSConnection if secure else http.client.HTTPConnection
    try:
        connection = connection(host_port, timeout = timeout)
        timeout_set = True
    except TypeError:
        connection = connection(host_port)

    with closing(connection):
        if not timeout_set:
            connection.connect()
            connection.sock.settimeout(timeout)
            timeout_set = True

        connection.request("POST", url, data, headers)
        response = connection.getresponse()
        return (response.status, response.read())
