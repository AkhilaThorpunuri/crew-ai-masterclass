# Installation

> Venkata Bhattaram (c) 2026

## Contents

- Installing CrewAI
- Installing CrewAI Tools
- Creating a Python virtual environment
- Verifying the CrewAI installation
- Verifying the CrewAI CLI
- Choosing a supported Python version
- Creating the first CrewAI project
- Understanding the generated project structure

## Overview

This Masterclass uses one shared Python environment and dependency configuration for the entire tutorial rather than requiring each lesson to install packages independently.

Set up the environment once at the beginning, and the same environment can be used throughout the later chapters covering agents, tasks, tools, crews, processes, flows, memory, knowledge and RAG, testing, observability, and production.

The installation is organized by what each package unlocks:

- **Core Framework** — `crewai`. This provides the core CrewAI framework, including Agents, Tasks, Crews, Processes, Flows, and the CrewAI CLI.
- **Tools** — `crewai-tools`. This provides additional tool integrations that allow agents to interact with external information and services. It is installed separately from the core framework so that the core CrewAI installation remains focused.
- **Python Environment** — a project-specific `.venv` keeps CrewAI and its dependencies isolated from other Python projects on your machine.
- **Project Configuration** — `pyproject.toml` is used to define project metadata and dependencies for modern CrewAI projects.
- **LLM Providers** — CrewAI can work with different LLM providers. Provider configuration is introduced separately from framework installation so that installing CrewAI does not require a particular hosted LLM account.
- **Local Models** — a local Ollama installation can be used when you want to run supported models locally. This is optional and is covered separately in the LLM Integration chapter.

### Python Version

Use a Python version supported by the CrewAI version targeted by this Masterclass.

For the current course baseline, use:

```text
Python 3.10 – 3.13
```

Check your installed version with:

```bash
py --list
python --version
```

Using a supported Python version is important because CrewAI and its dependencies must all be compatible with the interpreter used by the project.

### What gets installed?

After completing this chapter, the development environment should look conceptually like:

```text
Python
  │
  └── .venv
       │
       ├── crewai
       │    ├── Agent
       │    ├── Task
       │    ├── Crew
       │    ├── Process
       │    └── Flow
       │
       └── crewai-tools
            └── Tool integrations
```

The later lessons build on this same environment.

## Code Example

### 1. Create a virtual environment

Create an isolated Python environment for the Masterclass.

### Windows / PowerShell

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Upgrade `pip`:

```powershell
python -m pip install --upgrade pip
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Upgrade `pip`:

```bash
python -m pip install --upgrade pip
```

---

### 2. Install CrewAI

Once the virtual environment is active:

```bash
pip install crewai
```

This installs the core CrewAI framework.

Verify it:

```bash
pip show crewai
```

---

### 3. Install CrewAI Tools

Install the additional CrewAI tool integrations:

```bash
pip install crewai-tools
```

Verify the installation:

```bash
pip show crewai-tools
```

You can now use the core framework and the additional tools throughout the later lessons.

---

### 4. Verify the CrewAI CLI

CrewAI provides a command-line interface that will be used throughout the Masterclass.

Run:

```bash
crewai --version
```

You can also inspect the available commands:

```bash
crewai --help
```

If the command executes successfully, the CrewAI CLI is available in your environment.

---

### 5. Create your first CrewAI project

Once CrewAI is installed, create a new project from the command line:

```bash
crewai create crew hello_crewai
```

This creates a new CrewAI project that can be used to explore the framework.

The modern CrewAI project structure includes components such as:

```text
hello_crewai/
├── agents/
├── knowledge/
├── skills/
├── tools/
├── crew.jsonc
├── pyproject.toml
└── README.md
```

The exact generated files may change between CrewAI releases, which is why the Masterclass will explain the generated project structure separately in the Project Architecture chapter.

> **Note:** CrewAI also provides a classic project scaffold for older Python/YAML-style projects. If you specifically need that structure, the classic scaffold can be created with the appropriate `--classic` option. The Masterclass uses the current project structure as its primary approach.

---

### 6. Verify the Python environment

Confirm that Python is being resolved from the virtual environment.

### Windows

```powershell
where python
```

### macOS / Linux

```bash
which python
```

The result should point to the `.venv` directory created for the Masterclass.

You can also verify the installed CrewAI packages:

```bash
pip show crewai
pip show crewai-tools
```

---

### 7. Verify the installation with Python

Create a file named:

```text
verify_installation.py
```

Add:

```python
import sys

import crewai


print("Python version:")
print(sys.version)

print("\nCrewAI installation:")
print("CrewAI imported successfully")

print("\nCrewAI version:")
print(getattr(crewai, "__version__", "Version information unavailable"))

print("\nInstallation verified.")
```

Run:

```bash
python verify_installation.py
```

If the script completes successfully, the Python environment can import CrewAI correctly.

---

### 8. API keys

Installing CrewAI does **not** require you to immediately configure a specific hosted LLM provider.

API keys become necessary when your application uses a provider that requires authentication.

For example, later lessons may configure:

```text
OpenAI
Anthropic
Gemini
Azure
Other supported providers
```

If you use a locally hosted model through Ollama, the authentication requirements are different because the model can run locally.

LLM provider configuration is intentionally covered in the **LLM Integration** chapter rather than making it part of the basic CrewAI installation.

---

### 9. Optional local Ollama setup

If you want to experiment with local models, Ollama can be installed separately.

The conceptual setup is:

```text
CrewAI
   │
   ↓
Ollama
   │
   ↓
Local LLM
```

Ollama is **not required** to complete the basic CrewAI installation.

It will be introduced later when the Masterclass covers LLM configuration and local models.

---

## Installation Checklist

Before continuing to the next chapter, verify:

```text
[ ] Supported Python version installed
[ ] Virtual environment created
[ ] Virtual environment activated
[ ] pip upgraded
[ ] crewai installed
[ ] crewai-tools installed
[ ] CrewAI CLI available
[ ] First CrewAI project created
[ ] CrewAI imports successfully
[ ] Installation verification completed
```

Your environment should now be ready for the rest of the Masterclass.

## Conclusion

CrewAI installation is intentionally kept separate from LLM provider configuration.

The setup process is:

```text
Python
   ↓
Virtual Environment
   ↓
CrewAI
   ↓
CrewAI Tools
   ↓
CrewAI CLI
   ↓
First CrewAI Project
   ↓
Installation Verification
```

Once this setup is complete, the same environment can be used throughout the Masterclass as we progressively move from individual agents and tasks to tools, multi-agent Crews, Processes, Flows, memory, knowledge and RAG, human-in-the-loop workflows, testing, observability, and production applications.

Run the verification script above. If it completes successfully and prints:

```text
Installation verified.
```

your CrewAI development environment is ready.

The next lesson begins with the fundamental building block of CrewAI: **Agents**.