"""
Supplies the main Searcher service
"""
from json import loads
from Bio import Entrez


class Searcher:
    """
    Searcher is the first DBVirus component. Its main purpose
    is to provide an API for searching SRA and caching the
    results from its queries.
    """

    def __init__(self, email, api_key=None, db="sra"):
        self.api_key = api_key
        self.db = db
        self.email = email
        Entrez.email = self.email
        Entrez.api_key = self.api_key

    def search(self, query, max_results=10):
        """
        Searches NCBI for a given query and returns the result in json
        """
        handle = Entrez.esearch(self.db, query, retmax=max_results, retmode='json')
        result = loads(handle.read())
        return result


    def search_human_rna(self, read_length=50):
        """
        Queries SRA for _Homo sapiens_ RNA sequences
        """
        query = (
            '"Homo sapiens"[Organism] AND '
            f"{read_length}[ReadLength] AND "
            '(cluster_public[prop] AND "biomol rna"[Properties])'
        )

        return self.search(query)
