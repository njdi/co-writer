# Why We Should Stop Designing Harnesses for AI Agents

**Author:** Kangwook Lee ([@Kangwook_Lee](https://x.com/Kangwook_Lee))  
**Published:** May 9, 2026  
**Source:** [Why We Should Stop Designing Harnesses for AI Agents](https://x.com/Zephyr_hg/status/2052925157606568217)

*(For those who aren't familiar with "the horse-carriage analogy", please read my recent article first)*

In this article, I want to explain why we all should stop hand-designing harnesses for AI agents.

**tldr:** The best harness for an AI agent may no longer be the one humans design for it, but the one the agent engineers for itself. If we keep designing harnesses for AI agents, we will become the bottleneck.

## A Harness Creates a Threshold

Let me start with laying out a new way of thinking about the relationship between a harness and a model.

The view most people use today is "fix the model, change the harness."

The view I want to propose is "fix the harness, and vary model capacity."

Then, for a fixed task, the harness creates a single threshold on the model's raw intelligence.

If the model is smarter than the threshold, it solves the task with this harness. If the model is below the threshold, it cannot.

Let's call this threshold θ(h), defined with respect to harness h.

![](images/img-01.jpg)

## The Three Regimes Framework

This view becomes very useful when it comes to comparing two harnesses.

One is a good harness (h_good). One is a bad harness (h_bad).

The good harness makes the task easier, so it creates a lower threshold. The bad harness demands a smarter model for the same task, so it creates a higher threshold.

This naturally gives rise to three regimes.

![](images/img-02.jpg)

**First regime.** Models in this regime cannot solve the task with either harness.

**Second regime.** Models in this regime are moderately smart, and they can solve the task but only with a good harness!

**Third regime.** Models in this regime are smart enough, and they can solve the task regardless of the harness.

Note that harness quality matters in the middle regime when models are moderately smart but not very smart. That's when a good harness makes a difference.

Let's call this The Three Regimes Framework.

## Human-Made Harness vs AI-Made Harness

Let's return to the horse-carriage analogy.

There is one crucial difference between a horse and an AI.

A horse could not build its own harness. AI can.

Now, consider the two kinds of harnesses.

- **h_human:** harnesses made by humans.
- **h_ai:** harnesses made by AI.

For the past several years, the situation was this:

```
h_good = h_human
h_bad  = h_ai
```

Human-made harnesses were better than AI-made ones.

So in the Three Regimes Framework, the middle regime meant: "AI model works only with human-made harness."

The agent loops, tool-use patterns, memory structures, planning scaffolds that we carefully engineered by hand outperformed what AI produced on its own. Building a good agent meant building a good harness.

Personally, I spent a lot of time in this era designing harnesses for AI agents. I've designed the state-of-the-art chatbot harness [ACL'23], the VLM-based image clustering agent [ICLR'24], a gaming companion agent for PUBG, Ally, and Terminus-KIRA for coding agents.

It was very fun. For a while.

## But the Premise is Changing

AI is getting better at coding. Better at debugging. Faster at iterating on systems. And eventually, better at building harnesses than we are.

This flips the situation:

```
h_good = h_ai
h_bad  = h_human
```

What does this mean? As per the Three Regimes Framework, the middle regime now means: "AI model works only with AI-made harness."

In other words, if we keep using "human-made harness", we won't be able to see the full potential of the models whose capability lies in the middle regime.

In fact, our recent work, Meta Harness (led by @yoonholeee), already showed that AI outperforms humans at iterative harness engineering for mid-sized models.

To see the full picture, let me add a time axis. Assume AI coding ability increases monotonically over time. You get the following 2D phase diagram and see we are at the cusp of an important phase transition.

![](images/img-03.jpg)

The emergence of the "yellow regime" gives another possible explanation for the mismanaged geniuses hypothesis. If we keep using hand-designed harnesses, we won't see the full potential of the underlying AI models.

## Conclusions

When a model is overwhelmingly strong, harness quality barely matters. A simple agent loop and the right tools are enough to handle almost anything.

When a model is too weak, harness quality also barely matters. No harness can save it.

The problem is the middle. When a model is modestly smart. Capable in principle, but failing without proper support. That is where harness quality is decisive.

And until recently, that good harness had to come from a human.

Not anymore. To fully leverage models in the middle regime, we need to step back from harness engineering.

Let the smart horses build their own harness.
