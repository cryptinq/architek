from typing import Optional

from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.orm.driver.ORMDriver import ORMDriver


class ORM:

    SCHEMAS_PATH = fs.from_root("database/schema")

    def __init__(self):
        self.driver: Optional[ORMDriver] = None
