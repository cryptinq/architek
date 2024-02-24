from time import time

from core.Kernel import Kernel
from core.kernel.configuration.KernelConfiguration import KernelConfiguration
from core.kernel.console.KernelConsole import KernelConsole
from core.kernel.console.helpers.colors import c
from core.kernel.Base import Base


class BaseCommand(Base):

    def __init__(self):
        super().__init__()
        self.start_time = time()
        if self.kernel.verbose(2): self.console.system(f"{self.__class__.__name__}::invoke() \n")

    def stdout(self, string: str, style="default", new_line=False):
        if new_line: print("")
        self.console.stdout(string, style)

    def exec_time(self): return f"{((time() - self.start_time) * 1000):.2f}"
