import sys

from core.kernel.console.base.BaseCommand import BaseCommand
from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.exceptions.KernelException import KernelException


class MakeServiceCommand(BaseCommand):

    service_type = {
        "base": {
            "class": "BaseService",
            "import": "from core.kernel.services.BaseService import BaseService"
        },
        "singleton": {
            "class": "SingletonService",
            "import": "from core.kernel.services.classes.SingletonService import SingletonService"
        }
    }

    def invoke(self):

        force = "-f" in sys.argv or "--force" in sys.argv
        singleton = "-s" in sys.argv or "--singleton" in sys.argv

        if len(sys.argv) == 2: KernelException(
            "MissingRequiredArgument",
            "Argument 'name' is missing, usage : 'python console make:service ExampleService [-f | -s]'"
        )

        service_name = sys.argv[2]
        service_type = "base" if not singleton else "singleton"

        service_path = fs.from_root(fs.join("app", "services", f"{service_name}.py"))
        service_stub_path = fs.from_root(fs.join("core", "kernel", "stub", "service", "service.stub"))

        if fs.file_exist(service_path) and not force: KernelException(
            "CommandAlreadyExistsException",
            f"Command '{service_name}' already exist, use --force to override"
        )

        content = fs.content(service_stub_path)

        replacements = {
            "%SERVICE_NAME%": service_name,
            "%SERVICE_TYPE%": self.service_type[service_type]["class"],
            "%SERVICE_TYPE_IMPORT%": self.service_type[service_type]["import"]
        }
        for replacement in replacements.keys(): content = content.replace(replacement, replacements[replacement])

        fs.write(service_path, content)

        self.console.info(f"Created service '{service_name}' at {service_path}")

        print("")

        self.console.success(
            f"Service successfully generated in {self.exec_time()}ms, "
            f"now you should configure it at config/app/services.yaml"
        )
