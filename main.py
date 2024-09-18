from Environment.NQueensEnvironment import NQueensEnvironment
from Agent.NQueensAgent import NQueensAgent

n = int(input())

environment = NQueensEnvironment(n)

agent = NQueensAgent(n)

environment.insert(agent)

environment.run()
