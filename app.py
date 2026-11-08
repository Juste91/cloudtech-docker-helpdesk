import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class HelpDeskHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            response = {"status": "healthy"}
            status = 200
        elif self.path == "/":
            response = {
                "project": "CloudTech Docker Help Desk",
                "answer": "Welcome to CloudTech! Your container is running."
            }
            status = 200
        else:
            response = {"error": "Not found"}
            status = 404

        body = json.dumps(response).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), HelpDeskHandler).serve_forever()
