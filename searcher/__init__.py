"""
Supplies the main Searcher service
"""
from Bio import Entrez


class Searcher:
    def __init__(self, email, api_key=None, db="sra"):
        self.api_key = api_key
        self.db = db
        self.email = email
        Entrez.email = self.email
        Entrez.api_key = self.api_key

    def search(self, query):
        Entrez.esearch(self.db, query, retmax=1)
