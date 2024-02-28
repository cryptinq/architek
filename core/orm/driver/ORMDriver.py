from core.exceptions.KernelException import KernelException
from core.kernel.file.helpers.KeySet import KeySet
from core.kernel.Base import Base


class ORMDriver(Base):

    def __init__(self, driver_configuration: KeySet):
        super().__init__(orm=False)
        self.configuration: KeySet = driver_configuration

    def connect(self, dry_run: bool): KernelException(
        "UnimplementedMethodException",
        "Driver method connect() not implemented"
    )

    def execute(self, script, params= False, fetch=False): KernelException(
        "UnimplementedMethodException",
        "Driver method execute() not implemented"
    )

    def execute_many(self, script, data, fetch=False): KernelException(
        "UnimplementedMethodException",
        "Driver method execute_many() not implemented"
    )

    def execute_script(self, script, fetch=False): KernelException(
        "UnimplementedMethodException",
        "Driver method execute_script() not implemented"
    )

    def drop(self): KernelException(
        "UnimplementedMethodException",
        "Driver method drop() not implemented"
    )
