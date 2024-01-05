from core.kernel.console.base.BaseCommand import BaseCommand
from core.kernel.console.interface.KernelCommandInterface import KernelCommandInterface


class HelpCommand(BaseCommand):

    def __init__(self, kernel):
        super().__init__(kernel)

    def invoke(self):

        self.stdout("∑7━━━━━━━━━━━━━━━━━━━━[ ∑aHelp ∑7]━━━━━━━━━━━━━━━━━━━━")
        self.stdout("")
        for command in KernelCommandInterface.commands():
            command = KernelCommandInterface.resolve(command["name"])
            self.stdout(f"∑a{command['name']} - ∑7{command['description']}")
