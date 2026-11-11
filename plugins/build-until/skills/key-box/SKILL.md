---
name: key-box
description: Saves a key, token or secret for the student without it ever touching the chat. Use whenever any step needs an API key, access token, webhook secret or any other secret from the student, and when the student says "set up my Key Box", "I have a key", or starts to paste one. Opens a private one-time form in their own browser on their own computer and saves the value to ~/.builder-secrets. Never ask for a key in the chat.
---

# The Key Box

A key never goes in the chat. When you need one, you open the student's Key Box: a small private form that runs on THEIR computer and opens in THEIR browser. They paste the key in the box and tap Save. It goes straight into `~/.builder-secrets/<name>.env` (readable only by them). You never see it. You only learn it's there.

## One time: set it up
1. Check for `~/.builder-secrets/keybox.py` (on Windows `%USERPROFILE%\.builder-secrets\keybox.py`). If it's there, skip to "Every time".
2. Make the folder `~/.builder-secrets`, readable only by them (`chmod 700` on Mac and Linux).
3. Copy `${CLAUDE_PLUGIN_ROOT}/keybox/keybox.py` into it. If `python3` isn't installed (try `python3 --version`, and `python --version` on Windows), copy `${CLAUDE_PLUGIN_ROOT}/keybox/keybox.js` instead and use `node`.
4. Prove it with a fake key: run it for `TEST_KEY`, tell them to paste any made-up word and tap Save, wait for "Saved", say "Saved TEST_KEY" (name and length only), then delete `~/.builder-secrets/test_key.env`.
5. Add this to their `CLAUDE.md` (create it if there isn't one) under a heading "Keys": "Never ask me to paste a key, token or secret in the chat. Run my Key Box (`python3 ~/.builder-secrets/keybox.py VARIABLE_NAME \"Plain label\"`, or `node ~/.builder-secrets/keybox.js ...`), open the link, tell me in one plain sentence what to paste, wait for Saved, and confirm by name and length only."

## Every time you need a key
1. Say, in one plain sentence, what you need and where they get it (open the company's page for them in Chrome if you can, and stop at the Create button, which is theirs).
2. Run: `python3 ~/.builder-secrets/keybox.py VARIABLE_NAME "Plain label"` (for example `CLOUDFLARE_TOKEN "Cloudflare token"`). It prints one link that starts with `127.0.0.1` and opens it in their browser.
3. Tell them: "A box opened in your browser. Paste your <label> there and tap Save. Don't paste it here."
4. Wait for the line `Saved VARIABLE_NAME (N characters)`. It closes by itself after one save or 10 minutes. If it timed out, offer to run it again.
5. Confirm in one line, by name only: "Saved CLOUDFLARE_TOKEN." Then use it from the environment or `~/.builder-secrets/<name>.env`. Never print it, repeat it, put it in code, a page, a log or a commit, and never read the file back into the chat.

## If a key lands in the chat anyway
Don't repeat it. Move it into `~/.builder-secrets/<service>.env` (readable only by them), confirm by name only, tell them kindly to use the Key Box next time, and, if it's a live key that could cost money or expose data, tell them to turn that key off and make a new one (you can open the page for them).

## Never
Passwords, bank or card numbers, Social Security numbers and recovery codes don't go in the Key Box or the chat. The student types those themselves, on the real site.
