from typing import Optional

from core.kernel.console.base.BaseCommand import BaseCommand


class DatabaseRecreateCommand(BaseCommand):

    def __init__(self):
        super().__init__()
        self.schemas: Optional[dict] = None

    def invoke(self):

        self.kernel.invoke("database:drop")
        print("")
        self.kernel.invoke("database:create")
