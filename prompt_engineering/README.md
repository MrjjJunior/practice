 ## Day 1 – Foundations (6–8 hours)

Focus on understanding the concepts.

Topics:

- [x]  What orchestration is
- [ ]  System prompts
- [ ]  Prompt engineering
- [ ]  Role prompting
- [ ]  Few-shot prompting
- [ ]  Structured output
- [ ]  JSON
- [ ]  JSON Schema

- What is orchestration?
- What is prompt engineering?
- What is a system prompt?
- Why do we use structured output?
- What is JSON?
- Why is JSON better than plain English for applications?

Practice:

- Write prompts that always return JSON.
- Validate whether the JSON follows your expected structure.

Goal:

> Explain what prompt engineering is and why structured output matters.
> 

### what is orchestration ?

Process of coordinating (controlling) what happens when the user sends the message to the backend completing the request. 

**AI Orchestrator** 

> Note: Search on Token usage. And what is the cheapest way for this implementation.
> 

Always **determine** the user intent

user request → determine intent → Orchestrate (determine function call) → prompt AI → get response → validate response → 

user request → determine intent, orchestrate(function that determines the user intent) → valid the intent response → orchestrate (update function call / service)→ validate response → backend receives update status → respond to user. 

> The AI will return a json response, in the response it will tell us what function call we must make.
> 

> AI performs task for the current step.
> 

> Secure against prompt injections
> 

## Prompts

User and System prompt

### 

### What is prompt Engineering?

Designing clear, structured instruction that guide the AI model to produce the desired output reliably.