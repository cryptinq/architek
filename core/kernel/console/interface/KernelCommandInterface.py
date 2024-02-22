from core.exceptions.KernelException import KernelException


class KernelCommandInterface:

    COMMANDS = {}
    KERNEL = None
    
    @staticmethod
    def commands():
        commands = list(KernelCommandInterface.COMMANDS.keys())
        commands.sort()
        _commands = []
        for _command in commands:
            _commands.append(KernelCommandInterface.COMMANDS[_command])
        return _commands

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
        module = __import__(command_class, fromlist=[command['class']])
        class_instance = getattr(module, command['class'])(KernelCommandInterface.KERNEL)
        return class_instance.invoke()
