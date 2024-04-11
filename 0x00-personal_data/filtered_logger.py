#!/usr/bin/env python3
"""
A module that returns the log message obfuscated
"""
import logging
from typing import List
import re
from os import environ
from mysql.connector import connection

PII_FIELDS = ('name', 'email', 'password', 'ssn', 'phone')

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ filter data """
    temp = message
    for field in fields:
        temp = re.sub(field + "=.*?" + separator, field + "=" + redaction + separator, temp)

    return temp


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filters incoming log record """
        return filter_datum(self.fields, self.REDACTION, super(
            RedactingFormatter, self).format(record), self.SEPARATOR)

def get_logger() -> logging.Logger:
    """ logs user data """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream_handler)
    return logger

def get_db() -> connection.MySQLConnection:
    """ connect to mysql server """
    username = environ.get("PERSONAL_DATA_DB_USERNAME")
    password = environ.get("PERSONAL_DATA_DB_PASSWORD")
    host = environ.get("PERSONAL_DATA_DB_HOST")
    db = environ.get("PERSONAL_DATA_DB_NAME")

    return connection.MySQLConnection(
            user=username,
            password=password,
            host=host,
            database=db)
