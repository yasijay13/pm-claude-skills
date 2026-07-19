# PM Claude Skills

Skill files I use daily to run my product work with Claude. A skill is a markdown file with a trigger description and a set of rules; Claude reads it before doing the matching type of task. Instead of re-explaining my standards in every chat, the standards live in files and get applied automatically.

I'm a Senior Product Manager at a B2B SaaS company. This skill exists because I kept correcting the same thing: AI-sounding prose in my documents. That problem turned out to be fixable with written doctrine rather than repeated feedback.

## What's here

| Skill | What it does |
|---|---|
| [`anti-ai-writing`](skills/anti-ai-writing/SKILL.md) | My writing guide. Applies to everything I produce: Slack messages, PRDs, strategy docs, emails. Bans buzzwords and filler, forces the point into the first sentences, and includes rewrite patterns from vague to specific. |

Plus [`scripts/check_skill.py`](scripts/check_skill.py), a small validator I run before packaging a skill: checks the frontmatter, flags an over-long description, and zips the folder for upload.

## How I use these day to day

1. **Writing.** Every document, message, or post goes through `anti-ai-writing`. The skill encodes my actual failure patterns, not generic advice. When I catch a new AI-writing tell in my output, I add it to the guide, so the skill improves with use.
2. **Versioning.** Skills are markdown in a folder, so they version like code. When a rule changes, the diff shows exactly what changed and why.

The private version of this skill contains employer-specific detail. What's published here is the reusable methodology with all of that removed.

## Why this beats prompting from scratch

A prompt is a request. A skill is a standard. The difference shows up on the hundredth task: my hundredth Slack draft follows the same rules as my first, and when the rules were wrong I fixed them once, in one place. Most of the value of AI in my workflow has come from this loop, not from better one-off prompts.
