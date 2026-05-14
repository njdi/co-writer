# How to Set Up Claude Code Routines to Automate Any Workflow (Full Course)

**Author:** Khairallah AL-Awady ([@eng_khairallah1](https://x.com/eng_khairallah1))  
**Published:** May 13, 2026  
**Source:** [How to Set Up Claude Code Routines to Automate Any Workflow (Full Course)](https://x.com/Zephyr_hg/status/2054494450009932110)

There is a feature that Anthropic released, and almost nobody is talking about it.

Bookmark & Save this :)

It is called Claude Code Routines.

And it might be the most important feature Anthropic has shipped this year.

Here is why.

Until now, every Claude Code automation required your laptop to be open. You could use /loop to poll for changes. You could use /schedule to set up recurring tasks. But the moment you closed your terminal or shut your laptop, everything stopped.

Routines fix that completely.

A routine is a Claude Code automation you configure once — a prompt, a repo, a set of connectors — and then it runs on Anthropic's cloud infrastructure. On a schedule. From an API call. Or triggered by a GitHub event.

Your laptop can be off. Your terminal can be closed. The routine runs anyway.

This is the shift from "AI tool you use" to "AI system that works for you."

Here is exactly how to set one up, even if you have never used Claude Code before.

## Why Routines Are Different From Everything Else

Claude Code already had scheduling. So what changed?

The difference is infrastructure.

The old /schedule and /loop commands ran inside your local Claude Code session. They depended on your machine being on, your terminal being open, and your internet connection staying stable. If any of those failed, the automation died.

Routines run on Anthropic's cloud. They are persistent autonomous agents that survive restarts, terminal closures, and overnight runs. They have direct access to your repos and your connectors — Slack, Linear, Google Drive, GitHub — without you needing to manage any of it.

Think of the old system as a reminder on your phone. It dings, but you still have to do the work.

Routines are the employee who does the work while you are asleep and sends you a summary when you wake up.

## Step 1: Decide What to Automate

The best routines automate tasks that are:

**Recurring** — they happen on a predictable schedule (daily, weekly, or triggered by an event).

**Well-defined** — you can describe exactly what "done" looks like without ambiguity.

**Low-judgment** — the task does not require your unique creative thinking or decision-making. It requires execution.

Here are the patterns that early users are running right now:

**Backlog management** — every night at midnight, the routine pulls new issues from Linear, categorizes them by type and severity, assigns labels, and posts a summary to a Slack channel. The engineering lead wakes up to a clean, organized board.

**Documentation drift detection** — every Friday, the routine scans merged pull requests from the past week, identifies any that changed APIs or interfaces, cross-references them against the documentation, and opens update PRs for docs that are now out of date.

**Deploy verification** — triggered by a webhook after every deployment, the routine runs smoke tests against the new build, scans error logs for regressions, correlates any issues with recent code changes, and posts a go/no-go verdict to the release channel.

**Daily code review** — every morning at 9am, the routine picks up the oldest open PR, reviews it for security issues, logic errors, and style violations, and posts inline comments.

The people who set up three or four of these are operating at a completely different level than people who are still using Claude as a chat tool.

## Step 2: Create Your First Routine

There are two ways to create a routine.

**From the web interface:** Go to claude.ai/code/routines and click "New routine." This gives you the full configuration options — schedule triggers, API triggers, and GitHub event triggers.

**From the CLI:** If you already use Claude Code in the terminal, type /schedule followed by a description. For example:

```
/schedule daily PR review at 9am
```

The CLI creates schedule-based triggers only. For API and GitHub triggers, you need the web interface.

When you create a routine, you configure four things:

**The prompt** — this is the most critical part. Since the routine runs autonomously, the prompt needs to be completely self-contained. Everything the agent needs to know must be in the prompt. There is no "context from earlier in the conversation." Every run starts clean.

**The repository** — which codebase the routine works with. It gets full read access and can push to branches prefixed with claude/ by default.

**The connectors** — which external services the routine can access. Slack for posting updates. Linear for reading and managing issues. Google Drive for reading and writing documents. GitHub for monitoring events and opening PRs.

**The trigger** — when and how the routine runs. Scheduled (hourly, nightly, weekly), API-triggered (you call it programmatically), or GitHub-triggered (it fires when a specific event happens in your repo).

## Step 3: Write a Bulletproof Prompt

This is where most people fail.

A routine runs without you watching. If the prompt is vague, the agent will interpret it differently every time and you will get inconsistent results.

The best routine prompts follow this structure:

**Role definition:** "You are a senior code reviewer specializing in security and performance."

**Task definition:** "Review the oldest open pull request in this repository."

**Step-by-step process:** "First, read the PR description. Then check out the branch. Read the changed files. Analyze for security vulnerabilities, logic errors, and performance issues. Write inline comments for each issue found."

**Output specification:** "Post a summary comment on the PR with: total issues found (by severity), a one-paragraph overall assessment, and a clear approve/request-changes verdict."

**Error handling:** "If there are no open PRs, post to #engineering in Slack saying 'No open PRs to review today.' If a PR has more than 50 changed files, skip it and post that it needs manual review."

**Constraints:** "Never approve a PR that has a Critical severity issue. Never modify any code directly — only comment. Maximum three inline comments per file to avoid noise."

The more precise your prompt, the more reliable your routine becomes.

## Step 4: Understand the Limits

Routines are powerful but they have constraints you need to know about.

**Daily run cap:** During the research preview, each account gets 15 routine runs per day. If you need more, enable extra usage in your organization settings — additional runs are metered.

**Token consumption:** Routines draw from the same subscription limit as interactive Claude Code sessions. A complex routine that reads many files and makes multiple API calls will use significantly more tokens than a simple one.

**Branch security:** By default, Claude can only push to branches prefixed with claude/. This is a safety measure — a poorly written routine cannot accidentally push to main. Do not disable this unless you have robust review processes downstream.

**GitHub event caps:** GitHub-triggered routines have per-routine and per-account hourly caps during the preview. If your repo is very active, filter which events trigger the routine to avoid wasting runs on noise.

**Schedule dependency:** Scheduled routines run at the specified time, but there can be variance during high-demand periods. Do not build workflows that depend on exact-second timing.

## Step 5: Build a Routine Stack

One routine is useful. A stack of routines is a system.

Here is what a complete routine stack looks like for a small engineering team:

**Morning (9am) — Daily PR Review**  
Claude reviews all open PRs, posts inline comments, and sends a summary to Slack with a prioritized list of what needs attention today.

**Post-deploy (webhook) — Deploy Verification**  
Every time a deploy hits staging, Claude runs the test suite, scans logs for errors, and posts a go/no-go to the release channel within minutes.

**Nightly (2am) — Backlog Triage**  
Claude processes all new issues filed that day, adds labels, assigns priority scores, and creates a morning briefing document.

**Weekly (Friday 5pm) — Documentation Check**  
Claude scans the week's merged PRs, identifies docs that need updating, and opens draft PRs for each one.

**Weekly (Monday 8am) — Tech Debt Report**  
Claude scans the codebase for TODO comments, deprecated dependencies, and test coverage gaps. Produces a ranked list of tech debt items with estimated effort.

Each routine takes 10-15 minutes to set up. The stack takes an afternoon. The time savings compound every single week.

## Step 6: Monitor and Improve

Every routine run generates a log. Review it.

Look for patterns:

- Is the routine consistently producing good output? If not, which part of the prompt is ambiguous?
- Is it taking too long on certain runs? You might need to narrow the scope.
- Is it encountering errors? Add explicit error handling to the prompt.
- Is it producing too much noise? Tighten the constraints.

The new "Dreaming" feature — announced at Code with Claude on May 6th — takes this even further. When Dreaming is enabled, Claude reviews its own past routine sessions between runs, identifies patterns in what worked and what did not, and self-improves its approach for next time.

Your routines literally get smarter the more they run.

## Who This Is For (And Who It Is Not For)

Routines are built for developers and technically-inclined operators who:

- Already use Claude Code or are willing to learn
- Have repeatable tasks in their workflow that follow clear patterns
- Want to automate the operational overhead that eats hours every week
- Work with codebases hosted on GitHub

If you are a non-technical user looking for AI automation, Claude Cowork with scheduled tasks is a better starting point. Routines are the power user tool.

But if you are a developer, an engineering manager, a DevOps engineer, or a technical founder — routines will save you more time than any other feature Anthropic has shipped.

## Routines vs. GitHub Actions: What Is the Difference

Many developers will ask: why pay for Claude routines when GitHub Actions is free?

The answer is that a GitHub Action is a script. You write every step. You define every conditional. You handle every edge case yourself. It does exactly what you coded and nothing more.

A Claude routine is an agent. You give it a goal. It decides how to reach it. It adapts to unexpected situations. It reasons about problems. It verifies its own work.

A GitHub Action runs a linter and tells you what failed. A Claude routine reads the error, understands why it failed, proposes a fix, and opens a pull request with the correction.

That is a fundamentally different category. Scripts follow rules. Agents solve problems.

For simple automation — run tests, check formatting, post a notification — GitHub Actions is fine. For anything that requires judgment, analysis, or adaptation, routines are in a different league.

## Common Routine Recipes You Can Copy Today

Here are five routine configurations you can set up in the next hour:

**Recipe 1: The Morning Standup Bot**  
Schedule: Daily at 8:30am  
Prompt: "Check the GitHub repository for all commits pushed yesterday. Check Linear for new and updated issues. Check Slack #engineering for any messages mentioning blockers. Compile a standup briefing with three sections: what was done, what is in progress, and what is blocked. Post the briefing to #daily-standup in Slack."

**Recipe 2: The Dependency Auditor**  
Schedule: Weekly on Monday at 6am  
Prompt: "Scan package.json and requirements.txt for all dependencies. Check each dependency for known vulnerabilities using the web. Identify any dependencies that are more than two major versions behind current. Create a prioritized report with severity ratings and open a GitHub issue if any Critical vulnerabilities are found."

**Recipe 3: The Changelog Generator**  
Trigger: GitHub event — new release tag pushed  
Prompt: "When a new release tag is pushed, read all commits since the previous tag. Categorize each commit as feature, fix, improvement, or chore. Generate a formatted changelog in CHANGELOG.md and open a PR."

**Recipe 4: The Test Coverage Monitor**  
Schedule: Nightly at 1am  
Prompt: "Run the test suite. Calculate coverage percentages by module. Compare against the coverage baselines in coverage-config.json. If any module drops below its baseline by more than 2%, open a GitHub issue with the specific module, old coverage, new coverage, and the commits that likely caused the drop."

**Recipe 5: The PR Description Enforcer**  
Trigger: GitHub event — new PR opened  
Prompt: "When a new PR is opened, check if the description meets our template requirements: must include a Summary section, a Testing section, and a Screenshots section if UI changes are involved. If any section is missing, post a polite comment requesting the author update the description before review."

Each recipe takes less than 10 minutes to configure. Together they save a team dozens of hours per month.

## The Bottom Line

The old way: wake up, open terminal, start Claude Code session, type commands, wait for results, move on to next task. Repeat tomorrow.

The new way: configure routines once, let them run on Anthropic's cloud, wake up to results.

This is not a theoretical improvement. People are already running stacks of routines that handle their entire operational workflow overnight.

The gap between "person who uses Claude as a chatbot" and "person who has Claude working autonomously around the clock" is getting bigger every week.

Routines are how you cross to the other side.

Most people will read this and think "I should set that up sometime." The ones who actually create their first routine today will have a system running by next week that saves them hours every month.

Follow me [@eng_khairallah1](https://x.com/eng_khairallah1) for more AI breakdowns and workflows. I post content like this regularly - tools, setups, and strategies that actually work.

hope this was useful for you, Khairallah ❤️
