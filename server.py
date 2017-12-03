#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import original_api
import datetime
import socket

PORT = 9000

class JSONRequestHandler (BaseHTTPRequestHandler):

    def do_GET(self):

        #send response code:
        self.send_response(200)
        #send headers:
        self.send_header("Content-type", "application/json")
        # send a blank line to end headers:
        self.wfile.write("\r\n".encode())
        path = queries = ''

        if self.path.startswith('/balance'):
            path = '/balance'
        if self.path.startswith('/balance-history'):
            path = '/balance-history'
            date_before = (datetime.datetime.now().date() - datetime.timedelta(days = 30)).strftime('%Y%m%d')
            queries = '?date_from=' + date_before
        if self.path.startswith('/transaction-history'):
            path = '/transaction-history'
            curr_date = datetime.datetime.now().date().strftime('%Y%m%d')
            date_before = (datetime.datetime.now().date() - datetime.timedelta(days = 30)).strftime('%Y%m%d')
            queries = '?date_from=' + date_before + '&date_to=' + curr_date

        data = original_api.make_get_request(path, queries)
        self.wfile.write(data.encode())

if __name__ == '__main__':
    HOST_NAME = socket.gethostbyname('hackatonoriginalback.herokuapp.com')
    print(HOST_NAME)
    server = HTTPServer((HOST_NAME, PORT), JSONRequestHandler)
    print(datetime.datetime.now(), 'Server Starts - %s:%s' % (HOST_NAME, PORT))
    server.serve_forever()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    print(datetime.datetime.now(), 'Server Stops - %s:%s' % (HOST_NAME, PORT))

