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


class Kernel(KernelInterface):

    def __init__(self, path, console=False):
        super().__init__(self, path, console)

        self.orm = None

        self.configuration: KernelConfiguration = self.bootstrap(KernelConfigurationInterface)
        self.environnment: KernelEnvironnment = self.bootstrap(KernelEnvironnmentInterface)
        self.console: KernelConsole = self.bootstrap(KernelConsoleInterface)

    def finalize(self):

        self.orm: ORM = self.bootstrap(ORMInterface)

        return self

    def boot(self):
        KernelCommandInterface.invoke(self.command)
