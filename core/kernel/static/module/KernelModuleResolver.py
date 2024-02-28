import importlib
import os

from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.exceptions.KernelException import KernelException


class KernelModuleResolver:

    @staticmethod
    def resolve_class(namespace: str, cls: str):

        try:
            module = importlib.import_module(namespace)
            cls = getattr(module, cls)
        except ModuleNotFoundError as e: KernelException(
            "UnableToResolveClassException",
            f"Could not resolve class {cls} from namespace {namespace} - {str(e)}"
        )

        return cls


    @staticmethod
    def resolve_modules(namespace: str):

        files = fs.list_files(namespace.replace('.', os.sep), [".py"])
        classes_name = [file.replace('.py', '') for file in files]

        classes = []

        for class_name in classes_name:

            try: module = importlib.import_module(f"{namespace}.{class_name}")
            except Exception as e: KernelException(
                "InvalidModuleException",
                f"There was an error loading {namespace}.{class_name} - {str(e)}"
            )

            if not hasattr(module, class_name): KernelException(
                "ModuleResolveException",
                f"Module {namespace}.{class_name} as no attribute {class_name}"
            )

            classes.append(getattr(module, class_name))

        return classes
