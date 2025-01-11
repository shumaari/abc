# # some_file.py
# import sys
# # caution: path[0] is reserved for script path (or '' in REPL)
# sys.path.insert(1, '/path/to/application/app/folder')
# import file

# Just make sure folder also contains an __init__.py. This allows it to be included as a package. I am not sure why the other answers talk about PYTHONPATH.
# from application.app.folder.file import func_name


import pytest
# import abc
from src.abc import is_num_odd, is_multiple_of_three, reverse_string
import time

def test_is_num_odd():
    assert is_num_odd(5) == "odd"
    assert is_num_odd(4) == "even"
    assert is_num_odd(0) == "neither odd nor even"
    assert is_num_odd(-1) == "neither odd nor even"


# Using pytest.mark to group certain tests together.
# Here command "pytest -vm ft1_func_3" can be used to run only tests with this marker.
@pytest.mark.ft1_func_3
def test_is_multiple_of_three():
    # Using time.sleep to simulate a long running test.
    # Here command "pytest -n 2" can be used run long tests in parallel.
    # Here command "pytest -k test_is_multiple_of_three" can be used to run only tests with this name.
    # Here command "pytest -vm ft1_func_3 -n 4" can be used to run only tests with this marker in parallel.
    # Here command "pytest -x" can be used to stop testing after first failure.
    # Here command "pytest --maxfail=2" can be used to stop testing after 2 failures.

    time.sleep(5)
    assert is_multiple_of_three(3) == "yes"
    assert is_multiple_of_three(9) == "yes"
    assert is_multiple_of_three(10) == "no"
    assert is_multiple_of_three(0) == "yes"
    assert is_multiple_of_three(-3) == "yes"
    assert is_multiple_of_three(-4) == "no"

    
# @pytest.mark.ft1_func_3
# Using pytest.mark.parametrize to run multiple tests with different inputs.
@pytest.mark.parametrize("input_value, expected", 
                           [("hello", "olleh"),
                            ("12345", "54321"),
                            ("a", "a")])
def test_reverse_string(input_value, expected):
    # assert reverse_string("world") == "dlrow"
    assert reverse_string(input_value) == expected

@pytest.mark.ft1_func_3
def test_reverse_string_error():
    time.sleep(5)
    with pytest.raises(ValueError):
        reverse_string(123)


@pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.parametrize("input_value, expected", 
                           [(3, 9),
                            (4, 16),
                            (-1, 1),])
def test_sqaure_num(input_value, expected):
    assert square_num(input_value) == expected