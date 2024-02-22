import sqlite3

from core.exceptions.KernelException import KernelException
from core.kernel.configuration.KernelConfiguration import KernelConfiguration
from core.kernel.console.KernelConsole import KernelConsole
from core.kernel.decorators.KernelDecorators import KernelDecorator
from core.orm.ORM import ORM
from core.orm.driver.ORMDriver import ORMDriver
from core.orm.driver.ORMDriverResolver import ORMDriverResolver


class ORMInterface:

    @staticmethod
    @KernelDecorator.boot
    def boot(kernel):
        orm_interface = ORMInterface(kernel)
        return orm_interface.orm

    def __init__(self, kernel):
        self.kernel = kernel
        self.orm = ORM()
        self.initialize()

    def initialize(self):

        configuration: KernelConfiguration = self.kernel.app("configuration")
        console: KernelConsole = self.kernel.app("console")

        driver = configuration.get("app.database", "driver")
        driver_configuration = configuration.get("app.database", driver)

        orm_driver: ORMDriver = ORMDriverResolver.resolve(driver, driver_configuration)
        self.orm.driver = orm_driver

        if self.kernel.verbose(0): console.info(f"ORMDriver : {driver}")

        connect = orm_driver.connect(dry_run=True)
        if isinstance(connect, sqlite3.Error): KernelException(
            "SQLConnectionException",
            f"Unable to connect to SQL database ({driver}) -> {str(connect).capitalize()}"
        )

        if self.kernel.verbose(0): console.info("Database connection : OK")
