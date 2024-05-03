# Any Pytest file should start with test_
# pytest methods name should start or end with test
# Code should be wrapped inside the method
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail 
def test_GreetCreditCard():
    print("Good Morning")

def test_Crossbrowser(crossbrowser):
    print(crossbrowser)