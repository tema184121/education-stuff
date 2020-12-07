from factory.django import DjangoModelFactory
from factory import Sequence

from users.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Sequence(lambda n: 'user{0}@test.com'.format(n))
    is_staff = False
    is_active = True
