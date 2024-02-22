from typing import Optional

from core.Kernel import Kernel
from core.kernel.console.base.BaseCommand import BaseCommand
from core.orm.ORM import ORM
from core.kernel.console.commands.database.DatabaseDropCommand import DatabaseDropCommand
from core.kernel.console.commands.database.DatabaseCreateCommand import DatabaseCreateCommand


class DatabaseRecreateCommand(BaseCommand):

    def __init__(self, kernel: Kernel):
        super().__init__(kernel)
        self.orm: ORM = self.kernel.app("orm")
        self.schemas: Optional[dict] = None

    def invoke(self):

        (DatabaseDropCommand(self.kernel)).invoke()
        print("")
        (DatabaseCreateCommand(self.kernel)).invoke()
