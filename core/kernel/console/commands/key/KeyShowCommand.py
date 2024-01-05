import random
import re
import time

from core.Kernel import Kernel
from core.kernel.console.base.BaseCommand import BaseCommand
from core.kernel.file.helpers.FileSystem import FileSystem


class KeyShowCommand(BaseCommand):

    def __init__(self, kernel: Kernel):
        super().__init__(kernel)

    def invoke(self):

        app_key = self.kernel.app("env").get("APP_KEY")
        # app_key = "t5xR7o196HGLBHfa75GDu5XkL8jfb91cN61yrdGhLR0z5NjGQdiuavL28E00nOP7"

        key_str_len = len(f"∑9. Application key : {app_key} ") - 1

        self.stdout("∑9." + (" " * key_str_len), new_line=True)
        self.stdout(f"∑9.  Application key : {app_key}  ")
        self.stdout("∑9." + (" " * key_str_len))
