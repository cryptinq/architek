import os

from core.kernel.interface.KernelInterface import KernelInterface

from core.kernel.configuration.KernelConfiguration import KernelConfiguration
from core.kernel.configuration.interface.KernelConfigurationInterface import KernelConfigurationInterface

from core.kernel.console.KernelConsole import KernelConsole
from core.kernel.console.interface.KernelConsoleInterface import KernelConsoleInterface

from core.kernel.providers.KernelProvider import KernelProvider
from core.kernel.providers.interface.KernelProviderInterface import KernelProviderInterface


class Kernel(KernelInterface):

    def __init__(self, path, console=False):
        super().__init__()
        self.path = path
        self.console_mode = console

    def boot(self):

        # This is the boot sequence of the application, including the core and then the app

        # First load the different configuration files into the system (user config & core config)
        self.configuration: KernelConfiguration = self.bootstrap(KernelConfigurationInterface)

        # Then load the console interface (manage IO, register commands, etc.)
        self.console: KernelConsole = self.bootstrap(KernelConsoleInterface)

        # Then load the different core providers (environment, etc.)
        self.provider: KernelProvider = self.bootstrap(KernelProviderInterface)

        # Then load the different core services (logger, argument parser, db connection, etc.)
        # self.bootstrap(KernelServiceInterface)

        # Intialize the ORM (entities & repositories)
        # self.bootstrap(KernelOrmInterface)

        # Intialize the custom app services
        # self.bootstrap(AppServiceInterface)

        # Finally, load the app
        # self.bootstrap(AppInterface)
