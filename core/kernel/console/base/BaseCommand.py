from core.Kernel import Kernel
from core.kernel.configuration.KernelConfiguration import KernelConfiguration
from core.kernel.console.KernelConsole import KernelConsole
from core.kernel.console.helpers.colors import c


class BaseCommand:

    def __init__(self, kernel: Kernel):
        self.kernel: Kernel = kernel
        self.console: KernelConsole = self.kernel.app("console")
        self.configuration: KernelConfiguration = self.kernel.app("configuration")
        if self.kernel.verbose(0): self.console.info(f"Invoking {self.__class__.__name__}")

    def stdout(self, string: str, style="default", new_line=False):
        if new_line: print("")
        self.console.stdout(string, style)
