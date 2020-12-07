import pytest

pytestmark = [pytest.mark.django_db]


def test_api_token(api, user):
    user.set_password('12345')
    user.save()

    response = api.post('/api/token/', {'username': user.username, 'password': '12345'}, format='json')

    assert 'access' in response.json().keys()
    assert 'refresh' in response.json().keys()
