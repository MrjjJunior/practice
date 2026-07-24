 ## Day 1 – Foundations (6–8 hours)

Focus on understanding the concepts.

Topics:

- [x]  What orchestration is
- [x]  System prompts
- [x]  Prompt engineering
- [x]  Role prompting
- [x]  Few-shot prompting
- [x]  Structured output
- [x]  JSON
- [x]  JSON Schema

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

### Making a good prompt.

1. Role
2. Task
3. Rules
4. Format
5. context

giving example of the desired behavior will help

prompt engineering is controlling ai behavior 

### Prompt Injection Protection

Strong system prompt


Use clear delimiters:

The model can more clearly distinguish between **your instructions** and **the user's content**.

**Validate intent** only accept the known ones.  

### Tokens

- Prompts have token limits.
- Long prompts cost more.
- Long prompts take longer to process.