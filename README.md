# Purpose

Shows how to use the simplified bdr_tools architecture in a script, which can be run from any valid server.


# Usage

    $ uv run --env-file "../.env" ./example_script.py --collection_name "The Collection Name"

The output will show the collection name, followed by five 


# Notes

- `.env` handling was added to `uv` in version 6.10.

- Neither `uv` or the PEP-723 inline-script-metadata is required. You could instead: 
    - install a virtual environment
    - a requirements file 
    - update the requirements file to import the python-dotenv package
    - update the virtual environment from the requirements file
    - update the code to load and use the python-dotenv package
    - run the script via a regular python call

- Feel free to add other sample scripts!

- Note that the `example_script.py` specifies `python 3.8`. _Normally_ we should use `python 3.12` for new scripts wherever possible. However, `bdr_tools` has dependencies that are incompatible with python 3.12. So update python and package versions cautiously. (This upgrade-caution has nothing to do with this improved bdr_tools architecture; it's true for using it via the workshop approach, too.)
