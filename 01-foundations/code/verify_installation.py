import sys

import crewai


print("Python version:")
print(sys.version)

print("\nCrewAI installation:")
print("CrewAI imported successfully")

print("\nCrewAI version:")
print(getattr(crewai, "__version__", "Version information unavailable"))

print("\nInstallation verified.")
