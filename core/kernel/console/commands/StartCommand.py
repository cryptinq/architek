from app.app import App
from core.kernel.console.base.BaseCommand import BaseCommand


class StartCommand(BaseCommand):

    def __init__(self, kernel):
        super().__init__(kernel)

    def invoke(self):
        (App(self.kernel)).boot()
