from core.kernel.configuration.KernelConfiguration import KernelConfiguration
from core.kernel.console.KernelConsole import KernelConsole


class KernelConsoleInterface:

    @staticmethod
    def boot(kernel):
        kernel_interface = KernelConsoleInterface(kernel)
        return kernel_interface.kernel_console

    def __init__(self, kernel):
        self.kernel = kernel
        self.kernel_console = KernelConsole()
        self.initialize()

    def initialize(self):
        configuration: KernelConfiguration = self.kernel.app("configuration")
        kernel_commands = configuration.get("kernel.console")
        self.kernel_console.info("Loading kernel console commands...")