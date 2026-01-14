from flask import Flask, render_template
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

    # admin_user=User.query.filter_by(user_email='admin@gmail.com').first()
    # if not admin_user:
    #     admin_user = User(
    #         user_name='Super Admin',
    #         user_email='admin@gmail.com',
    #         passsword='123456789'
    #     )
    #     db.session.add(admin_user)

    #     admin_user_detail=User.query.filter_by(user_email='admin@gmail.com').first()
    #     admin_role = Role.query.filter_by(name='Admin').first()

    #     user_id=admin_user_detail.user_id
    #     role_id=admin_role.id

    #     user_role=UserRole(user_id=user_id,role_id=role_id)
    #     db.session.add(user_role)
    admin_user = User.query.filter_by(user_email="admin@gmail.com").first()
    if not admin_user:
        admin_role = Role.query.filter_by(name="Admin").first()
        admin_user = User(
            user_name='Super Admin',
            user_email='admin@gmail.com',
            passsword='123456789',
            roles=[admin_role]
        )
        db.session.add(admin_user)

    db.session.commit()
    




from controller.auth_routes import *
from controller.routes import *

if __name__ == '__main__':
    app.run(debug=True)