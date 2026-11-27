
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = b"<h1>Hello from Kubernetes - Version 2!</h1>"
        self.wfile.write(message)

server = HTTPServer(("0.0.0.0", 5000), MyHandler)

print("Python application running on port 5000")

server.serve_forever()
