from flask_marshmallow import Marshmallow

class UserSchema(Marshmallow().Schema):
    class Meta:
        fields = ('id', 'username', 'email')

class QuerySchema(Marshmallow().Schema):
    class Meta:
        fields = ('id', 'qy_name', 'user_id', 'description', 'parameters')

class CommentSchema(Marshmallow().Schema):
    class Meta:
        fields = ('id', 'query_id', 'user_id', 'description', 'created')