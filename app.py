from http.server import BaseHTTPRequestHandler, HTTPServer
import os
 
MESSAGE = os.environ.get("APP_MESSAGE", "Hello from DevOps!")
 
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/health"):
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(("OK" if self.path == "/health" else MESSAGE).encode())
        else:
            self.send_error(404)
 
if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
