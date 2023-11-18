from flask import request, jsonify, Blueprint
from models.models import db, Comment
from models.schema import CommentSchema
from sqlalchemy.exc import IntegrityError

comment_bp = Blueprint('comment_bp', __name__)

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

@comment_bp.route('/', methods=['POST'])
def get_comments():
    data = request.json
    new_comment = Comment(
        query_id=data.get('query_id'),
        user_id=data.get('user_id'),
        description=data.get('description'),
    )
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({'message': 'Comment created successfully'}), 201

@comment_bp.route('/<int:query_id>', methods=['GET'])
def get_query_comments(query_id):
    comments = Comment.query.filter_by(query_id=query_id).all()
    return comments_schema.jsonify(comments)