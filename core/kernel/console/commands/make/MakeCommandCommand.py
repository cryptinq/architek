import sys

from core.kernel.console.base.BaseCommand import BaseCommand
from core.kernel.file.helpers.FileSystem import FileSystem as fs
from core.exceptions.KernelException import KernelException


class MakeCommandCommand(BaseCommand):

    def invoke(self):

        force = "-f" in sys.argv or "--force" in sys.argv

        if len(sys.argv) == 2: KernelException(
            "MissingRequiredArgument",
            "Argument 'name' is missing, usage : 'python console make:command ExampleCommand'"
        )

        command_name = sys.argv[2]

        command_path = fs.from_root(fs.join("app", "commands", f"{command_name}.py"))
        command_stub_path = fs.from_root(fs.join("core", "kernel", "stub", "command", "command.stub"))

        if fs.file_exist(command_path) and not force: KernelException(
            "CommandAlreadyExistsException",
            f"Command '{command_name}' already exist, use --force to override"
        )

        content = fs.content(command_stub_path)

        replacements = {"%COMMAND_NAME%": command_name}
        for replacement in replacements.keys(): content = content.replace(replacement, replacements[replacement])

        fs.write(command_path, content)

        self.console.info(f"Created command '{command_name}' at {command_path}")

        print("")

        self.console.success(
            f"Command successfully generated in {self.exec_time()}ms, "
            f"now you should configure it at config/app/commands.yaml"
        )
