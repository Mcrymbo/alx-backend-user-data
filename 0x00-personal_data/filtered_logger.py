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
