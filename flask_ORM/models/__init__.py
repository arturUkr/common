from db import db


room_staff = db.Table(
    'room_staff',
    db.Column('room_id', db.Integer, db.ForeignKey('room.number')),
    db.Column('staff_id', db.Integer, db.ForeignKey('staff.passport_id'))
)


class RoomModel(db.Model):
    __tablename__ = 'room'

    number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.passport_id'))

    def __repr__(self):
        return f"Room {self.number}"


class TenantModel(db.Model):
    __tablename__ = 'tenant'

    passport_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    rooms = db.relationship('RoomModel', backref='rooms')

    def __repr__(self):
        return f"Tenant {self.passport_id}"


class StaffModel(db.Model):
    __tablename__ = 'staff'

    passport_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    salary = db.Column(db.Float, nullable=False)
    serve = db.relationship('RoomModel', secondary=room_staff, backref='roomms')

    def __repr__(self):
        return f"Staff {self.passport_id}"
