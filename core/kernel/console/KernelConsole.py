import inspect, json
from core.kernel.console.helpers.colors import c


class KernelConsole:

    def __init__(self):
        self.styles = {
            "default": self.default,
            "info": self.info,
            "success": self.success,
            "error": self.error
        }

    @classmethod
    def stdout(cls, message, style="default"): cls().styles[style](message)

    @classmethod
    def default(cls, message): print(c(message))

    @classmethod
    def info(cls, message): print(c("∑9.∑f INFO ") + "    | " + c(cls.format(message)))

    @classmethod
    def warning(cls, message): print(c("∑e.∑f WARNING ") + " | " + c(cls.format(message)))

    @classmethod
    def error(cls, message): print(c("∑c.∑f ERROR ") + "   | " + c(cls.format(message)))

    @classmethod
    def success(cls, message): print(c("∑a. SUCCESS ") + " | " + c(cls.format(message)))

    @classmethod
    def system(cls, message): print(c("∑5. SYSTEM ") + "  | " + c(cls.format(message)))

    @classmethod
    def format(cls, message: str) -> str: return message.replace("\n", f"\n {' ' * 8} | ")

    @classmethod
    def debug(cls, value):

        frame = inspect.currentframe().f_back
        file = frame.f_code.co_filename
        line = frame.f_lineno
        caller = frame.f_globals['__name__']
        method = frame.f_code.co_name
        caller = caller + "::__" + method + "()"

        value = json.dumps(value, indent=1)

        print(c(f"∑d[DEBUG] in {file} at line {line} \n> {caller} \n"))
        print(c(f"∑d{value}"))
