---
description: Start or resume your Build Until setup, one step at a time
---

Use the build-until `setup-wizard` skill and follow it exactly.

First read the progress file `~/.build-until/setup.json`. If it shows steps already done, welcome the student back and continue from the next step that isn't done. If it doesn't exist, start at Step 1, Welcome.

Before anything else, make sure automatic updates are on for Build Until, so every improvement reaches this student the same day. Read the student's `~/.claude/settings.json`. If `extraKnownMarketplaces` has no `build-until` entry with `"autoUpdate": true`, say in one line: "I'll turn on automatic updates for Build Until, so you always have the newest version. Okay?" On yes, add (merging, never overwriting other settings, and keeping a backup copy first as `settings.json.bak`):

```json
"extraKnownMarketplaces": {
  "build-until": {
    "source": { "source": "github", "repo": "jessefwood/build-until-plugins" },
    "autoUpdate": true
  }
}
```

If the student typed anything after the command, treat it as their answer or a note about where they are: $ARGUMENTS
