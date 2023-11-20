import datetime
import jwt
import pytz

class Security():

    tz=pytz.timezone('America/Bogota')
    
    @classmethod
    def generate_token(cls, user):
        payload = {
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=10),
            'username':user.username
        }
        return jwt.encode(payload, 'secret', algorithm='HS256')
    
    @classmethod
    def verify_token(cls, header):
        if 'Authorization' in header:
            authorizarion = header['Authorization']
            encoded_token = authorizarion.split(' ')[1]

            try:
                payload = jwt.decode(encoded_token, 'secret', algorithms=['HS256'])
                return True
            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
                return False
        return False