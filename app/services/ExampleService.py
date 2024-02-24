from core.kernel.services.SingletonService import SingletonService


class ExampleService(SingletonService):

    def __init__(self):
        super().__init__()
