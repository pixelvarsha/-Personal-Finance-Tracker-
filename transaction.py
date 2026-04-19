class Transaction:
    def __init__(self, amount, category, date, t_type):
        self.amount = amount
        self.category = category
        self.date = date
        self.type = t_type  # income or expense

    def to_list(self):
        return [self.amount, self.category, self.date, self.type]
