# How to build a team of AI Agents that actually work together (Full Course)

**Author:** Kanika ([@KanikaBK](https://x.com/KanikaBK))  
**Published:** May 25, 2026  
**Source:** [How to build a team of AI Agents that actually work together (Full Course)](https://x.com/KanikaBK/status/2058817146411692358)

Most people build one AI agent, watch it fail at complex tasks, and conclude AI agents are not ready. The real problem is architecture. This full course shows the exact mental model, team structures, tools, and production patterns for building multi-agent systems that produce reliable, high-quality output.

A single agent given a complex job is like hiring one person to simultaneously research, write, design, code, and publish while remembering every detail of every step.

It breaks down under complexity. The solution is what human teams figured out centuries ago: specialization, clear roles, and a manager who coordinates.

This is the complete course on building a team of AI agents that actually work together — from the mental model to the tools to production-ready patterns.

I have tried to include every point possible from my experience of building AI agents. Hope you are ready!

## THE CORE MENTAL SHIFT

Before you write a single prompt, you need to change how you think about agents.

### Think in tasks, not roles

The most common mistake when building multi-agent systems is replicating a human org chart. You create a "Research Agent," a "Writing Agent," and a "Marketing Agent" — and wonder why the outputs are inconsistent and hard to debug.

The shift that changes everything: think in tasks, not roles.

AI agents perform best when they have one clear goal, a limited set of specific tools, and precise instructions for a single discrete task. An agent with a broad remit makes vague decisions. An agent with a narrow task produces consistent, reliable output.

Instead of a "Content Agent," build:

- A Research Task Agent - takes a topic, returns structured research notes.
- A Brief Writer Agent - takes research notes, returns a content brief.
- A Draft Writer Agent - takes a brief, returns a full draft.
- A Editor Agent - takes a draft, returns an edited version with critique.
- A Publisher Agent - takes the final copy, formats and publishes it.

Each agent is simple, testable, and replaceable. The system as a whole is powerful.

### Why multi-agent systems outperform single agents

Research from MIT and Google Brain found that when agents debate and critique each other's outputs, both reasoning quality and factual accuracy improve significantly — even when one agent starts with an incorrect answer, the critique from other agents corrects the trajectory.

Multi-agent systems are not just about parallelism. They are about quality through specialization and verification.

## PART 1: THE FOUR CORE AGENT ROLES

Every effective multi-agent team has agents in four functional categories. You do not need one agent per category but every production team needs all four functions covered.

### Role 1: The Orchestrator (Manager Agent)

The Orchestrator receives the top-level task, breaks it into subtasks, assigns each to the right specialist agent, collects outputs, and synthesizes the final result. It never does the actual work, it only coordinates.

What it needs:

- A clear description of every specialist agent available to it and what each one does.
- Rules for when to delegate vs. when to synthesize.
- A quality gate, criteria for when a subtask output is good enough to pass on.

Example system prompt for an Orchestrator:

![](images/img-01.jpg)

```
Prompt 1
You are a project manager overseeing a team of specialist AI agents.

Your team:
- Research Agent: searches the web and returns structured summaries
- Writer Agent: takes a brief and writes long-form content
- Editor Agent: critiques drafts and returns specific improvements
- Publisher Agent: formats content and posts to the target platform

When given a task:
1. Break it into discrete subtasks
2. Assign each subtask to the appropriate agent
3. Review each output before passing it to the next agent
4. Return the final synthesized result

If an agent's output does not meet the quality criteria, return it with specific feedback and request a revision.
```

### Role 2: The Researcher

The Researcher's only job is to find, retrieve, and structure information. It does not write, analyze, or create, it gathers.

What it needs:

- Web search tools (Perplexity API, Serper, Brave Search API)
- A URL fetcher for reading full pages
- A structured output format so its results are always easy for downstream agents to use

Example output format to enforce:

```
Topic: [topic]
Key Facts: [bulleted list]
Statistics: [with sources]
Competing Perspectives: [brief list]
Sources: [URLs]
```

### Role 3: The Specialist Producers

These are the workers, one agent per production task. Common specialist agents include:

- Writer Agent: takes a brief and writes a draft.
- Coder Agent: takes requirements and writes code.
- Data Analyst Agent: takes raw data and returns insights.
- Designer Brief Agent: takes a concept and returns a visual design brief.
- Outreach Agent: takes lead data and writes personalized messages.

Each specialist agent should have:

- A tightly scoped system prompt (one job only).
- The minimum tools needed for that job.
- An explicit output format that downstream agents can parse reliably.

### Role 4: The critic / reviewer

This is the most underbuilt role in most agent systems - and the one that matters most for quality. The Critic receives any agent's output, evaluates it against defined criteria, and returns specific, actionable feedback.

A well-designed Critic does not say "this is bad." It says:

- "The introduction buries the main claim in paragraph three. Move it to sentence one."
- "Claim in paragraph two is unsubstantiated. Add a source or remove it."
- "Tone is inconsistent - paragraphs 1–3 are formal, paragraphs 4–6 are casual. Standardize."

The Critic agent is what separates a multi-agent system that produces mediocre output from one that produces work you are proud to publish.

## PART 2: THE THREE ARCHITECTURES

Multi-agent teams follow one of three structures. Understanding which to use determines everything about how you build.

### Architecture 1: Sequential (Pipeline)

Agents run one after another. The output of Agent A becomes the input of Agent B.

```
Input → Research Agent → Brief Agent → Writer Agent → Editor Agent → Output
```

Use when: Tasks have a clear linear flow. Each step depends on the previous one completing correctly.

Best for: Content creation, research reports, proposal generation, data processing pipelines.

The risk: If Agent 2 produces poor output, every subsequent agent inherits that error. Add a quality gate between each step.

### Architecture 2: Parallel (Fan-Out)

An Orchestrator splits a task and sends parts to multiple agents simultaneously. All agents work at the same time. The Orchestrator collects and synthesizes results.

```
                       ┌→ Research Agent A → ┐
Input → Orchestrator   ├→ Research Agent B → ├→ Synthesis Agent → Output
                       └→ Research Agent C → ┘
```

Use when: Tasks can be divided into independent parallel workstreams. Dramatically reduces total run time.

Best for: Multi-source research, competitive analysis across multiple companies, processing large batches of items.

The risk: Synthesis is hard. The Orchestrator needs clear rules for how to combine parallel outputs that might conflict.

### Architecture 3: Hierarchical (Multi-Layer)

Multiple layers of orchestration. A top-level Orchestrator manages mid-level Orchestrators, each of which manages specialist agents.

![](images/img-02.jpg)

```
CEO Agent
├── Content Orchestrator
│   ├── Research Agent
│   ├── Writer Agent
│   └── Editor Agent
└── Distribution Orchestrator
    ├── SEO Agent
    ├── Social Agent
    └── Email Agent
```

Use when: The task is complex enough to require coordinating multiple pipelines, not just multiple agents.

Best for: End-to-end business process automation, complex research and publishing workflows, full marketing campaign automation.

The risk: Complexity compounds quickly. Every layer adds latency, cost, and potential failure points. Only go hierarchical when sequential and parallel genuinely cannot solve your problem.

## PART 3: THE TOOLS STACK

### No-Code / Low-Code (Start Here)

**Make (formerly Integromat)**

The best visual builder for multi-agent workflows. Connect Claude, OpenAI, or any LLM via API. Build sequential pipelines visually. Add conditional branches, error handlers, and parallel routes without code.

**n8n**

Open-source alternative to Make. Self-hostable, more flexible, better for complex workflows with custom logic. Has native AI agent nodes with tool-calling support.

**Relevance AI**

Built specifically for multi-agent systems. Lets you create agents with tool access, connect them into teams, and define handoff rules between agents visually. Strong for business workflow automation.

### Code-Based Frameworks (For full control)

**Claude API with tool use**

Build agents directly with the Anthropic Claude API. Each agent is a system prompt + a set of tools (functions it can call). The Orchestrator calls Claude with a task, Claude calls tools, tools return results, Claude synthesizes.

**LangGraph**

A graph-based framework for building multi-agent workflows where nodes are agents and edges define handoffs. Excellent for complex conditional flows where the next agent depends on the current output.

**Agno (formerly Phidata)**

Framework specifically designed for building agent teams with hierarchical orchestration. Has built-in support for team memory, agent-to-agent communication, and parallel execution.

**AutoGen (Microsoft)**

Multi-agent conversation framework where agents message each other directly. Well-suited for agents that need to debate, critique, and revise in a conversation loop.

## PART 4: BUILD YOUR FIRST AGENT TEAM (STEP BY STEP)

We will build a Content Research and Writing Team - a three-agent system that takes a topic and produces a polished, research-backed article draft. This is the most practical starting point and the architecture transfers to dozens of other use cases.

![](images/img-03.jpg)

### Step 1: Build the Research Agent

System prompt:

```
You are a research specialist. Your only job is to research a given topic and return structured notes.

When given a topic and angle:
1. Search for the most relevant, recent, and credible information
2. Find 3–5 key insights, each with supporting evidence
3. Identify 2–3 competing perspectives or counterarguments
4. Find 2–3 specific statistics or data points with sources
5. Note any expert voices or credible sources worth quoting

Return your output in this exact format:
---
TOPIC: [topic]
ANGLE: [angle]
KEY INSIGHTS:
- [insight 1] (Source: [URL])
- [insight 2] (Source: [URL])
STATISTICS:
- [stat 1] (Source: [URL])
COUNTERARGUMENTS:
- [counterargument 1]
NOTABLE SOURCES:
- [source name]: [URL]
---

Do not write prose. Do not add commentary. Return structured notes only.
```

Tools to give it: Web search (Perplexity API or Serper API), URL fetcher.

### Step 2: Build the Writer Agent

System prompt:

```
You are a skilled long-form writer. Your only job is to write a clear, engaging article draft from research notes.

When given research notes and a brief:
1. Write a compelling opening that hooks the reader immediately
2. Develop the key insights into full sections with clear subheadings
3. Use the statistics and sources naturally within the prose — never in a list
4. Address counterarguments honestly — they build credibility
5. Close with a clear, actionable takeaway

Writing standards:
- Active voice throughout
- Sentences under 25 words on average
- No corporate jargon, no filler phrases
- Every section should make one clear point
- Target length: 800–1,200 words unless specified otherwise

Return only the article draft. No meta-commentary about the draft.
```

Tools to give it: None. It only needs the research notes as input.

### Step 3: Build the Editor Agent

System prompt:

```
You are a senior editor. Your job is to critique a draft and return specific, actionable improvements.

When given an article draft:
1. Identify the three most important structural issues (if any)
2. Flag any claims that need stronger evidence or sourcing
3. Mark any sections where the logic is unclear or the point is buried
4. Highlight the two strongest parts of the draft (what to protect)
5. Rewrite the opening paragraph to make it stronger

Return your output in this format:
---
STRUCTURAL ISSUES:
1. [issue + specific fix]
2. [issue + specific fix]
EVIDENCE GAPS:
- [claim that needs support]
CLARITY ISSUES:
- [paragraph/section + what is unclear]
STRONGEST SECTIONS:
- [section + why it works]
REVISED OPENING:
[rewritten opening paragraph]
---
```

Tools to give it: None.

### Step 4: Build the Orchestrator

System prompt:

```
You are a content project manager. You coordinate a team of specialist agents to produce polished articles.

Your team:
- Research Agent: searches and returns structured research notes
- Writer Agent: writes an article draft from research notes
- Editor Agent: critiques a draft and returns specific improvements

When given a topic and angle:
1. Send the topic to the Research Agent. Wait for structured notes.
2. Review the notes. If they seem thin or miss the angle, ask the Research Agent for a second pass focused on [gap].
3. Send the notes to the Writer Agent with the original angle as context.
4. Send the draft to the Editor Agent.
5. If the Editor flags more than 2 structural issues, send the draft back to the Writer with the critique.
6. When the Editor gives a clean review (0–1 structural issues), return the final draft.

Always explain which step you are on and why.
```

### Step 5: Connect and Test

In Make or n8n:

- Create a trigger (webhook or manual form).
- Connect it to the Research Agent (Claude API call with Research system prompt + web search tool).
- Pass the output to the Writer Agent (Claude API call with Writer system prompt).
- Pass the draft to the Editor Agent (Claude API call with Editor system prompt).
- Return the final output to Slack, Notion, or email.

Test with five different topics. Note where the pipeline breaks and tighten the prompt at that step.

## PART 5: THE FIVE PATTERNS THAT MAKE AGENT TEAMS RELIABLE

### Pattern 1: Enforce Structured Outputs

Every agent in your team should return output in a defined format - not free-form prose. This makes handoffs reliable. If the Research Agent can return its notes in any format it wants, the Writer Agent has to interpret them. That interpretation introduces inconsistency.

Use explicit output templates in every system prompt. Every agent in the team should know exactly what format it receives and exactly what format it must return.

### Pattern 2: Quality Gates Between Agents

Do not pass every output to the next agent automatically. Add a simple evaluation step - either an Orchestrator review or a dedicated Critic agent - that checks the output before it moves downstream.

A quality gate asks: does this output meet the minimum standard required for the next step to succeed? If not, it goes back with specific feedback. This is what prevents a single weak agent from degrading the entire pipeline.

### Pattern 3: Give Agents Minimal Tools

An agent with 15 tools available will use them inconsistently. An agent with 2–3 tools will use them reliably. Match tools to the exact job the agent does. The Research Agent gets search and fetch. The Writer Agent gets nothing - it needs no external information, just its context.

The Publisher Agent gets the platform API.

### Pattern 4: Build in a Retry Loop

Every production agent team needs a retry mechanism. When an agent's output fails the quality gate, it should get a second chance with specific feedback - not just run again. The feedback is the important part. "Your research notes are missing statistics - find at least two data points with sources and revise" produces a better second attempt than running the same prompt again.

Limit retries to 2–3 attempts per task. If an agent fails three times on the same task, escalate to a human or log it for review.

### Pattern 5: Log Everything

In production, every agent call should log: the input it received, the output it produced, the tools it called, and the time it took. This is what makes debugging possible. When the pipeline produces a bad output, logs tell you which agent introduced the error - and exactly what that agent received as input.

## PART 6: REAL-WORLD TEAM EXAMPLES

### Team 1: Lead Generation and Outreach

Agents:

- Prospecting Agent - searches LinkedIn and company sites for target leads matching your ICP.
- Research Agent - finds specific recent news, posts, or context about each lead.
- Personalization Agent - writes a personalized first-line for each outreach message using the research.
- Sequencer Agent - builds the full 3-touch outreach sequence per lead.

Output: A CRM-ready list of leads with personalized multi-touch outreach sequences, ready to send.

### Team 2: Competitive Intelligence Monitor

Agents:

- Monitor Agent (runs on schedule) - checks competitor websites, product pages, pricing, and social channels for changes.
- Change Detection Agent - compares current state to last week's snapshot and flags what changed.
- Analysis Agent - interprets the significance of each change and suggests implications.
- Report Agent - compiles a weekly briefing and sends it to Slack or email.

Output: An automated weekly competitive intelligence briefing, no manual research needed.

### Team 3: Customer Support Triage System

Agents:

- Classifier Agent - reads each incoming support message and classifies by type (billing, technical, general, urgent) and sentiment.
- Knowledge Agent - searches the company's knowledge base for the most relevant answer.
- Draft Agent - writes a reply using the knowledge base answer and the original message tone.
- Routing Agent - sends the draft to the right human queue based on classification, or auto-sends if confidence is high.

Output: Every support message classified, answered, and routed automatically. Humans only review flagged or complex cases.

### Team 4: Newsletter Research and Writing Pipeline

Agents:

- Topic Scout Agent - finds the top 5 trending developments in a given niche from the past 7 days.
- Deep Research Agent - for each topic, finds sources, statistics, and expert opinions.
- Section Writer Agent - writes a 150-word newsletter section per topic.
- Editor Agent - reviews all sections for consistency, tone, and quality.
- Assembly Agent - combines sections into a complete newsletter draft with intro and outro.

Output: A complete weekly newsletter draft, research included, ready to review and send.

## PART 7: THE MISTAKES THAT KILL AGENT TEAMS

### Mistake 1: Building One Giant Agent Instead of a Team

If your system prompt is more than 500 words and gives the agent six different jobs to do, you have built a confused agent pretending to be a team. Break it up. Each distinct task gets its own agent.

### Mistake 2: No Defined Output Format

Without a structured output format, every agent returns something slightly different. The next agent cannot reliably parse it. Add an explicit output template to every system prompt and enforce it.

### Mistake 3: Skipping the Critic

Most people build Research → Write → Publish and skip the review step entirely.

The Critic agent is what separates work that is good enough to publish from work that embarrasses you. Build it into every pipeline.

### Mistake 4: Giving Agents Memory They Cannot Handle

Agent context windows are finite.

An agent trying to hold a full research database, the conversation history, its instructions, and its current task in one context window will degrade. Use a structured handoff - pass only what the next agent needs, not everything the previous agent produced.

### Mistake 5: No Human Oversight Before Production

Run every new agent team in a monitoring mode first — where a human reviews every output before it takes any external action (sends an email, posts to social, makes an API call). Move to automated only after the pipeline has produced 20+ consecutive outputs you would have been happy to send manually.

## QUICK START: YOUR FIRST AGENT TEAM IN 48 HOURS

- **Hour 1:** Pick one workflow in your business that takes three or more steps, each of which could be done by a different person.
- **Hour 2:** Write a system prompt for each step as if you were briefing a new hire: here is your one job, here is what you receive, here is exactly what you must return.
- **Hour 3:** Build the pipeline in Make or n8n. Connect the agents sequentially.
- **Hour 4–6:** Run five test cases. Find where the pipeline breaks. Tighten the weakest prompt.
- **Day 2:** Add a Critic agent after the most important step. Run five more tests. Compare output quality.
- **Day 2 evening:** Put it in front of a real task. Review the output. Iterate.

One agent runs a task. A team of agents runs a business.

The principles are simple: one job per agent, structured handoffs, quality gates between steps, and a Critic that keeps the whole system honest.

Build those four things into any workflow and you have a team that actually works.
