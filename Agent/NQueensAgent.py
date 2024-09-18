from .CSPAgent import CSPAgent

class NQueensAgent(CSPAgent):
    def __init__(self, n):
        variables = list(range(n))
        domains = {i: list(range(n)) for i in range(n)}
        constraints = {i: {} for i in range(n)}
        self.solutions = []

        for i in range(n):
            for j in range(i + 1, n):
                constraints[i][j] = lambda qi, qj, i=i, j=j: qi != qj and abs(qi - qj) != abs(i - j)

        super().__init__(variables, domains, constraints)

    def is_consistent(self, variable, value):
        for var in range(variable):
            qj = self.assignments.get(var)
            if qj is not None:
                if qj == value or abs(var - variable) == abs(qj - value):
                    return False
        return True

    def backtracking(self):
        # Modified method to find all CSP solutions using backtracking.
        if len(self.assignments) == len(self.variables):
            self.solutions.append(self.assignments.copy())
            return None

        variable = self.select_unassigned_variable()

        for value in self.order_values(variable):
            if self.is_consistent(variable, value):
                self.assignments[variable] = value
                self.backtracking()
                del self.assignments[variable]

        return None

    def program(self):
        self.backtracking()
        self.alive = False
        return self.solutions
