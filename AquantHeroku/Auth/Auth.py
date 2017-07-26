from flask_httpauth import HTTPBasicAuth
from flask import make_response, jsonify

auth = HTTPBasicAuth()


@auth.verify_password
def get_password(username, password):
    if username == 'z':
        return 'x'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
