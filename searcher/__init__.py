from Bio import Entrez

class Searcher:
    
    def __init__(self, db="sra"):
        self.db = db

    def search(self, query):
        Entrez.email = "felipe@felipevr.com"
        Entrez.esearch(self.db, query, retmax=1)
