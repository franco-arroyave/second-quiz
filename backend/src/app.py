from flask import Flask
import time
#from flask_cors import CORS
from models.models import db
from routes.user import user_bp
from routes.query import query_bp
from config.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(query_bp, url_prefix='/query')

db.init_app(app)

if __name__ == "__main__":
    time.sleep(10)
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
