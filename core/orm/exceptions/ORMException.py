from core.Kernel import Kernel
from core.kernel.console.KernelConsole import KernelConsole


class ORMException(Exception):
    """Base Exception for ORM Exceptions"""
    def __init__(self, error):
        self.console: KernelConsole = ((Kernel.instance()).app("console"))
        self.console.error(error)


class InvalidORMDriver(ORMException):
    """Invalid database driver provided"""
    def __init__(self, driver):
        super().__init__(f"Invalid database driver provided ({driver})")


class MissingORMConfiguration(ORMException):
    """Missing ORM configuration"""
    def __init__(self, missing_configurations):
        super().__init__(f"Missing ORM Configuration : {str(missing_configurations)}")
