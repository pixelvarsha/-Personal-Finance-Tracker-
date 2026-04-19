class User:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def set_budget(self, amount):
        self.budget = amount

    def get_budget(self):
        return self.budget
