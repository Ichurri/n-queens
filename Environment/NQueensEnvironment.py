from .Environment import Environment


class NQueensEnvironment(Environment):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.domain = {i: list(range(n)) for i in range(n)}

    def get_perceptions(self, agent):
        return self.domain

    def execute(self, agent):
        solutions = agent.program()
        if solutions:
            print(f"{len(solutions)} solutions were found:")
            for i, solution in enumerate(solutions):
                print(f"Solution {i + 1}: {solution}")
        else:
            print("No solutions were found.")
