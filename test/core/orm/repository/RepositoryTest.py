import time

from app.common.entity.User import User
from app.common.repository.UserRepository import UserRepository
from core.test.BaseTest import BaseTest


# @architek.test
class RepositoryTest(BaseTest):

    def test_create_user_from_tuple(self):

        key, name, email, password = 1, "Noah Boussard", "ahondev@proton.me", "A!s8B&Kslp"
        user: User = User.from_tuple((key, name, email, password,))

        self.assertEqual(user.id, key)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)
        self.assertEqual(user.password, password)

    def test_get_user_from_id(self):

        key = 1
        user_repository: UserRepository = self.repository(User)
        user: User = user_repository.get_by_id(key)

        self.assertEqual(isinstance(user, User), True)
        self.assertEqual(user.id, key)

    def test_save_user(self):

        user_repository: UserRepository = self.repository(User)
        user: User = User(name="Noah Boussard", email="ahondev@proton", password="A!s8B&Kslp")
        success = user_repository.save(user)

        self.assertEqual(success, True)
