
class Rooms:

    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price

    def __repr__(self):
        return f"Room with number: {self.number}"

    # def __eq__(self, other):
    #     return self.number == other.number
