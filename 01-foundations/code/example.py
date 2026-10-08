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
