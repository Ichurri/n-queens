from .Agent import Agent

class CSPAgent(Agent):
    def __init__(self, variables, domains, constraints):
        super().__init__()
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignments = {}
        self.alive = True

    def is_consistent(self, variable, value):
        # Verifies if assigning a value to a variable is consistent with the current constraints.
        for (var, constraint) in self.constraints.get(variable, {}).items():
            if var in self.assignments and not constraint(value, self.assignments[var]):
                return False
        return True

    def select_unassigned_variable(self):
        for variable in self.variables:
            if variable not in self.assignments:
                return variable
        return None

    def order_values(self, variable):
        return self.domains[variable]

    def backtracking(self):
        if len(self.assignments) == len(self.variables):
            return self.assignments

        variable = self.select_unassigned_variable()

        for value in self.order_values(variable):
            if self.is_consistent(variable, value):
                self.assignments[variable] = value
                result = self.backtracking()
                if result is not None:
                    return result
                del self.assignments[variable]

        return None

    def program(self):
        solution = self.backtracking()
        if solution:
            self.alive = False
        return solution
