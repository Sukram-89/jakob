import pytest

def test_one(setup):
    #Detta test kommer köra "setup" funktionen nedan först, sedan testet.
    print("\n Mitt första test")


@pytest.fixture()
def setup():
    print("\n Setting up test")