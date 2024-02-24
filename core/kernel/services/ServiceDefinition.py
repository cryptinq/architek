from typing import Optional

from core.kernel.interface.KernelInterface import KernelInterface


class ServiceDefinition:

    def __init__(self, name: str, namespace: str, identifier: str, singleton: bool = False):

        super().__init__()

        self.kernel = KernelInterface.instance()
        self.console = self.kernel.app("console")

        self.name: str = name
        self.namespace: str = namespace
        self.identifier: str = identifier
        self.singleton: bool = singleton

        self.service_implemented: bool = False
        self.service_class = self.resolve_class()

    def resolve_class(self):

        cls = None

        try: cls = self.kernel.resolve_class(f"{self.namespace}.{self.name}", self.name)
        except Exception:

            if "make:service" not in self.kernel.command: self.console.info(
                    f"Service {self.namespace}.{self.name} defined from config/services.yaml is not implemented, "
                    f"consider running 'python console make:service {self.name}' to implement this class"
                )

        if cls is not None: self.service_implemented = True

        return cls

    def is_implemented(self): return self.service_implemented



