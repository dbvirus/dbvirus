"""
This module provides functional tests for the searcher module. Those tests
do hit the NCBI databases and use live data acquired from those sources.
"""
import jsonschema
from searcher import Searcher
from .schemata import SEARCH_RESULT_SCHEMA


def test_searcher_format(searcher: Searcher):
    """
    The searcher must return data in an specified format
    """
    result = searcher.search("Human", max_results=3)

    assert isinstance(result, dict)
    assert "header" in result.keys()
    assert "esearchresult" in result.keys()
    jsonschema.validate(result, SEARCH_RESULT_SCHEMA)
