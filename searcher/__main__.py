"""
Defines a basic CLI for exposing Searcher
"""
import fire

from searcher import Searcher


def main(email, api_key=None, query=None, mongo_url=None, download_all=False, **kwargs):
    """
    Given an e-mail and API key, searches for Human RNA and outputs the result
    """
    print(
        """
    This is a sample usage. It will search for a given query.
    If no query is provided, it will search for Human RNA data in SRA.
    After searching, it will output the first result.
    """
    )

    searcher = Searcher(email, api_key=api_key, mongo_url=mongo_url)

    if query:
        searcher.search(query, **kwargs)
    else:
        searcher.search_human_rna()

    if download_all:
        assert searcher.cached, "Searcher is not cached."


if __name__ == "__main__":
    fire.Fire(main)
