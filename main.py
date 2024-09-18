from Environment.NQueensEnvironment import NQueensEnvironment
from Agent.NQueensAgent import NQueensAgent

n = int(input())

environment = NQueensEnvironment(n)

agent = NQueensAgent(n)

environment.insert(agent)

environment.run()

num_solutions = len(agent.solutions)
print(f"{num_solutions} solutions were found.")
