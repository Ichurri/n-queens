class Environment:
    def __init__(self):
        self.agents = []

    def get_perceptions(self, agent):
        raise Exception("No implementation exists")

    def execute(self, agent):
        raise Exception("No implementation exists")

    def evolve(self):
        if not self.terminate():
            for agent in self.agents:
                self.get_perceptions(agent)
                self.execute(agent)

    def run(self):
        while True:
            if self.terminate():
                break
            self.evolve()

    def terminate(self):
        return any(not agent.alive for agent in self.agents)

    def insert(self, agent):
        self.agents.append(agent)
