"""
Defines a basic CLI for exposing Searcher
"""
import fire

from searcher import Searcher


def main(email, api_key=None, query=None):
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

    searcher = Searcher(email, api_key=api_key)

    if query:
        searcher.search(query)
    else:
        searcher.search_human_rna()
    print(searcher[0])


if __name__ == "__main__":
    fire.Fire(main)
