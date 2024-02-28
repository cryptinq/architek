from core.kernel.console.base.BaseCommand import BaseCommand
from core.kernel.console.interface.KernelCommandInterface import KernelCommandInterface


class HelpCommand(BaseCommand):

    def __init__(self):
        super().__init__()

        self.last_command = None
        self.is_group = False
        self.start_groups = False

    def invoke(self):

        self.stdout("∑7━━━━━━━━━━━━━━━━━━━━[ ∑9Help ∑7]━━━━━━━━━━━━━━━━━━━━")
        self.stdout("")
        for command in KernelCommandInterface.commands():

            command = KernelCommandInterface.resolve(command["name"])

            # hide architek command
            if command["name"] == "architek": continue

            # ignore first command
            if self.last_command is None: self.last_command = command["name"]

            # if current command prefix is same as last command
            if len(command["name"].split(":")) == 2:
                if self.last_command.split(":")[0] == command["name"].split(":")[0]:
                    if not self.is_group: self.is_group = True  # start a group

            # if current command prefix is not same as last command
            if self.last_command.split(":")[0] != command["name"].split(":")[0]:
                if not self.is_group:
                    if len(command["name"].split(":")) == 2: self.start_groups = True
                    if self.start_groups: print("")
                if self.is_group: self.is_group = False; print("")  # end group and print newline

            self.stdout(f"∑9{command['name']} - ∑7{command['description']}")

            self.last_command = command["name"]
