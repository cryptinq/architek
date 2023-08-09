from core.kernel.console.helpers.colors import c
from core.kernel.console.interface.CommandInterface import CommandInterface as Command


class KernelConsole:

    def __init__(self, kernel):
        self._kernel = kernel
        self._commands = {}

    def register(self, command):
        self._commands[command["name"]] = Command(self._kernel, self, command)

    def info(self, message):
        print(c(f"§b[INFO] {message}"))

    def warning(self, message):
        print(c(f"§e[WARNING] {message}"))

    def error(self, message):
        print(c(f"§c[ERROR] {message}"))

    def success(self, message):
        print(c(f"§a[SUCCESS] {message}"))
