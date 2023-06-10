from core.kernel.interface.KernelInterface import KernelInterface

from core.kernel.configuration.KernelConfiguration import KernelConfiguration
from core.kernel.configuration.interface.KernelConfigurationInterface import KernelConfigurationInterface

from core.kernel.console.KernelConsole import KernelConsole
from core.kernel.console.interface.KernelConsoleInterface import KernelConsoleInterface


class Kernel(KernelInterface):

    def __init__(self, path, console=False):
        super().__init__()
        self.path = path
        self.console_mode = console

    def boot(self):
        self.configuration: KernelConfiguration = self.bootstrap(KernelConfigurationInterface)
        self.console: KernelConsole = self.bootstrap(KernelConsoleInterface)
