"""
Mongoengine documents used for caching
"""
# pylint: disable=wildcard-import, unused-wildcard-import, no-member
from datetime import datetime

from mongoengine import *
from pytz import utc


class SearchResult(DynamicDocument):
    """
    Mongoengine document to hold search results
    """

    created_at = DateTimeField(default=datetime.now(utc))


class EntrezItem(DynamicDocument):
    """
    Mongoengine document to hold search items
    """

    created_at = DateTimeField(default=datetime.now(utc))
    uid = StringField()
