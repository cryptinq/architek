from core.kernel.Base import Base

from app.common.entity.User import User
from app.common.repository import UserRepository
from app.services.ExampleService import ExampleService


class App(Base):

    def __init__(self):
        super().__init__()
        self.example_service: ExampleService = self.service("app.example")

    def boot(self):

        self.console.info('Booting Application')

        self.example_service.example_method()

        user_repository: UserRepository = self.repository(User)

        for index in range(1, 11):
            user: User = user_repository.get_by_id(index)
            self.console.info(f"User #{index} - {str(user)}")

