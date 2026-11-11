// Key Box: a one time private form on YOUR computer. The key goes from the form into ~/.builder-secrets/<name>.env and nowhere else.
// Usage: node keybox.js VARIABLE_NAME "Plain label"
const http = require("http"), fs = require("fs"), os = require("os"), path = require("path"), crypto = require("crypto"), { exec } = require("child_process");
const NAME = (process.argv[2] || "").toUpperCase().replace(/[^A-Z0-9_]/g, ""), LABEL = (process.argv[3] || NAME).slice(0, 80);
if (!NAME) { console.error('Say which key: node keybox.js VARIABLE_NAME "Plain label"'); process.exit(1); }
const DIR = path.join(os.homedir(), ".builder-secrets"), TOKEN = crypto.randomBytes(18).toString("base64url");
const esc = (s) => s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const page = (extra = "") => `<!doctype html><meta name=viewport content="width=device-width,initial-scale=1"><title>Key Box</title><body style="font:18px/1.5 system-ui;max-width:520px;margin:40px auto;padding:0 18px"><h1 style="font-size:26px">Key Box</h1><p>Paste your <b>${esc(LABEL)}</b> here and tap Save. It goes into a private file on this computer and nowhere else.</p><form method=post><input type=password name=v autofocus autocomplete=off style="width:100%;font-size:18px;padding:12px;box-sizing:border-box"><p><button style="font-size:18px;padding:12px 26px">Save</button></p></form>${extra}</body>`;
const send = (res, code, body) => { res.writeHead(code, { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store" }); res.end(body); };
const srv = http.createServer((req, res) => {
  const mine = req.url === "/k/" + TOKEN && /^(127\.0\.0\.1|localhost)(:\d+)?$/.test(req.headers.host || "");
  if (!mine) return send(res, 404, "Not found");
  if (req.method === "GET") return send(res, 200, page());
  let b = ""; req.on("data", (c) => { if (b.length < 20000) b += c; });
  req.on("end", () => {
    const v = decodeURIComponent((b.replace(/^v=/, "")).replace(/\+/g, " ")).trim();
    if (v.length < 8 || v.length > 4000 || /[\r\n]/.test(v)) return send(res, 200, page("<p style='color:#b00'>That doesn't look like a key. Paste it again.</p>"));
    fs.mkdirSync(DIR, { recursive: true, mode: 0o700 }); fs.writeFileSync(path.join(DIR, NAME.toLowerCase() + ".env"), NAME + "=" + v + "\n", { mode: 0o600 });
    send(res, 200, "<!doctype html><meta name=viewport content='width=device-width,initial-scale=1'><body style='font:18px/1.5 system-ui;max-width:520px;margin:40px auto;padding:0 18px'><h1>Saved.</h1><p>You can close this tab.</p>");
    console.log(`Saved ${NAME} (${v.length} characters)`); srv.close(); process.exit(0);
  });
});
srv.listen(0, "127.0.0.1", () => {
  const url = `http://127.0.0.1:${srv.address().port}/k/${TOKEN}`; console.log("Key Box is open: " + url);
  exec((process.platform === "darwin" ? "open " : process.platform === "win32" ? "start \"\" " : "xdg-open ") + url, () => {});
  setTimeout(() => { console.log("Key Box closed. Nothing was saved."); process.exit(0); }, 600000);
});
