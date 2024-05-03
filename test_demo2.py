# Any Pytest file should start with test_
# pytest methods name should start or end with test
# Code should be wrapped inside the method only
# Method name should have the sense
# -k stands for method names execution, -s logs in output, -v stands for more meta data
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip test with @pytest.mark.skip
# @pytest.mark.xfail : It will execute operations but it will not show pass/fail status in test reports
# fixtures are used as setup and tear methods for test  cases- conftest file to generalise fixtures and make it available to all the test cases
# data driven and parameterisation can be done with return statements in list format
# When you define fixture scope to class only, it will run once before class is initiated and after the class

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because String not matched"


def test_SecondProgramCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not matched"