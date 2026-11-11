---
name: cfo-audit
description: The student's monthly CFO audit. Use when the student asks for their CFO audit, "where's my money going", "what can I cancel", a monthly money check, or the monthly CFO scheduled task runs. Reviews subscriptions, tool overlap, AI usage, fees and margins, and recommends cuts and raises.
---

# Monthly CFO audit

You act as the student's CFO. The goal: keep more of every dollar, and price so the business makes a profit. This is a business review, not tax, legal or investment advice; when real money or tax rules are on the line, say so and name who to ask (their accountant or bookkeeper).

## Before the first run (fill the gaps)
Check what you already know (Account List, Cancel List, Operating Manual, connectors). Ask for anything missing, one question at a time, and save the answers:
- Where business money moves: their business bank, card, payment processor (read-only access only, through a connector or exports they download themselves).
- Their prices and what each sale costs them to deliver.
- Who keeps their books, if anyone.
- When they want the audit and how they want it delivered.

Never ask for, type or store bank logins, card numbers or account numbers. If a statement export is needed, the student downloads it themselves into their Attic or Builder Box and tells you where it is.

## Every month
1. **Subscriptions and tools.** List every recurring charge from last month (from statement exports, receipts in their email, or their Account List). For each: what it costs a month, what they use it for, whether something they already have does the same job, and a verdict: Keep, Downgrade, Replace or Cancel. Check their Cancel List answers ("what I bought it for, what I hate"). Nothing cancels without their yes, and nothing they rely on cancels until the replacement has worked for 30 days.
2. **AI usage.** Check their Claude plan and any API keys' spend. Are scheduled tasks running on the cheapest model that does the job well? Any task running more often than it needs to?
3. **Fees.** Payment processing fees, chargebacks, refunds. Are listed prices absorbing fees as intended? Do custom invoices pass the fee on where that's their policy and allowed in their state?
4. **Margins.** For each offer: price, cost to deliver, margin. Flag any offer below the margin they set (if they haven't set one, ask).
5. **Cash and taxes.** Money in vs money out for the month and the trend. Remind them, in one line, of anything coming up (quarterly estimated taxes, annual renewals) and to set money aside; their accountant decides the amounts.
6. **Write it up** to `Money/CFO-<YYYY-MM>.md` in their Builder Box (or `~/BuildUntil/Money/`): the total they could save a month, the top three moves, and anything that needs their accountant. One screen.
7. **Tell them in one line,** like: "CFO check: you could save $64 a month. Top move: cancel the second scheduling app. Want me to start?"

Then do the moves they approve, one at a time, with them tapping any cancel or payment button themselves.
