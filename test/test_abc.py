# # some_file.py
# import sys
# # caution: path[0] is reserved for script path (or '' in REPL)
# sys.path.insert(1, '/path/to/application/app/folder')
# import file

# Just make sure folder also contains an __init__.py. This allows it to be included as a package. I am not sure why the other answers talk about PYTHONPATH.
# from application.app.folder.file import func_name


# import abc
from src.abc import is_num_odd

def test_is_num_odd():
    assert is_num_odd(5) == "odd"
    assert is_num_odd(4) == "even"
    assert is_num_odd(0) == "neither odd nor even"
    assert is_num_odd(-1) == "neither odd nor even"