
import os

def conexion():
    return dict(
        host=os.environ.get('DB_HOST'), 
        user='root', 
        password=os.environ.get('DB_PASSWORD'), 
        db=os.environ.get('DB_NAME')
    )
