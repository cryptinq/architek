from core.kernel.interface.KernelInterface import KernelInterface
from core.kernel.console.KernelConsole import KernelConsole
from core.kernel.configuration.KernelConfiguration import KernelConfiguration
from core.kernel.environnment.KernelEnvironnment import KernelEnvironnment
# from core.kernel.services.KernelServiceContainer import KernelServiceContainer


class Base:

    def __init__(self, console: bool = True, orm: bool = True, configuration: bool = True, env: bool = True):
        self.kernel = KernelInterface.instance()
        self.console: KernelConsole = self.kernel.app("console") if console else None
        self.orm = self.kernel.app("orm") if orm else None
        self.configuration: KernelConfiguration = self.kernel.app("configuration") if configuration else None
        self.env: KernelEnvironnment = self.kernel.app("env") if env else None
        self.service_container = None

    def service(self, service_name: str):
        if self.service_container is None: self.service_container = self.kernel.app("service_container")
        return self.service_container.service(service_name)

    def repository(self, entity): return self.orm.get_repository(entity)
