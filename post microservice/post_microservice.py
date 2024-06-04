from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('POST_DB_USERNAME')}:{os.getenv('POST_DB_PASSWORD')}@{os.getenv('HOST_IP_ADR')}:{os.getenv('DB_PORT')}/{os.getenv('POST_DB_NAME')}"
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@/{os.getenv('DB_NAME')}?host={os.getenv('DB_HOST')}"
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)


def initialize_database():
    with app.app_context():
        db.create_all()


@app.route('/create_post', methods=['POST'])
def create_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    user_id = data.get('user_id')

    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({'message': 'Post created successfully'})


if __name__ == '__main__':
    initialize_database()
    app.run(debug=True, host='0.0.0.0', port=5002)
