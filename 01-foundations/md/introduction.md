# Introduction to CrewAI

> Venkata Bhattaram (c) 2026

## Introduction

CrewAI is a framework for building applications where AI agents can work independently or collaborate with other agents to accomplish a goal.

Instead of treating an AI application as a single prompt sent to a language model, CrewAI allows us to organize an application around concepts such as:

- **Agents** — AI workers with specific roles and responsibilities.
- **Tasks** — pieces of work assigned to agents.
- **Tools** — capabilities that allow agents to interact with external systems and information.
- **Crews** — groups of agents working together to accomplish a goal.
- **Processes** — define how tasks within a Crew are executed.
- **Flows** — provide event-driven application orchestration, state management, routing, and control around CrewAI workflows.

A simplified CrewAI application can be understood as:

```text
                  CrewAI Application
                         │
             ┌───────────┴───────────┐
             │                       │
           Crew                    Flow
             │                       │
       ┌─────┴─────┐          State / Routing
       │           │                │
    Agent        Agent             Crew
       │           │                │
     Task        Task            Agents
       │           │                │
     Tools       Tools           Tasks
```

The goal of this Masterclass is to move from these fundamental concepts to complete production-oriented AI applications.

---

## Questions This Introduction Answers

Before beginning the hands-on lessons, you should be able to answer:

### 1. What is CrewAI?

CrewAI is a framework for orchestrating AI agents and building multi-agent applications.

### 2. Why do we need multiple AI agents?

A complex problem can be divided among specialized agents.

For example:

```text
Research Agent
      ↓
Analysis Agent
      ↓
Writing Agent
      ↓
Review Agent
```

Each agent can have a different responsibility instead of asking one agent to perform the entire workflow.

### 3. What is an Agent?

An Agent represents an AI worker that has a defined role, goal, and behavior.

For example:

```text
Role: Research Analyst
Goal: Find and analyze information
Tools: Web search
```

### 4. What is a Task?

A Task describes the work that an agent needs to perform.

```text
Agent
  ↓
Task
  ↓
Result
```

### 5. What is a Crew?

A Crew combines agents and tasks into a collaborative workflow.

```text
Crew
 ├── Researcher
 ├── Analyst
 └── Writer
```

### 6. What is a Flow?

A Flow provides application-level orchestration.

It can control:

- execution order
- application state
- conditional routing
- branching
- multiple Crews
- persistence
- event-driven execution

A useful mental model is:

```text
Flow = controls the application

Crew = coordinates the agents

Agent = performs the work
```

### 7. Crew vs Flow — what is the difference?

A Crew focuses primarily on **agent collaboration**.

A Flow focuses primarily on **application orchestration and control**.

They are not competing concepts. They can be combined:

```text
Flow
 │
 ├── Crew A
 │    ├── Agent
 │    └── Agent
 │
 ├── Validation
 │
 └── Crew B
      ├── Agent
      └── Agent
```

This Flow + Crew architecture will become an important part of the later Masterclass lessons.

### 8. What will I learn in this Masterclass?

The tutorial progresses from:

```text
Installation
    ↓
Agents
    ↓
Tasks
    ↓
Tools
    ↓
Crews
    ↓
Processes
    ↓
Flows
    ↓
Flow + Crew Architecture
    ↓
LLM Integration
    ↓
Memory
    ↓
Knowledge & RAG
    ↓
Outputs & Guardrails
    ↓
Human-in-the-Loop
    ↓
Testing & Observability
    ↓
Production
    ↓
Real-World Projects
```

---

## How to Use This Tutorial

This repository is designed to be followed **sequentially**.

Each lesson introduces a concept and then builds on concepts learned earlier.

For every topic, follow this sequence:

```text
Read the concept
      ↓
Understand the architecture
      ↓
Study the example
      ↓
Run the example
      ↓
Modify the code
      ↓
Complete the exercise
      ↓
Compare with the solution
      ↓
Move to the next lesson
```

### 1. Read Before Running

First understand what the example is demonstrating.

Do not immediately copy and execute the code.

Ask:

> What problem is this example solving?

and:

> Which CrewAI concept is being demonstrated?

### 2. Run the Example

Every major lesson should contain runnable code.

After understanding the example, execute it locally and observe the output.

### 3. Experiment

Change the example.

For example:

- change the agent's role
- change the goal
- modify the task
- add a tool
- introduce another agent
- change the process
- modify the Flow state

The purpose of the Masterclass is not only to make the examples work, but to understand how changing the architecture changes the behavior.

### 4. Complete the Exercises

Where an exercise is provided, try solving it before looking at the solution.

The exercises should gradually increase in difficulty.

### 5. Build the Final Project

The later lessons combine the concepts learned throughout the Masterclass into complete CrewAI applications.

---

## Prerequisites

Before starting the hands-on lessons, you should have:

- Basic Python knowledge
- Familiarity with functions and classes
- Basic understanding of APIs
- Basic understanding of JSON
- Basic understanding of environment variables
- A supported Python version
- Basic familiarity with the command line

You do **not** need previous CrewAI experience.

The Masterclass starts from the fundamentals.

---

## Code Example

The first example should intentionally be simple.

The objective is only to verify the basic CrewAI concepts:

```text
Agent
   ↓
Task
   ↓
Crew
   ↓
Execution
```

### Example: First CrewAI Agent(example.py)

```python
from crewai import Agent, Crew, Task


researcher = Agent(
    role="AI Researcher",
    goal="Explain what CrewAI is in simple terms",
    backstory=(
        "You are an AI researcher who specializes in "
        "explaining artificial intelligence concepts clearly."
    ),
    verbose=True,
)

explain_crewai = Task(
    description=(
        "Explain CrewAI to a beginner in approximately "
        "three short paragraphs. Explain what it is, "
        "why it is useful, and what an Agent, Task, and Crew are."
    ),
    expected_output=(
        "A clear beginner-friendly explanation of CrewAI "
        "covering Agents, Tasks, and Crews."
    ),
    agent=researcher,
)

crew = Crew(
    agents=[researcher],
    tasks=[explain_crewai],
    verbose=True,
)

result = crew.kickoff()

print("\n=== CrewAI Result ===\n")
print(result)
```

### What happens in this example?

The execution can be understood as:

```text
Create Agent
     ↓
Create Task
     ↓
Assign Task to Agent
     ↓
Create Crew
     ↓
Kickoff Crew
     ↓
Agent processes Task
     ↓
Crew returns result
```

This is intentionally a small example.

We will **not** introduce tools, memory, RAG, Flow routing, multiple agents, or production infrastructure yet.

Those concepts will be introduced progressively in later lessons.

---

## What You Should Understand After This Lesson

By the end of this introduction, you should be able to explain:

```text
CrewAI
 │
 ├── Agent
 │
 ├── Task
 │
 ├── Tool
 │
 ├── Crew
 │
 ├── Process
 │
 └── Flow
```

You should also understand the difference between:

```text
Agent
= performs work

Task
= describes work

Crew
= coordinates agents and tasks

Flow
= orchestrates the application
```

---

## Conclusion

CrewAI provides a structured way to build AI applications around agents, tasks, tools, crews, and flows.

The most important idea to remember from this introduction is:

> **CrewAI is not simply about creating multiple AI agents. It is about designing reliable AI workflows in which agents can perform specialized work and applications can control how that work is executed.**

Throughout this Masterclass, we will start with the smallest possible CrewAI building blocks and progressively combine them into increasingly sophisticated systems.

The learning progression is:

```text
Agent
  ↓
Task
  ↓
Crew
  ↓
Tools
  ↓
Processes
  ↓
Flow
  ↓
Flow + Crew
  ↓
Production AI Application
```

Once you understand this progression, you are ready to begin with the first hands-on lesson: **setting up the CrewAI development environment**.