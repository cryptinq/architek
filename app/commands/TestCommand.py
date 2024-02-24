from core.kernel.console.base.BaseCommand import BaseCommand


class TestCommand(BaseCommand):

    def invoke(self):
        self.console.info("Called TestCommand")
