import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))
MP3_DIR = os.path.join(ROOT, "mp3")

class MP3Server(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/list":
            data = self.list_mp3s()
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))
        else:
            super().do_GET()

    def list_mp3s(self):
        structure = {}
        for root, _, files in os.walk(MP3_DIR):
            rel = os.path.relpath(root, MP3_DIR)
            mp3s = [f for f in files if f.lower().endswith(".mp3")]
            if mp3s:
                structure[rel if rel != "." else ""] = mp3s
        return structure


if __name__ == "__main__":
    print(f"🌐 Szerver fut: http://localhost:{PORT}")
    print(f"🎵 MP3 mappa: {MP3_DIR}")
    HTTPServer(("0.0.0.0", PORT), MP3Server).serve_forever()
