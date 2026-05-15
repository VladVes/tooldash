from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import mimetypes


CLIENT_DIR = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "client", "dist")
)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        file_path = os.path.normpath(os.path.join(CLIENT_DIR, self.path.lstrip("/")))

        if file_path.startswith(CLIENT_DIR) and os.path.isfile(file_path):
            self.send_response(200)
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type:
                self.send_header("Content-Type", mime_type)
            self.end_headers()
            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
        else:
            index_path = os.path.join(CLIENT_DIR, "index.html")
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open(index_path, "rb") as f:
                self.wfile.write(f.read())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 3000), Handler)
    print("Server running on port 3000")
    server.serve_forever()
