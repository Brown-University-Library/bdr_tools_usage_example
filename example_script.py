# /// script
# requires-python = ">=3.8,<3.9"
# dependencies = [
#     "bdrcommon",
#     "bdr_tools",
#     "bdrxml",
#     "eulxml~=1.1.0",
#     "pysolr~=3.8.0",
#     "rdflib~=6.0.0",
#     "redis~=3.5.0",
#     "requests~=2.26.0",
#     "requests-toolbelt~=0.9.0",
#     "rq~=0.13.0",
#     "setuptools",
# ]
#
# [tool.uv.sources]
# bdrcommon = { git = "ssh://git@github.com/Brown-University-Library/bdrcommon.git", rev = "v0.5.0" }
# bdr_tools = { git = "ssh://git@github.com/Brown-University-Library/bdr_tools.git", rev = "1029d0d0758b5eba9d77f3404bcf577a241b655d" }
# bdrxml = { git = "https://github.com/Brown-University-Library/bdrxml.git", rev = "d167e4c6f7ae85104f92b61877f373fd4ace33ed" }
# ///

"""
Purpose
- to demonstrate usage of the simplified bdr_tools architecture, removing workshop dependencies,
  allow it to be run from any valid server.

Usage:
    $ uv run --env-file "../.env" ./uv_script.py --collection_name "The Collection Name"
"""

import argparse
import pprint

import bdr_tools


## run code ---------------------------------------------------------
def run_code(collection_name: str) -> None:
    """
    Runs code.
    Called by dundermain.

    Args:
        collection_name (str): The name of the collection.
    """
    query: str = f'ir_collection_name:"{collection_name}"'
    print('\n' + f'Collection Name, ``{query}``' + '\n\n')
    results = bdr_tools.solr.search(
        query,
        rows=5,
        fl='pid,primary_title',
        sort='pid asc',  # _does_ sort by pid, but by pid as a string, not as a number; eg `bdr:123` comes before `bdr:5`
    ).docs
    print(f'results, ``{pprint.pformat(results)}``\n\n')
    return


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Run code with a specified collection name')
    parser.add_argument('-c', '--collection_name', required=True, type=str, help='Name of the collection')
    return parser.parse_args()


if __name__ == '__main__':
    args: argparse.Namespace = parse_arguments()
    run_code(args.collection_name)

## eof
