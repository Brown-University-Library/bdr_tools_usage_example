# Purpose

Shows how to use the simplified bdr_tools architecture in a script, or via an ipython shell, either of which can be run from any valid server.

The `example_script.py` simply takes a collection name, and uses bdr_tools to query solr. It prints out the pid and title of five items of the collection.

The `example_ipython_shell.py` just loads ipython with access to bdr_tools and other dependencies, then queries solr via bdr_tools and prints out the first five items' titles.

---


# Usage

- `example_script.py`

        $ uv run --env-file "../.env" ./example_script.py --collection_name "The Collection Name"

    output: the collection name, followed by the pid and title of five items of the collection.

- `example_ipython_shell.py`

        $ uv run --env-file "../.env" ./example_ipython_shell.py

        Launching IPython shell with all dependencies available...

        Python 3.8.9 (default, Apr 15 2021, 00:39:38) 
        Type 'copyright', 'credits' or 'license' for more information
        IPython 8.12.3 -- An enhanced Interactive Python. Type '?' for help.

        In [1]: query = '*:*'

        In [2]: bdr_tools.solr.search( query, rows=5, fl='primary_title' ).docs
        Out[2]: 
        [{'primary_title': 'test sha512 checksum'},
        {'primary_title': 'test large object'},
        {'primary_title': 'test large object'},
        {'primary_title': 'setUp object'},
        {'primary_title': 'test title'}]

---


# Notes

- `.env` handling was added to `uv` in version 6.10.

- Neither `uv` or the PEP-723 inline-script-metadata is required. You could instead, for `example_script.py`: 
    - install a virtual environment
    - create a requirements.in file 
    - compile a requirements.txt file
    - update the requirements .in and .txt files to import the python-dotenv package
    - update the virtual environment from the requirements file
    - update the code to load and use the python-dotenv package
    - run the script via a regular python call

    ...and do something similar for `example_python_shell.py`

- Feel free to add other sample scripts!

- Note that these scripts specify `python 3.8`. _Normally_ we should use `python 3.12` for new scripts wherever possible. However, `bdr_tools` has dependencies that are incompatible with python 3.12 -- and which cannot be updated easily without first changing other things (ie rq and redis updates will likely require updating our queuing code). So update python and package versions cautiously. (This upgrade-caution has nothing to do with this simplified bdr_tools architecture; it's true for using it via the workshop approach, too.)

- Note that the PEP-723 inline-script-metadata refers to a commit-hash for bdr_tools, which is an older version than the current one. That's simply because there have been lots of commits to the bdr_tools repo that don't at all affect code (eg, the readme has been updated many times). Once the bdr_tools repo has a release, this repo will be updated with a tag representing a release. 

---
