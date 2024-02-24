from time import time

from core.kernel.environnment.KernelEnvironnment import KernelEnvironnment
from core.kernel.environnment.interface.KernelEnvironnmentInterface import KernelEnvironnmentInterface

from core.kernel.interface.KernelInterface import KernelInterface
from core.kernel.console.interface.KernelCommandInterface import KernelCommandInterface

from core.kernel.configuration.KernelConfiguration import KernelConfiguration
from core.kernel.configuration.interface.KernelConfigurationInterface import KernelConfigurationInterface

from core.kernel.console.KernelConsole import KernelConsole
from core.kernel.console.interface.KernelConsoleInterface import KernelConsoleInterface

from core.orm.ORM import ORM
from core.orm.interface.ORMInterface import ORMInterface

from core.exceptions.interface.KernelExceptionInterface import KernelExceptionInterface


class Kernel(KernelInterface):

    def __init__(self, path, console=False):
        super().__init__(self, path, console)

        if self.verbose(2): KernelConsole.system(f"Kernel::init()\n")

        self.orm = None

        self.configuration: KernelConfiguration = self.bootstrap(KernelConfigurationInterface)
        self.env: KernelEnvironnment = self.bootstrap(KernelEnvironnmentInterface)
        self.console: KernelConsole = self.bootstrap(KernelConsoleInterface)

        self.bootstrap(KernelExceptionInterface)

    def finalize(self):

        if self.verbose(2): KernelConsole.system(f"Kernel::finalize()\n")

        self.orm: ORM = self.bootstrap(ORMInterface)
        self.orm.initialize()

        if self.verbose(0): self.console.success(
            f" -- Kernel initialized successfully in {((time() - self.start_time) * 1000):.2f}ms \n"
        )

        return self

    def boot(self):
        KernelCommandInterface.invoke(self.command)
