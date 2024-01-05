import sqlite3
from sqlite3 import Connection

from core.kernel.file.helpers.FileSystem import FileSystem
from core.kernel.file.helpers.KeySet import KeySet
from core.orm.driver.ORMDriver import ORMDriver


class SQLiteDriver(ORMDriver):

    def __init__(self, driver_configuration: KeySet):
        super().__init__(driver_configuration)

    def connect(self, dry_run=False):
        err, cnx, path = None, None, self.configuration.get("path") + "/" + self.configuration.get("database")

        try: cnx = sqlite3.connect(FileSystem.from_root(path))
        except sqlite3.Error as e: err = e

        if dry_run and cnx: cnx.close()

        return cnx if not dry_run and isinstance(cnx, Connection) else \
            err if err is not None else isinstance(cnx, Connection)

