from core.kernel.Base import Base
from app.services.ExampleService import ExampleService


class App(Base):

    def __init__(self):
        super().__init__()
        self.example_service: ExampleService = self.service("app.example")

    def boot(self):

        self.console.info('Booting Application')
        self.example_service.example_method()
