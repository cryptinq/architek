import importlib


class KernelModuleResolver:

    @staticmethod
    def resolve_class(namespace: str, cls: str):
        module = importlib.import_module(namespace)
        return getattr(module, cls)