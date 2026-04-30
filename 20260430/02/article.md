# How to build a content idea engine in n8n that never runs dry

**Author:** Aaron ([@IAmAaronWill](https://x.com/IAmAaronWill))  
**Published:** April 29, 2026  
**Source:** [How to build a content idea engine in n8n that never runs dry](https://x.com/Zephyr_hg/status/2049459882844143696)

Most people running a personal brand burn out within 90 days.

Not because they can't write. Because they can't think of what to write.

Every morning becomes the same fight: stare at a blank screen, scroll X for inspiration, end up posting something generic, hate it, repeat tomorrow.

The fix isn't discipline. It's a system that does the thinking before you sit down.

Here's the complete build for an n8n workflow that hands you 30 ready-to-write content ideas every Monday morning, pulled from your actual life, your actual work, and your actual audience. Specific nodes, specific prompts, specific outputs.

By the end of this you'll have a system that does the hardest 80% of content creation while you sleep.

## What this system actually does

The engine runs once a week on a schedule. It pulls raw signal from every place your ideas already live, hands that signal to Claude with a prompt that knows your voice and your audience, and drops 30 fully-formed content ideas into a single document you can work from all week.

You don't sit down to "think of content" anymore. You sit down to write the third idea on the list.

That's the entire game. Removing the part of content creation that kills most people.

The system has five jobs:

1. Collect raw signal from your week
2. Structure that signal so Claude can use it
3. Send it to Claude with a prompt that knows your voice
4. Parse the output into usable content briefs
5. Drop those briefs into a doc or database you'll actually open

Each job is one section of the workflow. Build them in order and you'll have the whole thing running in an afternoon.

## The five sources you pull from

The reason most idea generators output garbage is they're pulling from nothing. You ask ChatGPT for content ideas and it gives you the same recycled list everyone else gets because it has no context.

Your engine needs context. Real context. From places that already contain the raw material of good content.

The sources that actually matter:

**Your own writing.** Notes, voice memos, half-finished drafts, ideas you typed into your phone at 2am. This is where your best thinking lives and dies. Most people lose 90% of it because there's no system for resurfacing it.

**Your client work.** Problems you solved this week. Conversations on calls. Patterns across multiple clients. Questions clients keep asking. This is the stuff nobody else can write because they haven't lived it. It's also the stuff that converts, because it's tied directly to the work you sell.

**Your audience.** DMs, comments, replies, questions you keep getting asked. If three people asked you the same thing this week, that's a post. If you've answered the same question on five sales calls this month, that's a post. Your audience tells you what to write if you actually listen.

**Your saves and bookmarks.** Articles, posts, threads, tweets you saved because something hit. You saved them for a reason. Most people never go back to them. Your engine should pull them back into circulation as raw material for new angles.

**Your past content that performed.** What hit before will hit again with a new angle. The engine needs to know what your top posts were so it can use them as a reference point for what your audience actually responds to.

In n8n, each of these is a separate node pulling from wherever you actually keep that data. Notion, Google Docs, a Twitter export, Apify scraping your own profile, your CRM, your email, whatever. The point isn't the specific tool. The point is you're feeding the system real signal from your life instead of asking AI to invent ideas from nothing.

If you don't currently track these things in any centralised way, that's the first job. Spend a week capturing them. A simple Notion database with five tables — notes, client problems, audience questions, saves, top posts — is enough. Once it's set up, you fill it as you go and the engine pulls from it weekly.

## The n8n build, node by node

Here's the workflow structure top to bottom.

**1. Schedule trigger.**

Set to fire every Monday at 6am. The system runs while you sleep. By the time you sit down with coffee, the ideas are waiting.

**2. The data collection nodes.**

One node per source. Each one pulls the last 7 days of data from that source.

For Notion sources, use the Notion node with a filter on "last edited time is within the past 7 days". This pulls only the new stuff, not your entire database every week.

For Google Docs or Sheets, use the respective nodes with date filters. Same logic.

For your past Twitter content, you can use Apify's Twitter scraper node, or pull from a Google Sheet you update manually with your top posts.

For client problems, the simplest version is a Notion or Sheets database where you log a one-line note after every client call. The engine pulls the past week's entries.

For DMs and audience questions, this is harder to automate fully. The pragmatic approach: keep a running Notion page where you paste in interesting DMs, comments, and questions as they come up during the week. The engine pulls that page on Monday.

Keep each pull small and recent. You don't need everything. You need this week's signal. If you try to feed Claude six months of data, the output gets worse, not better.

**3. The merge and structure node.**

After collecting from each source, you'll have five separate data streams. Use a Merge node to combine them, then a Set node to label each chunk clearly.

The Set node should output something like:

```
PERSONAL NOTES THIS WEEK:
[content from notes pull]

CLIENT PROBLEMS THIS WEEK:
[content from client log]

AUDIENCE QUESTIONS THIS WEEK:
[content from DM/comment log]

SAVES THIS WEEK:
[content from bookmarks pull]

TOP PERFORMING POSTS (LAST 90 DAYS):
[content from analytics pull]
```

This labelling is critical. Without it, Claude treats everything as one undifferentiated blob and the output suffers. With it, Claude knows the difference between "something I noted down" and "something my audience asked", and weights the ideas accordingly.

**4. The Claude API node.**

This is where the magic happens. Use the HTTP Request node configured to hit Claude's API, or the dedicated Anthropic node if you've installed it.

Model: claude-opus-4-7 if you want the best output quality, claude-sonnet-4-6 if you want speed and lower cost. For a weekly run, the cost difference is negligible. Use Opus.

Max tokens: 8000. You're asking for 30 detailed ideas. You need the room.

System prompt and user prompt structure: covered in the next section.

**5. The parser node.**

Claude returns a single block of text. You need to split it into 30 individual idea entries so they can be written to a database row by row.

Easiest approach: tell Claude in the prompt to return the output as JSON. Then use a Code node in n8n to parse the JSON into individual items. Each item becomes a row in your output.

If JSON feels fragile, an alternative is asking Claude to separate each idea with a specific delimiter like `---IDEA---` and using the Split node to break the response into chunks.

**6. The output node.**

Send the parsed ideas to wherever you'll actually open them on Monday morning.

The setup I recommend: a Notion database with columns for hook, angle, format, takeaway, source, and status. The engine creates 30 new rows every Monday. You work through them during the week, marking each one as written, scheduled, or skipped.

If you don't use Notion, a Google Doc with the ideas formatted as a numbered list works. Or have it emailed to you. Pick the place you'll actually open.

That's the whole build. Six functional sections. A confident n8n user gets it running in three to four hours. A first-timer in a day.

## The prompt that makes it work

A bad prompt produces 30 versions of "5 tips for productivity". A good prompt produces 30 ideas you actually want to write.

The prompt needs four things, in this order:

**Voice context.**

Two or three paragraphs describing how you write, what you don't do, what your tone sounds like. Be specific.

Bad: "Write in a casual, conversational tone."

Good: "Direct and blunt. Short paragraphs of one to three sentences. No corporate language, no buzzwords, no consulting speak. Swears occasionally when it fits. Always uses contractions. No em dashes. Writes like someone explaining something at a pub, not someone presenting at a conference."

The more specific the voice description, the closer the output sounds to you.

**Audience context.**

Who reads this. What they want. What they're sick of seeing. What stage of the journey they're at.

Bad: "Entrepreneurs and business owners."

Good: "Solopreneurs and small agency owners building automation businesses. They already know n8n basics. They want commercial angles, pricing logic, specific build advice. They're tired of beginner content like 'what is an API'. Assume technical literacy. Assume they want to make money."

**Performance context.**

Your top three to five posts of all time, pasted into the prompt verbatim. With the engagement numbers if you have them.

This is the single biggest lever. It teaches Claude what your audience actually responds to, not what you think they should respond to.

You can pull this manually once and hardcode it into the prompt. Update it every couple of months as new top performers emerge.

**The output spec.**

Tell Claude exactly what you want. Not just a topic. Each idea needs four fields:

- **Hook**: the opening line of the post or article
- **Angle**: what makes this idea different from a generic version of the same topic
- **Format**: post, thread, article, or video
- **Takeaway**: the specific thing the reader leaves knowing or able to do

30 ideas, all four fields per idea, returned as JSON.

When the prompt has all four sections, the output stops being generic. It starts sounding like ideas you'd have come up with on your best day, just compressed into 30 seconds of Claude's processing time instead of three hours of your thinking.

## How to feed the system without it becoming work

The engine is only as good as the data going in. If your sources are empty, the output is empty.

The trick is making the inputs frictionless to maintain.

**For notes**: voice-memo everything during the week. Have a single Notion page or Apple Notes doc where you dump thoughts as they happen. Don't structure them. Don't refine them. Just capture. The engine processes the rough material.

**For client work**: after every call, spend 60 seconds logging the core problem the client surfaced and how you solved it. One line in a database. That's it.

**For audience questions**: when someone asks you something good in DMs or comments, copy and paste the question into your Notion log. Takes five seconds. Pays back massively.

**For saves**: use whatever native save feature the platform has. Once a week the engine pulls them.

**For top posts**: update once a quarter. Pull your analytics, find the top five, paste them into the prompt. Done.

The whole input maintenance routine takes maybe 10 minutes a day spread across the week. The output is 30 content ideas a week with no creative effort on your part. That's the trade.

## Why this beats every other approach

You're not asking AI to be creative for you. You're asking it to be a better-rested, better-organised version of you on autopilot, with access to all the inputs you'd use anyway if you had time to sit down and think properly.

The signal is yours. The voice is yours. The audience knowledge is yours. Claude is just doing the synthesis layer that your tired brain at 9am on a Monday can't do well.

That's why the output doesn't sound like AI slop. The foundation isn't AI. It's your real life, run through a system that organises it into content.

The other reason this works: it removes the worst part of content creation, which is the cold start. Going from zero to first draft is where most people quit. With 30 ideas waiting on a Monday morning, you skip the hardest step every time.

## What to do today

Open n8n. Create a new workflow.

Add a Schedule trigger. Set it to Monday 6am.

Connect one source first. The easiest one. Probably a Notion page or Google Doc where you already dump notes. Get that pulling correctly with a 7-day filter.

Add the Claude API node. Write a rough version of the prompt with all four sections. Don't perfect it yet. Just get something working end-to-end.

Run it manually. Look at the output. It'll be 60% of the way there.

Add the second source. Run it again. Output gets better.

Keep adding sources until all five are connected. Tweak the prompt based on what's missing or wrong in the output. Run it three or four times across different weeks.

Within three weeks you'll have a system that produces better content ideas than you ever did on your own, with zero ongoing effort beyond capturing the raw material as you live your week.

The whole point of building things in n8n is removing the work you hate so you can do more of the work you don't.

Content ideation is the work most people hate. Build this once, and it's gone.
