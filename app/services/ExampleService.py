from core.kernel.services.classes.SingletonService import SingletonService


class ExampleService(SingletonService):

    def example_method(self): self.console.info("Hello World from ExampleService->example_method() !")
