# coding: utf-8

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

class class1(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("User-Agent","test1")
        self.end_headers()
        html = "<h1>テスト</h1>"
        self.wfile.write(html.encode())

ip = '127.0.0.1'
port = 80

server = HTTPServer((ip, port), class1)

server.serve_forever()
