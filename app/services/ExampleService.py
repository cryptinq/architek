from core.kernel.services.classes.SingletonService import SingletonService


class ExampleService(SingletonService):

    def __init__(self):
        super().__init__()

    def example_method(self):
        self.console.info("Hello World from ExampleService->example_method() !")
