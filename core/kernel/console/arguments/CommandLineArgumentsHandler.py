import sys, getopt
from typing import List

from core.Errors import MissingRequiredArgumentException
from core.Logger import Logger
from core.cli.CommandLineArgument import CommandLineArgument


class CommandLineArgumentsHandler:

    arguments = {}

    @staticmethod
    def handle(arguments: List[CommandLineArgument]):

        shorts, longs = CommandLineArgumentsHandler.format_options(arguments)
        CommandLineArgumentsHandler.arguments["__values"] = {}
        opts, args = getopt.getopt(sys.argv[1:], shorts, longs)

        for opt, value in opts:

            if opt not in CommandLineArgumentsHandler.arguments["__shorts"].keys() and \
               opt not in CommandLineArgumentsHandler.arguments["__longs"].keys():
                continue

            arg = CommandLineArgumentsHandler.get_all_args()[opt]
            _value = value if arg.has_value() else None
            CommandLineArgumentsHandler.arguments["__values"][arg.name()] = {
                "value": _value,
                "object": arg
            }

        CommandLineArgumentsHandler.check_required(arguments)
        Logger.log(f"Initialized §9{len(CommandLineArgumentsHandler.arguments['__values'])} §fcommand line argument" + ("s" if len(CommandLineArgumentsHandler.arguments['__values']) > 1 else ""))

    @staticmethod
    def format_options(arguments: List[CommandLineArgument]):

        CommandLineArgumentsHandler.arguments["__shorts"] = {}
        CommandLineArgumentsHandler.arguments["__longs"] = {}

        shorts = ""
        longs = []
        for arg in arguments:
            shorts += arg.short() if not arg.has_value() else f"{arg.short()}:"
            longs.append(arg.long() if not arg.has_value() else f"{arg.long()}=")
            CommandLineArgumentsHandler.arguments["__shorts"][f"-{arg.short()}"] = arg
            CommandLineArgumentsHandler.arguments["__longs"][f"--{arg.long()}"] = arg

        return shorts, longs

    @staticmethod
    def get_all_args():
        return CommandLineArgumentsHandler.arguments["__longs"] | CommandLineArgumentsHandler.arguments["__shorts"]

    @staticmethod
    def get(name):
        if name not in CommandLineArgumentsHandler.arguments["__values"].keys():
            return False
        if CommandLineArgumentsHandler.arguments["__values"][name]["value"] is None:
            return True
        return CommandLineArgumentsHandler.arguments["__values"][name]["value"]

    @staticmethod
    def check_required(initial_arguments):

        _values = CommandLineArgumentsHandler.arguments["__values"]
        for arg in initial_arguments:
            if not arg.required():
                continue
            if arg.name() in _values.keys():
                continue
            raise MissingRequiredArgumentException(arg.name())
