from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        hostname = socket.gethostname()
        self.wfile.write(f"Served by backend: {hostname}".encode())

if __name__ == "__main__":
    server = HTTPServer(("", 8080), Handler)
    server.serve_forever()