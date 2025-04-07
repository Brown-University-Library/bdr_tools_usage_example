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
Purpose: shows a simplified architecture for using bdr_tools, that can be run from any valid server.

Usage:
    $ uv run --env-file "../.env" "./uv_script.py"

Notes:
    - the `--env-file` option requires uv 0.6.10 or later.
    - Some packages don't work with python-3.12, so updates should be done cautiously.
    - It'd be good to have a suite of tests for the new bdr_tools github repo (they may exist in the workshop repo).
    - newer versions of `rq` are, IIRC, not backward-compatible.
    - newer versions of `rq` may require newer versions of redis, which may not be backward-compatible.
"""

import logging
import os
import pprint

import bdr_tools

## setup logging ----------------------------------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S',
)
log = logging.getLogger('example_script')
log.debug('starting log')


## envar constants --------------------------------------------------
COLLECTION_NAME = os.environ['UVSCRPT__COLLECTION_NAME']
log.debug(f'COLLECTION_NAME, ``{COLLECTION_NAME}``')


def quiet_package_loggers():
    """
    Minimizes output from package loggers.
    Not all of these are needed, but there was _lots_ of package logging, so I just disabled them all.
    Here's how to find possible package loggers:
        log.debug( f'logger-dict, ``{pprint.pformat(logging.Logger.manager.loggerDict)}``' )
    Called by `__main__`.
    """
    log.info('updating logging')
    for logger_identifier in [
        'bdr_tools',
        'bdrcommon',
        'bdrxml',
        'django',
        'eulxml',
        'pysolr',
        'redis',
        'requests',
        'rq',
        'workshop_common',
        'urllib3',
    ]:
        logging.getLogger(logger_identifier).setLevel(logging.WARNING)
    return


## run code ---------------------------------------------------------
def run_code():
    """Runs code.
    Called by `__main__`."""
    log.info('running code')
    log.debug('about to run solr search')
    results = bdr_tools.solr.search(
        f'ir_collection_name:"{COLLECTION_NAME}"',
        rows=5,
        fl='pid,primary_title',
        sort='pid asc',  # _does_ sort by pid, but by pid as a string, not as a number; eg `bdr:123` comes before `bdr:5`
    ).docs
    log.info(f'results, ``{pprint.pformat(results)}``')
    return


if __name__ == '__main__':
    log.info('__name__ is `main`')
    quiet_package_loggers()  # disables imported-package logging
    run_code()  # THIS IS WHERE WORK IS DONE
    log.debug('eof')

## eof
