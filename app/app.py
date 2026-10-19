"""DevOps student application: prints student info and serves it over HTTP."""
import http.server
import os
import signal
import sys

DEFAULTS = {
    "STUDENT_NAME": "Batyr",
    "STUDENT_SURNAME": "Gazizbek",
    "STUDENT_GROUP": "IT2-2301",
    "STUDENT_ID": "38091",
}


def get(key):
    """Environment variable wins over the default value."""
    return os.environ.get(key, DEFAULTS[key])


def render():
    line = "=" * 32
    return "\n".join([
        line,
        "DevOps Student Application",
        line,
        "",
        f"Name: {get('STUDENT_NAME')}",
        f"Surname: {get('STUDENT_SURNAME')}",
        f"Group: {get('STUDENT_GROUP')}",
        f"Student ID: {get('STUDENT_ID')}",
        "",
        "Application is running successfully!",
    ])


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        body = render().encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)


def main():
    signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))  # graceful docker stop
    print(render(), flush=True)
    port = int(os.environ.get("PORT", "5000"))
    print(f"\nListening on port {port} (Ctrl+C to stop)", flush=True)
    try:
        http.server.HTTPServer(("0.0.0.0", port), Handler).serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
