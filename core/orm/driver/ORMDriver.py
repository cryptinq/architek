from core.exceptions.KernelException import KernelException
from core.kernel.file.helpers.KeySet import KeySet


class ORMDriver:

    def __init__(self, driver_configuration: KeySet):
        self.configuration: KeySet = driver_configuration

    def connect(self, dry_run: bool): raise KernelException(
        "UnimplementedMethodException",
        "Driver method connect() not implemented"
    )
