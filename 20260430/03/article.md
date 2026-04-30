# The Complete Guide to Building Skills for Claude

**Author:** Clara Bennett ([@CodeswithClara](https://x.com/CodeswithClara))  
**Published:** April 29, 2026  
**Source:** [The Complete Guide to Building Skills for Claude](https://x.com/Zephyr_hg/status/2049479378112041101)

i have spent the last few weeks going deep on Claude Skills and i think most people are still sleeping on what this actually unlocks

if you dont know what a Skill is yet, here is the fastest way to understand it

a Skill is just a folder. inside that folder is a markdown file called SKILL.md, and optionally some scripts, templates, or reference docs. when Claude sees a task that matches the description in your SKILL.md, it loads the folder and follows the instructions inside

thats it. no fine tuning, no vector database, no infra. just a folder of instructions that Claude knows when to reach for

the reason this is a big deal is because it solves the problem nobody talks about with LLMs. the model is smart but it doesnt know your workflow. it doesnt know your brand voice, your file naming convention, your reporting format, the weird quirks of your stack. you end up reprompting the same context every single time

Skills fix that. you write the context once, and Claude pulls it in automatically when its relevant

## how to think about when to build one

dont sit down and try to invent a skill from scratch. that path leads to overengineered folders you never use

wait until you catch yourself prompting Claude the same way three times in a row. thats your signal. the repetition is the brief

i keep a notes file open while i work and any time i find myself pasting the same context, the same instructions, or the same examples into a chat, i write it down. at the end of the week i look at the list and the skills basically write themselves

## the anatomy of a SKILL.md

every SKILL.md has two parts that matter most. the description at the top, and the instructions in the body

the description is the single most important line in the whole file. this is what Claude reads to decide if your skill is relevant to the current task. if its vague, your skill will sit there and never get triggered. if its sharp and specific, it activates exactly when it should

bad description: "helps with writing"

good description: "use this when the user asks to write a cold outreach email to a founder, vc, or operator. covers tone, structure, and follow up sequence"

notice the difference. the second one tells Claude exactly when to reach for it and exactly when not to. specificity is what makes skills work

the body is where you put the actual playbook. think of it as a sop you would hand a smart new hire on day one. include the steps, the format, the examples, the things to avoid, and the edge cases. dont assume Claude knows your preferences. spell them out

## the structure i use for almost every skill

i open with a one line purpose statement so Claude knows the goal

then i list the inputs i usually provide so Claude knows what to expect from me

then i write the actual process as numbered steps. this is where most of the value lives. be opinionated. say "do this, not that"

then i drop in two or three examples of the input and the ideal output. this is the most underrated part of skill writing. examples teach Claude faster than any rule you can write. one good before and after pair is worth ten paragraphs of instructions

then i add a section called "common mistakes to avoid" where i list the stuff Claude tends to get wrong on this task. this single section has saved me more reprompts than anything else

## keep skills small and focused

this is the rule i broke the most when i started

one skill, one job. if you try to build a "do everything marketing" skill, the description gets so broad that Claude never knows when to use it. split it up. have a skill for cold emails, another for linkedin posts, another for landing page copy

small skills compose. big skills collapse

## use reference files

this is where skills get really powerful

you can drop any file into the skill folder. a brand guide pdf, a style sheet, a list of approved phrases, a template, a json schema, whatever. then reference it from the SKILL.md and Claude will pull it in when needed

this is how you get truly personalized output. instead of pasting your brand guide into every chat, you put it in the skill folder once and forget about it. Claude opens it when relevant and your output starts sounding like you wrote it

## let Claude help you build the skill

this is the meta move that saves the most time

open a chat, tell Claude what task you keep doing, paste in two or three examples of how you have done it before, and ask it to draft a SKILL.md for you. then edit

you will get to a working skill in 15 minutes instead of two hours. and the description Claude writes is usually sharper than what you would write yourself because it has read thousands of these

## skills can call other skills

once you have a few skills built, the real magic shows up

you can have a research skill that gathers information, a writing skill that turns research into a draft, and a formatting skill that outputs the final file. Claude orchestrates the chain on its own. you just give the original task and the skills hand off to each other

i did not believe this until i watched it happen. it feels like having a small team

## the meta point

the people winning with skills right now are not the ones with the fanciest folders. they are the ones who paid attention to their own repetition

every time you reprompt the same thing, you are leaking time. a skill is just the act of plugging that leak once and never thinking about it again

the loop is simple. notice the repetition. write the SKILL.md. test it on a real task. edit it when it gets something wrong. move on

do this five times and you have a personal version of Claude that knows how you work. do this twenty times and your output quality compounds in a way that is honestly hard to explain until you feel it

the next time you catch yourself typing the same prompt for the third time, stop. open a folder. write a SKILL.md. you just gave yourself a permanent upgrade
