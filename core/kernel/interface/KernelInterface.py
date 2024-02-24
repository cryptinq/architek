import sys
import time

from core.kernel.console.KernelConsole import KernelConsole


class KernelInterface:

    _instance = None
    @staticmethod
    def instance(): return KernelInterface._instance

    def __init__(self, kernel, path, console):

        self.start_time = time.time()

        self.kernel = kernel
        self.command = sys.argv[1] if len(sys.argv) > 1 else "architek"
        self.path = path
        self.console_mode = console
        self.verbosity_level = 0 if "-v" in sys.argv else (1 if "-vv" in sys.argv else (2 if "-vvv" in sys.argv else -1))
        KernelInterface._instance = kernel

        if self.verbose(0): KernelConsole.info(f"Verbosity level : {self.verbosity_level} \n")

    def app(self, name):
        module = getattr(self, name, None)

        if module is None: self.kernel.app("console").error(
            "UnavailableKernelModule | "
            f"UnavailableKernelModule - Unable to find module '{name}' - maybe it's not initialized yet? \n"
        ); raise Exception

        return module if module is not None else None

    def bootstrap(self, interface): return interface.boot(self)

    def verbose(self, verbose_level=0): return self.verbosity_level >= verbose_level

    @classmethod
    def invoke(cls, command):
        from core.kernel.console.interface.KernelCommandInterface import KernelCommandInterface
        return KernelCommandInterface.invoke(command)

    @classmethod
    def resolve_modules(cls, namespace):
        from core.kernel.static.module.KernelModuleResolver import KernelModuleResolver
        return KernelModuleResolver.resolve_modules(namespace)



