from flask import Flask
from controller.database import db
from controller.config import config
from controller.models import *

app = Flask(__name__, template_folder='templates',static_folder='static')
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()

    admin_role=Role.query.get.filter_by(name='Admin').first()
    if not admin_role:
        admin_role = Role(name='Admin')
        db.session.add(admin_role)
        db.session.commit()

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)