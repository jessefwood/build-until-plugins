#!/usr/bin/env python3
# Key Box: a one time private form on YOUR computer. The key goes from the form into ~/.builder-secrets/<name>.env and nowhere else.
# Usage: python3 keybox.py VARIABLE_NAME "Plain label"
import html, http.server, os, re, secrets, sys, threading, webbrowser
NAME = re.sub(r"[^A-Z0-9_]", "", (sys.argv[1] if len(sys.argv) > 1 else "").upper())
LABEL = (sys.argv[2] if len(sys.argv) > 2 else NAME)[:80]
if not NAME:
    sys.exit("Say which key: python3 keybox.py VARIABLE_NAME \"Plain label\"")
DIR = os.path.join(os.path.expanduser("~"), ".builder-secrets")
TOKEN = secrets.token_urlsafe(18)
PAGE = """<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><title>Key Box</title>
<body style="font:18px/1.5 system-ui;max-width:520px;margin:40px auto;padding:0 18px"><h1 style="font-size:26px">Key Box</h1>
<p>Paste your <b>%s</b> here and tap Save. It goes into a private file on this computer and nowhere else.</p>
<form method=post><input type=password name=v autofocus autocomplete=off style="width:100%%;font-size:18px;padding:12px;box-sizing:border-box"><p><button style="font-size:18px;padding:12px 26px">Save</button></p></form></body>"""
DONE = "<!doctype html><meta name=viewport content='width=device-width,initial-scale=1'><body style='font:18px/1.5 system-ui;max-width:520px;margin:40px auto;padding:0 18px'><h1>Saved.</h1><p>You can close this tab.</p>"
class H(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def ok(self, body, code=200):
        b = body.encode(); self.send_response(code); self.send_header("Content-Type", "text/html; charset=utf-8"); self.send_header("Cache-Control", "no-store"); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def mine(self):
        return self.path == "/k/" + TOKEN and self.headers.get("Host", "").split(":")[0] in ("127.0.0.1", "localhost")
    def do_GET(self):
        self.ok(PAGE % html.escape(LABEL)) if self.mine() else self.ok("Not found", 404)
    def do_POST(self):
        if not self.mine(): return self.ok("Not found", 404)
        n = min(int(self.headers.get("Content-Length") or 0), 20000)
        v = re.sub(r"^v=", "", self.rfile.read(n).decode("utf-8", "ignore"))
        from urllib.parse import unquote_plus
        v = unquote_plus(v).strip()
        if len(v) < 8 or len(v) > 4000 or "\n" in v or "\r" in v:
            return self.ok(PAGE % html.escape(LABEL) + "<p style='color:#b00'>That doesn't look like a key. Paste it again.</p>")
        os.makedirs(DIR, mode=0o700, exist_ok=True)
        fd = os.open(os.path.join(DIR, NAME.lower() + ".env"), os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w") as f: f.write(NAME + "=" + v + "\n")
        self.ok(DONE)
        print("Saved %s (%d characters)" % (NAME, len(v)), flush=True)
        threading.Thread(target=srv.shutdown).start()
srv = http.server.HTTPServer(("127.0.0.1", 0), H)
url = "http://127.0.0.1:%d/k/%s" % (srv.server_port, TOKEN)
print("Key Box is open: " + url, flush=True)
threading.Timer(600, lambda: (print("Key Box closed. Nothing was saved.", flush=True), srv.shutdown())).start()
try: webbrowser.open(url)
except Exception: pass
srv.serve_forever()
os._exit(0)
