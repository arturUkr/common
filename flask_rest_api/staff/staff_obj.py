
class Staff:
    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"Staff wirh passport_id: {self.passport_id}"
