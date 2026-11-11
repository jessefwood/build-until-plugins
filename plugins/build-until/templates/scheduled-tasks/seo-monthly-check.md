---
name: seo-monthly-check
schedule: "0 9 * * 1"
timezone: "{TIME_ZONE}"
description: Monthly SEO + AI search check for {DOMAIN}
---

Use the build-until seo skill for {DOMAIN} ({FIRST_NAME} is the author). This is the monthly check. It is scheduled every Monday: if today's day of the month is after the 7th, stop right away and do nothing (it runs on the first Monday only).
1. Search Console: what people searched to find the site this month.
2. Improve posts ranking on page 2.
3. Add answers to question searches the site shows up for but doesn't answer yet.
4. Rewrite titles that get seen but not clicked.
5. Refresh old posts with real new info (never invent numbers, stories or reviews).
6. Ask ChatGPT, Perplexity and Google {FIRST_NAME}'s top 5 customer questions. Note whether {FIRST_NAME} is mentioned, who is mentioned instead, and what those sites have that this one doesn't.
Make site changes inside {FIRST_NAME}'s decision rights; anything public that's new (a new page, a post) waits for a yes. Save the report to {BUILDER_BOX}/SEO/<YYYY-MM>.md, then send {FIRST_NAME} a 5-line summary: visits, best posts, AI mentions, what you fixed, and at most one question.
