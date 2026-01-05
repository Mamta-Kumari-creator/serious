from flask import Flask
from controller.database import db
from controller.config import config
from controller.models import *

app = Flask(__name__, template_folder='templates',static_folder='static')
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()

    admin_role=Role.query.filter_by(name='Admin').first()
    if not admin_role:
        admin_role = Role(name='Admin')
        db.session.add(admin_role)

    cust_role=Role.query.filter_by(name='Customer').first()
    if not cust_role:
        cust_role = Role(name='Customer')
        db.session.add(cust_role)

    manager_role=Role.query.filter_by(name='Manager').first()
    if not manager_role:
        manager_role = Role(name='Manager')
        db.session.add(manager_role)

    admin_user=User.query.filter_by(email='admin@gmail.com').first()
    if not admin_user:
        admin_user = User(
            name='Admin User',
            email='admin@gmail.com',
            password='admin123',
            role=admin_role
        )
        db.session.add(admin_user)

    db.session.commit()
    


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)