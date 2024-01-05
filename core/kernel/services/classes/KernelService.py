from core.kernel.file.helpers.KeySet import KeySet


class KernelService:

    def __init__(self, name: str):
        self.name = name
        # service_name = str(self).split(" object")[0].replace("<", "")
        # service_name = service_name.split(".")[0] + "." + service_name.split(".")[1] + "." + service_name.split(".")[2]
        # Logger.log("Initializing " + service_name)
        # self.configuration: KeySet = self.resolve_configuration()
        # self.service: ServiceContainer = ServiceContainer
        # self.boot()

    def resolve_configuration(self):
        if self.name not in AppConfiguration.SERVICE_CONFIGURATION:
            return KeySet({})
        return KeySet(AppConfiguration.SERVICE_CONFIGURATION[self.name])

    def boot(self):
        pass