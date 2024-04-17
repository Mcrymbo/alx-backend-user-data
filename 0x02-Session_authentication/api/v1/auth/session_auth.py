#!/usr/bin/env python3
"""
Module for implementing session authentication
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """ class for implementing session auth
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a session ID """
        if not user_id or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns user ID based on session ID """
        if not session_id or isinstance(session_id, str) is False:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns user based on cookie id """
        session_id = self.session_cookie(request)
        if session_id:
            user_id = self.user_id_for_session_id(session_id)
            if user_id:
                return User.get(user_id)
