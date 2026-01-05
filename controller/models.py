from controller.database import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    passsword = db.Column(db.String(120), nullable=False)
    user_name = db.Column(db.String(120), nullable=False)

    roles = db.relationship('Role', secondary='user_role', backref='users', lazy=True)
    customers= db.relationship('Customer', backref='user', lazy=True,uselist=False)
    store_manager_details= db.relationship('StoreManager', backref='user', lazy=True,uselist=False)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

class UserRole(db.Model):
    #table name will be "user_role"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)   

class StoreManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    
    qualification = db.Column(db.String(120), nullable=True)
    
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    address = db.Column(db.String(200), nullable=True)
    preffered_mode_of_payment = db.Column(db.String(50), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)