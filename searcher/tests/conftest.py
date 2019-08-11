"""
Define a Searcher fixture to be used by the other tests
"""
import pytest
from searcher import Searcher


@pytest.fixture
def searcher():
    """
    Fixture that provides a Searcher instance
    """
    return Searcher("test@test.com")
