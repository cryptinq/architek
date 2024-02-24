from core.kernel.services.ServiceDefinition import ServiceDefinition
from core.kernel.file.helpers.KeySet import KeySet
from core.exceptions.KernelException import KernelException


class KernelServiceContainer:

    def __init__(self):
        self.services: KeySet = KeySet({})

    def register(self, definition: ServiceDefinition):
        if not definition.is_implemented(): return False

        self.services.set(definition.identifier, KeySet({
            "__instance": definition.service_class(),
            "__definition": definition
        }))

    def service(self, identifier: str):

        if not self.services.has_key(identifier): KernelException(
            "InvalidServiceIdentifierException",
            f"Service identifier '{identifier}' does not exist, please check your config/services.yaml"
        )

        return self.services.get(f"{identifier}").get("__instance")


