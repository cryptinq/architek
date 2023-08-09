import os


class EnvironmentProvider:

    def __init__(self, kernel):
        self.kernel = kernel
        self.id = "env"

    def initialize(self):
        env_file = os.path.join(self.kernel.path, ".env")

        if not os.path.isfile(env_file):
            with open(env_file, "w") as file:
                file.write("")

        with open(env_file) as file:
            for line in file.readlines():
                if "=" in line:
                    key, value = line.split("=")
                    if "'" in value or '"' in value:
                        value = value.replace("'", "")
                        value = value.replace('"', "")
                    value = value.replace("\n", "")
                    os.environ[key] = value
