import http.server
import socketserver
import os

PORT = 9100
os.chdir(os.path.dirname(os.path.abspath(__file__)))
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
