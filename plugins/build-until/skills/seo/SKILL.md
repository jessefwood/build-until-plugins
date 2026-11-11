---
name: seo
description: Gets a Build On Purpose student found on Google and in AI answers (ChatGPT, Claude, Perplexity, Gemini, Google AI Overviews, Copilot). Use automatically whenever you write or update a blog post, page, launch or site for the student or for one of their clients, and when they ask about SEO, AI search, getting found, ranking, keywords, Search Console, schema, a blog post, or their 10 launch posts. Does question and keyword research first, writes answer-first posts with schema and internal links, submits them, and runs a monthly check.
---

# Get found: SEO + AI search

Google and the AI answer engines reward the same thing: the clearest, most honest answer to a real question, from a real person who has done it. The student is that person. You turn their know-how into pages that get found. Run this routine on every post, page and launch without being asked. It works the same for the student's clients' sites: the client is the author there.

## Who the author is
The student (or their brand, or their client) is always the author, with their name, short bio, photo and profile links. Never name AI as the author, and never say "written by AI." Write in their voice from their Voice File and Brand File: plain words, short sentences, no dashes, no AI-sounding phrases.

## Expert first, every post
Before writing, show them the plan in 5 short lines, in this shape:
```
I hear you. Here's the best way to do this one:
Main phrase: "how much does a wedding photographer cost in norfolk"
Questions it answers: 6 (from People Also Ask, autocomplete and your own customers)
Angle: real 2026 price ranges from your own bookings, plus who it's not for
My pick is this one. Approve it, or tell me what you'd like different.
```
If they don't answer and it's a routine weekly post inside their decision rights, go with your pick.

## 1. Research (before writing)
1. Start from a real customer question. Check their Builder Box for their weekly customer questions; ask once for 10 if there's no list, and save them.
2. Expand it with: Google autocomplete (the phrase plus how, what, why, can, is, vs, for, cost, near, and a to z), People Also Ask, related searches, Reddit and Quora wording ("reddit" + topic), and Google Trends to pick the more popular wording. Use their browser (Claude in Chrome) or web search.
3. If Search Console is connected (or they share an export), check which searches already show their site, especially questions they appear for but don't answer.
4. Look at the top 5 Google results and any AI Overview: what type of page wins, and what they all miss.
5. Pick ONE main phrase, written the way people type it, and 5 to 10 real questions. **One post per question:** check their site for a page on it first. If one exists, update that page instead of making a new one.

## 2. Write it (the answer-first template)
- **Title** under 60 characters, the question or promise, main phrase near the front. **Meta description** under 155 characters. **Short URL** with the main phrase.
- **First 40 to 60 words answer the question directly.** No warm-up. The key detail, and who it's for.
- **Every heading is a real question** people search; the first sentence under it answers it.
- **Proof:** one statistic with a link to a trusted source, one quote (theirs, or a customer's with permission), and one first-hand example from them (a story, a photo, a screenshot, their own numbers). Ask them for the story if you don't have one. Never invent stories, numbers, reviews or quotes.
- **Say who it's not for.**
- **End with 4 to 6 FAQs** with short answers.
- **Links:** at least 3 to their other pages and 2 to trusted outside sources (government, official pages).
- **One clear next step:** book, buy, join or download.
- Author name and short bio on the post.
- Money, health or legal topics: teach, don't promise results; add any disclosure their field requires.

## 3. Technical (every post)
- **Schema** (JSON-LD) that matches what's on the page: BlogPosting with the student as author, BreadcrumbList, FAQPage for the FAQ, Organization and Person site-wide, LocalBusiness if they serve a local area.
- Fast on phones; images compressed, with alt text.
- Add it to the sitemap, request indexing in Search Console (when connected), and ping IndexNow.
- robots.txt allows search and AI crawlers: Googlebot, Bingbot, OAI-SearchBot, PerplexityBot, ClaudeBot, Claude-SearchBot.
- The same day, link to the new post from 2 older related posts.
- Same business name and description everywhere on the site.
Skip old tricks that don't help: keyword stuffing, special "AI files", near-duplicate pages (like the same page with different city names).

## 4. Launch: 10 posts, then 1 a week
Every site launches with 10 posts, then one new post every week (and every few months, refresh the best posts with real new info instead of only adding):
1. The big guide to their main topic (links to the other 9).
2. "How much does it cost?"
3. An honest "you vs the other option" comparison.
4. "Best alternative to ___ for ___."
5. A step-by-step "how to ___."
6. "Is ___ worth it?" (or safe, or legal).
7. "___ for (their best customer type)."
8. Mistakes or myths they see all the time.
9. Their real story or their own numbers (original info gets quoted by AI).
10. A glossary or FAQ page with short answers.
Write the posts people still click even when AI answers simple facts: prices, comparisons, how-tos, local, and "is this right for me."

## 5. Tell Google and Bing (one time, with them, in their Chrome)
Set it up once so it covers the whole domain and every future post.
- **Google Search Console:** open https://search.google.com/search-console in their Chrome. They sign in with their business Google account. **Add property** → **Domain** → their domain → **Continue**. You add the verification record to their DNS (with their OK), then they tap **Verify**. Submit the sitemap.
- **Bing Webmaster Tools** (also feeds Copilot): https://www.bing.com/webmasters → sign in → **Import from Google Search Console** → **Continue** → **Import**.
- **Google Business Profile** (local businesses only): https://business.google.com → **Manage now**. Pick the most exact category, add services, hours and real photos. Help them ask happy customers for reviews and draft replies to every review (they approve before anything posts).
Sign-in taps and codes are theirs; you do the rest.

## 6. Get found by AI (around the web)
On the site you handle: answer first, question headings, FAQ, author info and profile links, the same name and description everywhere, crawlers allowed, fast phone pages.
Around the web, help them with: the same name, photo, bio and link on LinkedIn, Instagram, Facebook and YouTube; podcast guest spots (each show page helps); helpful Reddit or Quora answers as themselves, saying they own the business when they mention it; a short YouTube video for the big guide; real reviews, never fake ones. Draft everything; nothing posts without their yes.

## 7. The monthly check (scheduled task)
Offer to set up `${CLAUDE_PLUGIN_ROOT}/templates/scheduled-tasks/seo-monthly-check.md` (first Monday of the month), filled in with their domain, first name and Builder Box path. Create it with a scheduled task tool if you have one and run its first run yourself; otherwise walk them through Claude app → **Code** → **Scheduled** → **New task**. Each month it:
1. Checks Search Console for what people searched to find them.
2. Improves posts sitting on page 2 (the fastest win).
3. Adds answers to questions they show up for but don't answer yet.
4. Rewrites titles that get seen but not clicked.
5. Refreshes old posts with real new info.
6. Asks ChatGPT, Perplexity and Google their top 5 customer questions, and notes whether they're mentioned and who is mentioned instead (and what those sites have that theirs doesn't).
7. Sends a 5-line summary: visits, best posts, AI mentions, what it fixed, one question.

## Never
- Copy anyone's content.
- Fake reviews, numbers, quotes or testimonials.
- Near-duplicate pages, keyword stuffing, or promised rankings or results.
- Name AI as the author.
- Ask for passwords or keys in the chat. Keys go in a secure form; sign-ins are theirs.
- Publish anything they'd be embarrassed to read out loud to a customer.
