from app.app import App
from core.kernel.console.base.BaseCommand import BaseCommand


class StartCommand(BaseCommand):

    def invoke(self): (App()).boot()
