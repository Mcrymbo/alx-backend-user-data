#!/usr/bin/env python3
"""
implements basic authentication
"""
from base64 import b64decode
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    class that implements basic authentication
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Returns Base64 part of the authorization header
        """
        if authorization_header and isinstance(
                authorization_header,
                str) and authorization_header.startswith('Basic '):
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ decode the value of base64 auth header """
        if not base64_authorization_header and not isinstance(
                base64_authorization_header,
                str):
            return None

        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None


    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extract user email and password from the base64
        decorded value
        """
        if not decoded_base64_authorization_header:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        header = decoded_base64_authorization_header.split(':')
        return header[0], header[1]
