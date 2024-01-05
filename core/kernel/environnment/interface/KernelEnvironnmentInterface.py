from dotenv import dotenv_values

from core.exceptions.KernelException import KernelException
from core.kernel.console.KernelConsole import KernelConsole
from core.kernel.decorators.KernelDecorators import KernelDecorator
from core.kernel.environnment.KernelEnvironnment import KernelEnvironnment
from core.kernel.file.helpers.FileSystem import FileSystem


class KernelEnvironnmentInterface:

    @staticmethod
    @KernelDecorator.boot
    def boot(kernel):
        kernel_interface = KernelEnvironnmentInterface(kernel)
        return kernel_interface

    def __init__(self, kernel):
        self.kernel = kernel
        self.kernel_environnment = KernelEnvironnment({})
        self.initialize()

    def initialize(self):

        env_file = FileSystem.from_root(".env")

        if not FileSystem.file_exist(env_file): raise KernelException(
            "NonexistentEnvFileException",
            "File .env does not exist, please create a .env file first"
        )

        env_values = dict(dotenv_values(env_file))

        for key in env_values.keys():
            self.kernel_environnment.set(key, env_values[key])

        if self.kernel.verbose(0):
            KernelConsole.info(f"Loaded {len(self.kernel_environnment.keys())} environnment variables")


