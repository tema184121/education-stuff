import pytest
from pytest_factoryboy import register

from app.test_client import DRFClient
from users.tests.factories import UserFactory

register(UserFactory)


@pytest.fixture
def api():
    return DRFClient()
