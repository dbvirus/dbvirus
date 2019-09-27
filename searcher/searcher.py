"""
Supplies the main Searcher service
"""
from json import loads

from Bio import Entrez
from mongoengine import connect, connection
from pymongo.errors import ServerSelectionTimeoutError
from xmltodict import parse

from cacher.documents import SearchResult, EntrezItem


class Searcher:
    """
    Searcher is the first DBVirus component. Its main purpose is to
    provide an API for searching NCBI databases and caching the
    results from its queries.
    """

    def __init__(self, email, api_key=None, db="sra", mongo_url=None):
        self.api_key = api_key
        self.db = db
        self.email = email
        Entrez.email = self.email
        Entrez.api_key = self.api_key

        self._result = None

        # The cached flag is set accordingly to the connectivity to a Mongodb
        if mongo_url:
            try:
                connect(host=mongo_url)
                connection.get_connection().server_info()
            except ServerSelectionTimeoutError:
                self.cached = False
            else:
                self.cached = True
        else:
            self.cached = False

    def search(self, query, limit=10, **kwargs):
        """
        Searches NCBI for a given query and returns the result in json
        """
        handle = Entrez.esearch(self.db, query, retmax=limit, retmode="json", **kwargs)
        result = loads(handle.read())
        self._result = result

        if self.cached:
            SearchResult(**result).save()

        return result

    def search_human_rna(self, read_length=50, **kwargs):
        """
        Queries SRA for _Homo sapiens_ RNA sequences
        """
        query = (
            '"Homo sapiens"[Organism] AND '
            f"{read_length}[ReadLength] AND "
            '(cluster_public[prop] AND "biomol rna"[Properties])'
        )

        return self.search(query, **kwargs)

    def fetch(self, uid):
        """
        Fetch receives an Entrez UID and returns the related record

        https://www.ncbi.nlm.nih.gov/books/NBK25499/#_chapter4_EFetch_
        """
        # pylint: disable=no-member
        if self.cached and EntrezItem.objects(uid=uid):
            return loads(EntrezItem.objects(uid=uid)[0].to_json())

        handle = Entrez.efetch(id=uid, db=self.db, rettype="full", retmode="xml")
        data = handle.read()
        data = parse(data)
        data["uid"] = uid

        if self.cached:
            data = EntrezItem(**data).save()
            data = loads(data.to_json())

        return data

    def __getitem__(self, key):
        """
        Override the subscript operator, allowing the caller to fetch the n-th
        result in a more pythonic fashion.
        """
        assert self._result, "Please, make a query first."
        return self.fetch(self._result["esearchresult"]["idlist"][key])

    def __len__(self):
        """
        A Searcher len will be its last query's result size
        """
        if not (self._result and self._result["esearchresult"]["idlist"]):
            return 0

        return len(self._result["esearchresult"]["idlist"])
