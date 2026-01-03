from flask import Flask
from controller.database import db
from controller.config import config
app = Flask(__name__, template_folder='templates',static_folder='static')
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()
    
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)