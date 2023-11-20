from flask import request, jsonify, Blueprint
from models.models import db, Query
from models.schema import QuerySchema
from sqlalchemy.exc import IntegrityError
from utils.security import Security

query_bp = Blueprint('query', __name__)

query_schema = QuerySchema()
queries_schema = QuerySchema(many=True)

@query_bp.route('/', methods=['POST'])
def create_query():
    has_access = Security.verify_token(request.headers)
    if has_access:
        data = request.json
        new_query = Query(
            name=data.get('name'),
            user_id=data.get('user_id'),
            description=data.get('description'),
            parameters=data.get('parameters'),
        )
        db.session.add(new_query)
        db.session.commit()
        return jsonify({'message': 'Query created successfully'}), 201
    else:
        return jsonify({'message': 'Unauthorized'}), 401

@query_bp.route('/', methods=['GET'])
def get_queries():
    has_access = Security.verify_token(request.headers)
    if has_access:
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        start_index = (page - 1) * per_page
        end_index = start_index + per_page

        queries = Query.query.all()[start_index:end_index]
        result = [{'name': query.name, 'user_id': query.user_id, 'description': query.description,
                'parameters': query.parameters, 'created': query.created} for query in queries]
        return jsonify({'queries': result})
    else:
        return jsonify({'message': 'Unauthorized'}), 401

@query_bp.route('/by/<int:user_id>', methods=['GET'])
def get_query(user_id):
    has_access = Security.verify_token(request.headers)
    if has_access:
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        queries = Query.query.filter_by(user_id=user_id).all()[start_index:end_index]
        result = [{'name': query.name, 'user_id': query.user_id, 'description': query.description,
                'parameters': query.parameters, 'created': query.created} for query in queries]
        return jsonify({'queries': result})
    else:
        return jsonify({'message': 'Unauthorized'}), 401

@query_bp.route('/<int:query_id>', methods=['PUT'])
def modify_query(query_id):
    has_access = Security.verify_token(request.headers)
    if has_access:
        query = Query.query.get_or_404(query_id)
        data = request.json

        query.name = data.get('name', query.name)
        query.description = data.get('description', query.description)
        query.parameters = data.get('parameters', query.parameters)

        db.session.commit()
        return jsonify({'message': 'Query modificada exitosamente'})
    else:
        return jsonify({'message': 'Unauthorized'}), 401

@query_bp.route('/clone', methods=['POST'])
def clone_query():
    data = request.json
    query_to_clone = Query.query.get_or_404(data['query_id'])
    new_query = Query(
        name=query_to_clone.nombre + ' copy',
        user_id=data['user_id'],
        description='Copy of ' + query_to_clone.description,
        parameters=query_to_clone.parameters
    )
    db.session.add(new_query)
    db.session.commit()
    return jsonify({'message': 'Query clon successfully'}), 201

@query_bp.route('/<int:query_id>', methods=['DELETE'])
def delete_query(query_id):
    query = Query.query.get_or_404(query_id)
    db.session.delete(query)
    db.session.commit()
    return jsonify({'message': 'Query deleted successfully '})