from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('USER_DB_USERNAME')}:{os.getenv('USER_DB_PASSWORD')}@{os.getenv('HOST_IP_ADR')}:{os.getenv('DB_PORT')}/{os.getenv('USER_DB_NAME')}"
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@/{os.getenv('DB_NAME')}?host={os.getenv('DB_HOST')}"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


def initialize_database():
    with app.app_context():
        db.create_all()


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


if __name__ == '__main__':
    initialize_database()
    app.run(debug=True, host='0.0.0.0', port=5001)

