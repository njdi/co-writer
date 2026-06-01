# Software Fundamentals Matter More Than Ever

**Author:** Tech With Tim ([@TechWithTimm](https://x.com/TechWithTimm))  
**Published:** May 25, 2026  
**Source:** [Software Fundamentals Matter More Than Ever](https://x.com/TechWithTimm/status/2058931260966465667)

There is an idea that you can write a spec, have AI turn it into code, and then mostly keep working at the spec level. If something breaks, you update the spec and let AI generate more code.

That sounds nice.

But when you actually do it, the code often gets worse each time.

You get more code, but not necessarily better code. And if you keep changing the system without understanding the design, the codebase becomes harder to understand, harder to change, and easier to break.

That is why fundamentals matter more now, not less.

And these 5 things especially matter when you are writing code with AI.

## 1. Reach a shared understanding first

One failure mode with AI coding is that the AI simply does not build what you meant.

You had a clear idea in your head, but the AI produced something else. It may have followed the prompt in some technical sense, but it did not match the thing you were trying to build.

That is a requirements problem.

You and the AI have not reached the same design concept yet.

In other words, you do not share the same understanding of what the system should do, how the parts should fit together, and which tradeoffs matter.

So instead of asking AI to build right away, make it ask questions first. Let it push back, clarify the idea, ask about edge cases, and help you figure out what you actually want.

That matters because no one knows exactly what they want at the beginning.

Not you.

Not the AI.

The shared understanding has to come before the code.

## 2. Create a shared language

Another failure mode is that AI starts talking around the problem because you and AI are not using the same language.

Developers already know this from working with product teams or domain experts. The business uses one term, the code uses another, and you end up translating between both sides.

If that translation is messy, the software gets messy too.

The same thing happens with AI.

The terms in your plan, code, modules, tests, and prompts should line up. If the project has specific domain language, the AI should know that language too.

Because if those terms are not defined, the AI will guess.

And when it guesses, it can create the wrong abstraction, use the wrong naming, or connect the wrong ideas together.

So create a simple Markdown file that defines the project's language. List the important domain terms, explain what each one means, and show how each term should be used in the codebase. Then give that file to the AI whenever it plans, reviews, or writes code.

This makes the planning clearer and the implementation more aligned with what you actually meant.

## 3. Use feedback loops

Even when AI builds the right thing, it may not work.

That is where feedback loops matter.

Types, tests, browser access, and automated checks give AI a way to see when the code is wrong. Without those loops, it can generate a large amount of code before realizing anything is broken.

But feedback only helps if the AI gets it fast enough.

The problem is that AI often tries to do too much at once. It writes a big chunk of code, then checks it later.

That is backwards.

The rate of feedback is your speed limit.

If feedback is slow, make the work smaller and have AI verify each meaningful change as it goes.

That is why test-driven development fits so well with AI coding: write a test, make it pass, then refactor and improve the design.

That keeps AI from sprinting ahead and leaving you with a pile of code to untangle.

## 4. Make the codebase easy to test

Feedback loops only work well when the codebase is actually testable.

And testable code comes from clear boundaries.

That is why deep modules matter.

A deep module hides a meaningful amount of functionality behind a simple interface. You can test behavior at the boundary without understanding every tiny internal detail.

A shallow module does the opposite. It spreads complexity across too many small pieces, which makes the code harder for both you and the AI to understand later.

AI can create shallow, scattered code very easily.

It may look modular because there are lots of small files, but in practice, it becomes harder to review, harder to test, and harder to change.

That gives AI more context to guess, and gives you more code to review and maintain.

## 5. Design the interface, then delegate the implementation

AI is useful when you give it the right boundary.

As AI helps you produce more code faster, the harder part becomes reviewing, testing, maintaining, and fitting that code into the system.

You cannot review every tiny implementation detail forever, especially in lower-risk parts of the system.

The split is simple.

You design the interface, understand the module, and define what the code should do from the outside. Then AI can help implement what happens inside that boundary.

For some parts of an application, you do not need to inspect every tiny implementation detail if the outside boundary is clear, the purpose is clear, and the behavior is testable.

But this only works if you are still thinking about the system. You still need to know which modules are changing, which interfaces matter, and which parts are too critical to delegate casually.

AI can help with implementation, but the system design still belongs to you.

## Final thought

The real shift is not that AI makes coding disappear.

It moves the hard part.

Now generating code is easier, but understanding whether that code belongs in the system matters more than ever.

That means you need to know what should exist, what should not exist, where the boundary is, what behavior matters, and when the AI is making the system worse even if the code looks correct.

That is the part you cannot delegate blindly.

AI can help you write the code, but you still need to understand the system you are building.
