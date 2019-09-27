"""
Defines a basic CLI for exposing Searcher
"""
import fire
from tqdm import tqdm

from searcher import Searcher

# pylint: disable=too-many-arguments, bad-continuation
def main(
    email,
    api_key=None,
    query=None,
    mongo_url=None,
    download_all=False,
    limit=None,
    **kwargs,
):
    """
    Given an e-mail and API key, searches for Human RNA and outputs the result
    """

    searcher = Searcher(email, api_key=api_key, mongo_url=mongo_url)

    if query and query != "human":
        searcher.search(query, limit=limit, **kwargs)
    else:
        searcher.search_human_rna(limit=limit)

    if download_all:
        assert searcher.cached, "Searcher is not cached."

        print(f"Found {len(searcher)} results")
        all(tqdm(searcher))


if __name__ == "__main__":
    fire.Fire(main)
