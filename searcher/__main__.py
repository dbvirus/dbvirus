"""
Defines a basic CLI for exposing Searcher
"""
import fire

from searcher import Searcher


def main(email, api_key=None):
    """
    Given an e-mail and API key, searches for Human RNA and outputs the result
    """
    searcher = Searcher(email, api_key=api_key)
    searcher.search_human_rna()
    print(searcher[0])


if __name__ == "__main__":
    fire.Fire(main)
