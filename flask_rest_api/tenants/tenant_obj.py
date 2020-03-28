# - Name
# - PassportID
# - Age
# - Sex
# - Address(city, street) use Nested
# - RoomNumber


class Tenants:

    def __init__(self, name, passport_id, age, sex, address, room_number):
        self.name = name
        self.passport_id = passport_id
        self.age = age
        self.sex = sex
        self.address = address
        self.room_number = room_number

    def __repr__(self):
        return f"Tenant with passport_id = {self.passport_id}"
