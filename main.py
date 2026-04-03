"""Proxy server that serves DEGEN.md from GitHub."""

import urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler

RAW_URL = "https://raw.githubusercontent.com/maxyz-xyz/DEGEN.md/main/DEGEN.md"
PORT = 8080

# Cache
_cache = {"body": None, "etag": None}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            req = urllib.request.Request(RAW_URL)
            if _cache["etag"]:
                req.add_header("If-None-Match", _cache["etag"])
            resp = urllib.request.urlopen(req, timeout=10)
            _cache["body"] = resp.read().decode()
            _cache["etag"] = resp.headers.get("ETag")
        except urllib.error.HTTPError as e:
            if e.code == 304 and _cache["body"]:
                pass  # use cache
            else:
                self.send_response(502)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Failed to fetch DEGEN.md")
                return
        except Exception:
            if not _cache["body"]:
                self.send_response(502)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Failed to fetch DEGEN.md")
                return

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Cache-Control", "public, max-age=300")
        self.end_headers()
        self.wfile.write(_cache["body"].encode())

    def log_message(self, format, *args):
        pass  # silence logs


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
