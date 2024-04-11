#!/usr/bin/env python3
"""
A module that returns the log message obfuscated
"""
import logging
from typing import List
import re


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
