from core.kernel.decorators.ArchitekDecorator import architek
from core.kernel.services.KernelServiceContainer import KernelServiceContainer
from core.exceptions.KernelException import KernelException
from core.kernel.services.ServiceDefinition import ServiceDefinition
from core.kernel.file.helpers.KeySet import KeySet


class KernelServiceContainerInterface:

    REQUIRED_KEY = ["namespace", "identifier"]

    @staticmethod
    @architek.boot
    def boot(kernel):
        kernel_interface = KernelServiceContainerInterface(kernel)
        return kernel_interface.kernel_service_container

    def __init__(self, kernel):
        self.kernel = kernel
        self.kernel_service_container = KernelServiceContainer()

        self.service_configurations: KeySet = KeySet({})
        self.service_definitions: KeySet = KeySet({})

        self.initialize()

    def initialize(self):

        # first, parse config & resolve classes

        keys = ["kernel", "app"]

        for key in keys:

            configuration = self.kernel.configuration.get(f"{key}.services")
            self.service_configurations.set(key, configuration)

            for service_name in configuration.keys():
                self.service_definitions.set(
                    service_name,
                    self.get_service_definition(key, service_name)
                )

        # then autoload the services, and put them on the container, access from identifier

        for service_name in self.service_definitions.keys():
            definition = self.service_definitions.get(service_name)
            self.kernel_service_container.register(definition)

    def get_service_definition(self, configuration: str, service_name: str) -> ServiceDefinition:

        configuration = self.service_configurations.get(configuration)
        service = configuration.get(service_name)

        if not service.has_keys(self.REQUIRED_KEY): KernelException(
            "InvalidServiceConfigurationException",
            f"Missing required key: {service.missing_keys(self.REQUIRED_KEY)} for service '{service}'"
        )

        return ServiceDefinition(
            service_name, service.get("namespace"), service.get("identifier"),
            service.get("singleton") if service.has_key("singleton") else False
        )
