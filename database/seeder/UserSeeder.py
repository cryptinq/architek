from app.common.entity.User import User
from core.kernel.factory.BaseSeeder import BaseSeeder


class UserSeeder(BaseSeeder):

    def __init__(self): super().__init__(User)

    def run(self):

        entities = self.factory.create({
            "name": self.faker().name,
            "email": self.faker().email,
            "password": self.faker().password
        }, 10)

        return self.factory.persist(entities)
