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
#     "ipython"
# ]
# [tool.uv.sources]
# bdrcommon = { git = "ssh://git@github.com/Brown-University-Library/bdrcommon.git", rev = "v0.5.0" }
# bdr_tools = { git = "ssh://git@github.com/Brown-University-Library/bdr_tools.git", rev = "1029d0d0758b5eba9d77f3404bcf577a241b655d" }
# bdrxml = { git = "https://github.com/Brown-University-Library/bdrxml.git", rev = "d167e4c6f7ae85104f92b61877f373fd4ace33ed" }
# ///

from IPython import embed

import bdr_tools
import bdrcommon
import bdrxml

print('\nLaunching IPython shell with all dependencies available...\n')
embed()
