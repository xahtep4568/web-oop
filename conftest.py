import pytest


@pytest.fixture
def client(api):
    return api.test_session()
