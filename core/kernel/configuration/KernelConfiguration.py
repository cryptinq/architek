from core.kernel.file.helpers.KeySet import KeySet


class KernelConfiguration:

    def __init__(self):
        self.configurations = {"app": {}, "kernel": {}}

    def add(self, namespace, data, kernel=False):
        if kernel:
            self.configurations["kernel"][namespace] = data
        else:
            self.configurations["app"][namespace] = data

    def get(self, configuration: str, path=""):

        _base = self.configurations["kernel"] \
            if configuration.startswith("kernel") \
            else self.configurations["app"]
        _configuration = _base[configuration]

        keys = path.split(".")

        if path == "":
            return KeySet(_configuration) \
                if isinstance(_configuration, dict) \
                else _configuration

        if len(keys) == 1:
            return KeySet(_configuration[path]) \
                if isinstance(_configuration[path], dict) \
                else _configuration[path]

        value = _configuration
        for key in keys:
            value = value[key]

        return KeySet(value)

