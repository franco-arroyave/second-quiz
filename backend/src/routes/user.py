from flask import request, jsonify, Blueprint
from models.models import db, User
from models.schema import UserSchema
from sqlalchemy.exc import IntegrityError

user_bp = Blueprint('user', __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_bp.route('/', methods=['POST'])
def create_user():
    new_user_data = request.json
    errors = user_schema.validate(new_user_data)
    if errors:
        return jsonify({'errors': errors}), 400
    
    username = new_user_data['username']
    email = new_user_data['email']

    try:
        new_user = User(username, email)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'user': user_schema.dump(new_user)}), 201
    except IntegrityError as e:
        db.session.rollback()
        error_info = str(e.orig)

        if "Duplicate entry" in error_info:
            return jsonify({'error': 'Username or email already exists.'}), 400
        else:
            return jsonify({'error': error_info}), 500

    return user_schema.jsonify(new_user)

@user_bp.route('/', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = [{'name': user.username,'created': user.created} for user in all_users]
    return jsonify({'queries': result})

@user_bp.route('/<string:username>', methods=['GET'])
def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()

    if user:
        return jsonify({'user': user_schema.dump(user)})
    else:
        return jsonify({'message': 'User not found'}), 404