from core.exceptions.KernelException import KernelException


class KernelCommandInterface:

    COMMANDS = {}
    KERNEL = None
    
    @staticmethod
    def commands():

        # sort alphabetically
        commands = list(KernelCommandInterface.COMMANDS.keys())
        commands.sort()
        _commands = []
        for _command in commands:
            _commands.append(KernelCommandInterface.COMMANDS[_command])

        group_commands = list(filter(lambda _command: len(_command["name"].split(":")) == 2, _commands))
        solo_commands = list(filter(lambda _command: len(_command["name"].split(":")) == 1, _commands))

        return solo_commands + group_commands

    @staticmethod
    def register(command):
        KernelCommandInterface.COMMANDS[command["name"]] = command

    @staticmethod
    def resolve(command: str):
        list_keys = list(KernelCommandInterface.COMMANDS.keys())
        if command in list_keys: return KernelCommandInterface.COMMANDS[command]
        if command.startswith("-"): return KernelCommandInterface.COMMANDS["architek"]
        KernelException("UnknownCommandException", f"Unknow command '{command}'")

    @staticmethod
    def invoke(command: str):
        command = KernelCommandInterface.resolve(command)
        command_class = command["namespace"] + "." + command["class"]

        try: module = __import__(command_class, fromlist=[command['class']])
        except ModuleNotFoundError: KernelException(
            "InvalidCommandNamespaceException",
            f"Invalid namespace '{command['namespace']}' for command '{command['name']}'"
        )
        except ImportError: KernelException(
            "InvalidCommandClassException",
            f"Invalid class '{command['class']} in namespace '{command['namespace']}' for command '{command['name']}'"
        )

        class_instance = getattr(module, command['class'])()
        return class_instance.invoke()
