import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")


@pytest.fixture()
def dataload():
    print("User profile data is being created")
    return ["Aman", "Giri", "Goswami"]


@pytest.fixture(params=[("Chrome", "Rahul"), ("Firefox", "Aman"), ("IE", "Giri")])
def crossbrowser(request):
    return request.param