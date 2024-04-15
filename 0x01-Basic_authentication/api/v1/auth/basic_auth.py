#!/usr/bin/env python3
"""
implements basic authentication
"""
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
