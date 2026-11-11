---
description: Get the newest Build Until version right now, and see what changed
---

Update Build Until for this student, then tell them what's new in plain words.

1. Say in one line: "I'll check for a newer Build Until and install it. Okay?" Wait for yes.
2. Run:
   ```
   claude plugin marketplace update build-until
   claude plugin update build-until@build-until
   ```
   If `claude` isn't found, tell them the same thing can be done from the Claude app: click the **+** in the prompt box → **Plugins** → **Build Until** → **Update**.
3. Make sure automatic updates stay on: the student's `~/.claude/settings.json` should have `extraKnownMarketplaces.build-until.autoUpdate` set to `true` (source: GitHub repo `jessefwood/build-until-plugins`). If it's missing, offer to add it, merging with their settings and keeping a backup first.
4. Read `CHANGELOG.md` at the root of the updated marketplace (in Claude Code's plugin marketplaces folder, or https://raw.githubusercontent.com/jessefwood/build-until-plugins/main/CHANGELOG.md) and tell them the newest entries in three short lines or fewer. Lead with anything they need to do, and offer to do it for them, one step at a time.
5. Tell them: "Type /reload-plugins in the box below (or start a new session) to switch to the new version."
6. If the setup wizard's progress file shows setup isn't finished, offer to keep going with it.
7. If the Build Until course connector is connected, send `log_progress` with `Installer: updated to <version>.`

Never change their own files, site or settings beyond the Build Until plugin without asking.
