from core.kernel.configuration.KernelConfiguration import KernelConfiguration
from core.kernel.console.KernelConsole import KernelConsole
from core.kernel.console.interface.KernelCommandInterface import KernelCommandInterface
from core.kernel.decorators.ArchitekDecorator import architek


class KernelConsoleInterface:

    @staticmethod
    @architek.boot
    def boot(kernel):
        kernel_interface = KernelConsoleInterface(kernel)
        return kernel_interface.kernel_console

    def __init__(self, kernel):
        self.kernel = kernel
        self.kernel_console = KernelConsole()
        self.initialize()

    def initialize(self):
        KernelCommandInterface.KERNEL = self.kernel
        configuration: KernelConfiguration = self.kernel.app("configuration")

        kernel_commands = configuration.get("kernel.console")
        for kernel_command in kernel_commands:
            KernelCommandInterface.register(kernel_command)

        app_commands = configuration.get("app.commands")
        for app_command in app_commands:
            KernelCommandInterface.register(app_command)
