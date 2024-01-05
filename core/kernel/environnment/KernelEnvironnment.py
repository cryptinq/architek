from core.kernel.file.helpers.KeySet import KeySet


class KernelEnvironnment(KeySet):

    def __init__(self, env_values: dict):
        super().__init__(env_values)

