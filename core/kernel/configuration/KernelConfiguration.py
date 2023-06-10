class KernelConfiguration:

    def __init__(self):
        self.configurations = {"app": {}, "kernel": {}}

    def add(self, namespace, data, kernel=False):
        if kernel:
            self.configurations["kernel"][namespace] = data
        else:
            self.configurations["app"][namespace] = data

    def get(self, configuration, path=""):

        _base = self.configurations["kernel"] \
            if configuration.startswith("kernel") \
            else self.configurations["app"]
        _configuration = _base[configuration]

        keys = path.split(".")
        if path == "":
            return _configuration
        if len(keys) == 1:
            return _configuration[path]

        value = _configuration
        for key in keys:
            value = value[key]

        return value

