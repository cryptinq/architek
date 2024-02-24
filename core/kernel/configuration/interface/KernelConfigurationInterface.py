import os, json, yaml

from core.kernel.configuration.KernelConfiguration import KernelConfiguration

from core.kernel.decorators.ArchitekDecorator import architek


class KernelConfigurationInterface:

    @staticmethod
    @architek.boot
    def boot(kernel):
        kernel_interface = KernelConfigurationInterface(kernel)
        return kernel_interface.kernel_configuration

    def __init__(self, kernel):
        self.kernel = kernel
        self.kernel_configuration = KernelConfiguration()
        self.initialize()

    def initialize(self):

        app_configurations = [
            "app", "app.logs",
            "app.services", "app.commands", "app.database",
        ]

        kernel_configurations = [
            "console", "framework", "services"
        ]

        for app_config in app_configurations:
            folder_abs_path = os.path.abspath(os.path.dirname(__file__))
            root_abs_path = os.path.abspath(os.path.join(folder_abs_path, "..", "..", "..", ".."))
            with open(os.path.join(root_abs_path, "config", *app_config.split(".")) + ".yaml") as file:
                data = yaml.safe_load(file.read())
                self.kernel_configuration.add(app_config, data[list(data.keys())[0]])

        for kernel_config in kernel_configurations:
            folder_abs_path = os.path.abspath(os.path.dirname(__file__))
            root_abs_path = os.path.abspath(os.path.join(folder_abs_path, "..", "..", ".."))
            with open(os.path.join(root_abs_path, "config", *kernel_config.split(".")) + ".yaml") as file:
                data = yaml.safe_load(file.read())
                self.kernel_configuration.add(f"kernel.{kernel_config}", data[list(data.keys())[0]], kernel=True)
