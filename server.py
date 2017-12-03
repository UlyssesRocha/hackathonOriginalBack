#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import original_api
import datetime
import socket
import os
import gen
import retrieve
import json

PORT = int(os.environ.get("PORT", 5000))


class JSONRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        #send response code:
        self.send_response(200, message="HTTP/1.1 200 OK")
        #send headers:
        self.send_header("Content-type", "application/json")
        # send a blank line to end headers:
        self.end_headers()
        path = queries = ''

        if self.path.startswith('/balance'):
            path = '/balance'
        if self.path.startswith('/balance-history'):
            path = '/balance-history'
            date_before = (datetime.datetime.now().date() -
                           datetime.timedelta(days=30)).strftime('%Y%m%d')
            queries = '?date_from=' + date_before
        if self.path.startswith('/transaction-history'):
            path = '/transaction-history'
            curr_date = datetime.datetime.now().date().strftime('%Y%m%d')
            date_before = (datetime.datetime.now().date() -
                           datetime.timedelta(days=30)).strftime('%Y%m%d')
            queries = '?date_from=' + date_before + '&date_to=' + curr_date
        if self.path.startswith('/savings'):
            path = '/savings'
            data = json.dumps({'savings': 42})
        elif self.path.startswith('/predict-credit-score'):
            path = '/predict-credit-score'
            # mock with random data
            new_data = gen.random_client_data()
            credit_score = retrieve.get_credit_prection(new_data)
            data = json.dumps({'score': credit_score})
        else:
            data = original_api.make_get_request(path, queries)

        self.wfile.write(data.encode())


if __name__ == '__main__':
    HOST_NAME = '0.0.0.0'
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
