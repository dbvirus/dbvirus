"""
Unit tests for the searcher module
"""
import pytest
from Bio import Entrez
from searcher import Searcher


@pytest.fixture
def searcher():
    return Searcher()


def test_searcher_initialization():
    """
    Tests a searcher initialization parameters
    """
    searcher = Searcher()
    assert searcher
    assert searcher.db == "sra"

    searcher = Searcher(db="other_db")
    assert searcher.db == "other_db"


def test_searcher_searches_sra(searcher: Searcher, mocker):
    """
    Tests if the searcher, when supplied with a valid search string,
    calls the correct Biopython's Entrez methods
    """
    
    mocker.patch("Bio.Entrez.esearch")
    searcher.search('"Homo sapiens"[Organism]')
    Entrez.esearch.assert_called_with('sra', '"Homo sapiens"[Organism]', retmax=1)
