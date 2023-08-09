import importlib


class CommandInterface:

    def __init__(self, kernel, console, params):
        self.kernel = kernel
        self.console = console
        self.name = params["name"]
        self.description = params["description"] or "No description provided."
        self.namespace = params["namespace"]
        self.clazz = params["class"]
        self.arguments = params["arguments"] or []
        self.dynamic_class = self.import_class()

    def import_class(self):
        try:
            full_namespace = f"{self.namespace}.{self.clazz}"
            module = importlib.import_module(full_namespace)
            clazz = getattr(module, self.clazz)
            return clazz
        except ModuleNotFoundError:
            self.console.error(f"Module <{self.namespace}.{self.clazz}> not found. Please check your app/commands.yaml file.")
            self.kernel.kill()

    def execute(self):
        instance = self.dynamic_class()
        return instance.execute(console=self.console, args=self.arguments)
