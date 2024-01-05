class CommandLineArgument:

    def __init__(self, short: str, long: str, required: bool, has_value: bool):
        self._name: str = long
        self._short: str = short
        self._long: str = long
        self._required: bool = required
        self._has_value: bool = has_value

    def name(self):
        return self._name

    def short(self):
        return self._short

    def long(self):
        return self._long

    def required(self):
        return self._required

    def has_value(self):
        return self._has_value
