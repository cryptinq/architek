from core.kernel.console.base.BaseCommand import BaseCommand


class ExampleCommand(BaseCommand):

    def invoke(self):

        self.console.info("Hello World!")
