import os
import sqlite3
from sqlite3 import Connection

from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.kernel.file.helpers.KeySet import KeySet
from core.orm.driver.ORMDriver import ORMDriver
from core.exceptions.KernelException import KernelException


class SQLiteDriver(ORMDriver):

    def __init__(self, driver_configuration: KeySet):
        super().__init__(driver_configuration)
        self.__cnx = None

    def drop(self):
        database_file = fs.from_root(
            os.path.join(self.configuration.get("path"), self.configuration.get("database"))
        )
        if fs.file_exist(database_file): fs.remove(database_file)
        fs.write(database_file, "")

    def cnx(self):
        if self.__cnx is None: self.__cnx = self.connect()
        return self.__cnx

    def connect(self, dry_run=False):
        err, cnx, path = None, None, os.path.join(self.configuration.get("path"), self.configuration.get("database"))

        try: cnx = sqlite3.connect(fs.from_root(path))
        except sqlite3.Error as e: err = e

        if dry_run and cnx: cnx.close()

        return cnx if not dry_run and isinstance(cnx, Connection) else \
            err if err is not None else isinstance(cnx, Connection)

    def execute(self, statement, params=False, fetch=False):

        cnx, cursor, result, err = self.cnx(), self.cnx().cursor(), None, None

        try:

            if params: cursor.execute(statement, params)
            else: cursor.execute(statement)

            if fetch:
                if fetch == "all": result = cursor.fetchall()
                elif fetch == "one": result = cursor.fetchone()
            else: result = True

            cnx.commit()
        except sqlite3.Error as e:
            err = e
            KernelException(
                "SQLite3SyntaxException",
                f"An error occurred while executing {statement} - {str(e)}"
            )
            cnx.rollback()
        finally:
            cursor.close()

        if self.kernel.verbose(2):
            if isinstance(result, sqlite3.Error): self.kernel.console.system(
                f"SQLiteDriver->execute() \n Statement : {statement}"
                + (f"\n Parameters : {str(params)}" if params else "")
                + f"\n State : ∑cERROR"
                + f"\n Error : {str(err)}"
            )
            else: self.kernel.console.system(
                f"SQLiteDriver->execute() \n Statement : {statement}"
                + (f"\n Parameters : {str(params)}" if params else "")
                + f"\n State : ∑aSUCCESS∑f"
                + f"\n Result : {result}"
            )

        return result if result is not None else False

    def execute_script(self, script, fetch=False):
        cnx, cursor, result, statement = self.cnx(), self.cnx().cursor(), None, None

        try:
            for sql_statement in script.split(";"):
                statement = sql_statement.strip()
                if statement: cursor.execute(statement)

            if fetch:
                if fetch == "all":
                    result = cursor.fetchall()
                elif fetch == "one":
                    result = cursor.fetchone()

            cnx.commit()
        except sqlite3.Error as e:
            KernelException(
                "SQLite3SyntaxException",
                f"An error occurred while executing the script - {str(e)} \n"
                f" SQL Statement : {statement}"
            )
            cnx.rollback()
        finally:
            cursor.close()

        return result if result is not None else True

    def execute_many(self, statement, data, fetch=False):
        cnx, cursor, result = self.cnx(), self.cnx().cursor(), None

        try:
            cursor.executemany(statement, data)

            if fetch:
                if fetch == "all":
                    result = cursor.fetchall()
                elif fetch == "one":
                    result = cursor.fetchone()

            cnx.commit()
        except sqlite3.Error as e:
            KernelException(
                "SQLite3SyntaxException",
                f"An error occurred while executing the statement with data - {str(e)}"
            )
            cnx.rollback()
        finally:
            cursor.close()

        return result if result is not None else True

