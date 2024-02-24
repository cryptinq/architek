from core.kernel.services.classes.KernelService import KernelService


class LoggingService:

    # appName = Configuration.get("appName")
    # logDir = os.path.join(os.path.dirname(__file__), "..", Configuration.get("logFolder"))
    # logFile = os.path.join(logDir, f"{date.today()}.log")

    @staticmethod
    def log(message, title=None, format_traceback=False):
        pass
        # if format_traceback:
        #     traceback_lines = message.splitlines()
        #     formatted_traceback_lines = [traceback_lines[0]] + [f"[{Logger.appName}] {line}" for line in traceback_lines[1:]]
        #     message = "\n".join(formatted_traceback_lines)
        #
        # if Configuration.get("appEnvironment") == "development":
        #
        #     if not os.path.exists(Logger.logDir):
        #         os.mkdir(Logger.logDir)
        #
        #     with open(Logger.logFile, "a+") as file:
        #         _date = datetime.now().strftime("%H:%M:%S")
        #         _log = f"[{_date}]" + f" {message}" + "\n"
        #         file.write(_log)
        #
        # print(f"[{Logger.appName}]", message)

    @staticmethod
    def error(message, format_traceback=False):
        pass
        # if Configuration.get("appEnvironment") == "development":
        #     if not os.path.exists(Logger.logDir):
        #         os.mkdir(Logger.logDir)
        #
        #     if format_traceback:
        #         traceback_lines = message.splitlines()
        #         formatted_traceback_lines = [traceback_lines[0]] + [f"[{Logger.appName}] {line}" for line in traceback_lines[1:]]
        #         message = "\n".join(formatted_traceback_lines)
        #
        #     # with open(Logger.logFile, "a+") as file:
        #     #     _date = datetime.now().strftime("%H:%M:%S")
        #
        #     print(f"[{Logger.appName}]")
        #     print(f"[{Logger.appName}]", "===================== AN ERROR OCCURED =====================")
        #     print(f"[{Logger.appName}]")
        #     # print(f"[{Logger.appName}]", f"File: {caller_file}, Line: {caller_line}, Function: {caller_function}()")
        #     print(f"[{Logger.appName}] Traceback : ", message)
        #     print(f"[{Logger.appName}]")
        #     print(f"[{Logger.appName}]", f"Log file : {os.path.abspath(Logger.logFile)}")
        #     print(f"[{Logger.appName}]")
        #     print(f"[{Logger.appName}]", "============================================================")
        #
        #     return
        #
        # print(f"[{Logger.appName}] [ERROR]", message)

    @staticmethod
    def debug(message):
        pass
        # if Configuration.get("appEnvironment") == "development":
        #     if not os.path.exists(Logger.logDir):
        #         os.mkdir(Logger.logDir)
        #     with open(Logger.logFile, "a+") as file:
        #         _date = datetime.now().strftime("%H:%M:%S")
        #         _log = f"[{_date}] [DEBUG]" + f" {message}" + "\n"
        #         file.write(_log)
        #
        # if Configuration.get("logLevel") == 1:
        #     print(f"[{Logger.appName}] [DEBUG]", message)

