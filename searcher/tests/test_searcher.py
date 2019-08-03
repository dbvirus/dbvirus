"""
Unit tests for the searcher module
"""
# pylint: disable=redefined-outer-name
import pytest
from Bio import Entrez
from searcher import Searcher


@pytest.fixture
def searcher():
    """
    Fixture that provides a Searcher instance
    """
    return Searcher("test@test.com")


def test_searcher_initialization(searcher):
    """
    Tests a searcher initialization parameters
    """

    assert searcher
    assert searcher.db == "sra"

    new_searcher = Searcher("another@test.com", db="other_db")
    assert new_searcher.db == "other_db"


def test_searcher_searches_sra(searcher: Searcher, mocker):
    """
    Tests if the searcher, when supplied with a valid search string,
    calls the correct Biopython's Entrez methods
    """

    mocker.patch("Bio.Entrez.esearch")
    searcher.search('"Homo sapiens"[Organism]')

    # pylint: disable=no-member
    Entrez.esearch.assert_called_with("sra", '"Homo sapiens"[Organism]', retmax=1)


def test_searcher_configurer_entrez(mocker):
    """
    In order for everything to work, the Searcher must set Entrez's e-mail and
    API Key parameters
    """

    Searcher(email="test@test.com", api_key="3141516")

    assert Entrez.email == "test@test.com"
    assert Entrez.api_key == "3141516"
