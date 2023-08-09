from core.kernel.console.commands.BaseCommand import BaseCommand


class DatabaseCreateCommand(BaseCommand):

    def execute(self, console, args):
        console.info("Creating database...")
