from time import time

from core.kernel.environnment.KernelEnvironnment import KernelEnvironnment
from core.kernel.environnment.interface.KernelEnvironnmentInterface import KernelEnvironnmentInterface
from core.kernel.http.KernelServer import KernelServer
from core.kernel.http.interface.KernelServerInterface import KernelServerInterface

from core.kernel.interface.KernelInterface import KernelInterface
from core.kernel.console.interface.KernelCommandInterface import KernelCommandInterface

from core.kernel.configuration.KernelConfiguration import KernelConfiguration
from core.kernel.configuration.interface.KernelConfigurationInterface import KernelConfigurationInterface

from core.kernel.console.KernelConsole import KernelConsole
from core.kernel.console.interface.KernelConsoleInterface import KernelConsoleInterface

from core.orm.ORM import ORM
from core.orm.interface.ORMInterface import ORMInterface

from core.exceptions.interface.KernelExceptionInterface import KernelExceptionInterface
from core.kernel.services.interface.KernelServiceContainerInterface import KernelServiceContainerInterface


class Kernel(KernelInterface):

    def __init__(self, path, console=False):
        super().__init__(self, path, console)

        if self.verbose(2): KernelConsole.system(f"Kernel::init()\n")

        self.orm = None
        self.http_server = None
        self.service_container = None

        # Register the core apps "configuration", "env", "console"
        self.configuration: KernelConfiguration = self.bootstrap(KernelConfigurationInterface)
        self.env: KernelEnvironnment = self.bootstrap(KernelEnvironnmentInterface)
        self.console: KernelConsole = self.bootstrap(KernelConsoleInterface)

        # Initialize the KernelExceptionInterface too
        self.bootstrap(KernelExceptionInterface)

    def finalize(self):

        if self.verbose(2): KernelConsole.system(f"Kernel::finalize()\n")

        # Check if user wants ORM to be loaded
        use_orm = self.configuration.get("app", "use").get('orm')
        if self.verbose(2): KernelConsole.info(f"ORM status: {'∑cdisabled' if not use_orm else '∑aenabled'}")

        if use_orm:
            # Boot up the ORM if app.use.orm = true
            self.orm: ORM = self.bootstrap(ORMInterface)
            self.orm.initialize()

        # Check if user wants http server to be loaded
        use_http_server = self.configuration.get("app", "use").get('http_server')
        if self.verbose(2): KernelConsole.info(f"HTTP Server status: {'∑cdisabled' if not use_http_server else '∑aenabled'}\n")

        if use_http_server:
            # Boot up the HTTP Server if app.use.http = true
            self.http_server: KernelServer = self.bootstrap(KernelServerInterface)
            self.http_server.start()
            # self.http_server.initialize()

        # Register all the services - core one and app one
        self.service_container = self.bootstrap(KernelServiceContainerInterface)

        if self.verbose(0): self.console.success(
            f" -- Kernel initialized successfully in {((time() - self.start_time) * 1000):.2f}ms \n"
        )

        return self

    def boot(self):

        if self.verbose(2): KernelConsole.system(f"Kernel::boot()\n")

        KernelCommandInterface.invoke(self.command)
