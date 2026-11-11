# Build Until Installer

One paste sets up a Build On Purpose student's AI brand builder.

## Start here

Open the Claude app on your computer → click **Code** at the top → **New session** (it should say **this computer**, not cloud) → paste this and press Return:

```
Install Build Until: run "claude plugin marketplace add jessefwood/build-until-plugins" and then "claude plugin install build-until@build-until", then open the setup-wizard skill it installed and start my setup, one step at a time.
```

Your assistant installs Build Until, then walks you through setup one step at a time. It asks before it does anything, and you always type your own passwords and card details.

## What's inside

- `/build-until:setup`, the setup wizard. Stop anytime; say "keep going with my setup" to pick up where you left off.
- `/build-until:move-me-in`, bring what's worth keeping over from ChatGPT, Gemini, Cowork and others.
- `/build-until:update`, get the newest version now. Updates also arrive by themselves.
- Skills: Start with Claude basics, get found (SEO + AI search), reels that stop the scroll, your integrator (decision rights, weekly Same Page check-in, monthly DEAL audit), weekly CEO scorecard, monthly CFO audit.
- Connectors for Let's Sit Down and In Writing, using your own keys, kept in your computer's secure credential store.
- Scheduled task templates: morning brief, Same Page check-in, DEAL audit, SEO monthly check, CEO scorecard, CFO audit, Monday upgrade check.

No secrets live in this repository, ever.

## For maintainers

- Bump `version` in `plugins/build-until/.claude-plugin/plugin.json` on every change, or students won't get it, and add a line to `CHANGELOG.md`.
- Check with `claude plugin validate .` before pushing.
