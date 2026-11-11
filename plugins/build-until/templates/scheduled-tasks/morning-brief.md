---
name: morning-brief
schedule: "0 7 * * 1-5"
timezone: "{TIME_ZONE}"
description: Weekday morning brief for {BUSINESS_NAME}
---

Good morning brief for {FIRST_NAME}. Read only; send nothing.

1. Today's calendar: each meeting with time, who, and one line on what to bring. Flag clashes and anything with no video link.
2. Inbox: what needs {FIRST_NAME} today, what can wait, what's junk. Draft replies for the top three; send none.
3. Texts (if connected): who's waiting on an answer.
4. My Build (if the Build Until connector is connected): today's next step in one line.
5. One thing to do first today, and why, in one sentence.

Keep it to one screen. Save it to {BUILDER_BOX}/Briefs/<date>.md and show it when {FIRST_NAME} opens Claude.
