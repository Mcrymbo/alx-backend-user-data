#!/usr/bin/env python3
"""
view for handling all routes for session authentication
"""
from api.v1.views import app_views
from flask import request, jsonify
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def sess_login() -> str:
    
    """ login the user into a session """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({ "error": "email missing" }), 400
    if not password:
        return jsonify({ "error": "password missing" }), 400

    user_obj = User.search({'email': email})
    if not user_obj:
        return jsonify({ "error": "no user found for this email" }), 404

    user = user_obj[0]
    if not user.is_valid_password(password):
        return jsonify({ "error": "wrong password" }), 401
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    session_name = getenv('SESSION_NAME')

    res = jsonify(user.to_json())
    res.set_cookie(session_name, session_id)
    return res


@app_views.route('aut_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ deletes a session """
    from api.v1.app import auth

    destroy = auth.destroy_session(request)
    if destroy is False:
        abort(404)
    return jsonify({}), 200
