from core.kernel.configuration.KernelConfiguration import KernelConfiguration
from core.kernel.console.KernelConsole import KernelConsole


class KernelConsoleInterface:

    @staticmethod
    def boot(kernel):
        kernel_interface = KernelConsoleInterface(kernel)
        return kernel_interface.kernel_console

    def __init__(self, kernel):
        self.kernel = kernel
        self.kernel_console = KernelConsole(kernel)
        self.initialize()

    def initialize(self):

        configuration: KernelConfiguration = self.kernel.app("configuration")
        kernel_commands = configuration.get("kernel.console")

        for kernel_command in kernel_commands:
            self.kernel_console.register(kernel_command)