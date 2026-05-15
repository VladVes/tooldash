from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"tools dashboard")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 3000), Handler)
    print("Server running on port 3000")
    server.serve_forever()