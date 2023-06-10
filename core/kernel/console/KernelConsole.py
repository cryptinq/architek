from core.kernel.console.helpers.colors import c


class KernelConsole:

    def info(self, message):
        print(c(f"§b[INFO] {message}"))

    def warning(self, message):
        print(c(f"§e[WARNING] {message}"))

    def error(self, message):
        print(c(f"§c[ERROR] {message}"))

    def success(self, message):
        print(c(f"§a[SUCCESS] {message}"))
