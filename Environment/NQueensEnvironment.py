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
                print(f"\nSolution {i + 1}: {solution}")
                self.display_board(solution)
        else:
            print("No solutions were found.")

    def display_board(self, solution):
        n = len(solution)
        for row in range(n):
            row_str = ""
            for column in range(n):
                if solution.get(row) == column:
                    row_str += " Q "
                else:
                    row_str += " . "
            print(row_str)
