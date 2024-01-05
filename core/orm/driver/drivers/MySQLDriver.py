from core.kernel.file.helpers.KeySet import KeySet
from core.orm.driver.ORMDriver import ORMDriver


class MySQLDriver(ORMDriver):

    def __init__(self, driver_configuration: KeySet):
        super().__init__(driver_configuration)
