from time import time
from datetime import datetime
from typing import Optional

from core.Kernel import Kernel
from core.kernel.console.base.BaseCommand import BaseCommand
from core.orm.ORM import ORM


class DatabaseDropCommand(BaseCommand):

    def __init__(self, kernel: Kernel):
        super().__init__(kernel)
        self.orm: ORM = self.kernel.app("orm")
        self.schemas: Optional[dict] = None

    def invoke(self):
        start_time = time()
        self.orm.driver.drop()
        self.console.success(f"Database dropped successfully in {((time() - start_time) * 1000):.2f}ms")
