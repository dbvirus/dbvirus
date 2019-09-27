"""
Unit tests for the searcher module. Those tests mock the Entrez class
and do not make any sort of HTTP request.
"""
# pylint: disable=redefined-outer-name
import io
from pathlib import Path
from Bio import Entrez
from searcher import Searcher


def test_searcher_initialization(searcher):
    """
    Tests a searcher initialization parameters
    """

    assert isinstance(searcher, Searcher)
    assert searcher.db == "sra"

    new_searcher = Searcher("another@test.com", db="other_db")
    assert new_searcher.db == "other_db"


def test_searcher_searches_sra(searcher: Searcher, mocker):
    """
    Tests if the searcher, when supplied with a valid search string,
    calls the correct Biopython's Entrez methods
    """

    # We need to supply a return value to the esearch function.
    # That return value must be a buffer.
    mocker.patch("Bio.Entrez.esearch")
    Entrez.esearch.return_value = io.StringIO("{}")

    searcher.search('"Homo sapiens"[Organism]')

    # pylint: disable=no-member
    Entrez.esearch.assert_called_with(
        "sra", '"Homo sapiens"[Organism]', retmax=10, retmode="json"
    )


def test_searcher_configurer_entrez():
    """
    In order for everything to work, the Searcher must set Entrez's e-mail and
    API Key parameters
    """

    Searcher(email="test@test.com", api_key="3141516")

    assert Entrez.email == "test@test.com"
    assert Entrez.api_key == "3141516"


def test_searcher_returns_dictionary(searcher: Searcher, mocker):
    """
    The searcher must return a json formatted SRA resultset
    """
    mocker.patch("Bio.Entrez.esearch")
    Entrez.esearch.return_value = io.StringIO("{}")
    result = searcher.search("Human", max_results=3)
    assert isinstance(result, dict)


def test_fetch_result(searcher: Searcher, mocker):
    """
    Given an Entrez UID, the searcher must acquire the related data
    """
    mocker.patch("Bio.Entrez.efetch")
    Entrez.efetch.return_value = open(
        Path(__file__).parent.absolute().joinpath("sample_efetch_result.xml")
    )

    data = searcher.fetch("8801091")

    # pylint: disable=no-member
    Entrez.efetch.assert_called()

    assert data
    assert isinstance(data, dict)
