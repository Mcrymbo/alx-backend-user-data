#!/usr/bin/env python3
"""
A module for managing API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    class that implements API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ handles paths that require auth """
        if path is None or not excluded_paths:
            return True
        for ex in excluded_paths:
            if ex.endswith('*') and path.startswith(ex[:-1]):
                return False
            elif ex in {path, path + '/'}:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ handles request object """
        if not request or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) ->TypeVar('User'):
        """ handles current user """
        return None
