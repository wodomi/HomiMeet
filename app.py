from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from routes.auth import auth_bp
from routes.meetup import meetup_bp
from routes.user import user_bp
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to HomiMeet!"
if __name__ == '__main__':
    app.run(debug=True)

CORS(app)

# Database configuration
app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_USER'] = os.getenv('DB_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('DB_NAME')

mysql = MySQL(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(meetup_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)

def check_cloud_environment():
    env = os.getenv('ENV', 'cloud')  # Default to 'cloud' if not set
    if env == 'cloud':
        print("Running in cloud environment: configure cloud settings.")
    elif env != 'local':
        raise EnvironmentError("Invalid environment setup. Please check your configuration.")

check_cloud_environment()
