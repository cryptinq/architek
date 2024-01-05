import random
import re
import time

from core.Kernel import Kernel
from core.kernel.console.base.BaseCommand import BaseCommand
from core.kernel.file.helpers.FileSystem import FileSystem


class KeyGenerateCommand(BaseCommand):

    def __init__(self, kernel: Kernel):
        super().__init__(kernel)

    def invoke(self):

        key = ""
        key_lenght = 64

        chars_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number_list = "0123456789"

        nb_chars = int(70 * (key_lenght / 100))
        nb_numbers = int(30 * (key_lenght / 100)) + 1

        for _ in range(nb_chars):
            key += chars_list[random.randint(0, (len(chars_list) - 1))]
        for _ in range(nb_numbers):
            key += number_list[random.randint(0, (len(number_list) - 1))]

        key = ''.join(random.sample(key, len(key)))

        try:

            with open(FileSystem.from_root(".env"), "r") as env_file:
                env_file_content = env_file.readlines()
                env_file.close()
            new_env_file_content = []

            for line in env_file_content:

                starting_line = line
                edited_line = re.sub(r'(APP_KEY=).*', r'\1' + key, line)

                if starting_line != edited_line:
                    edited_line = "APP_KEY=" + edited_line \
                        if "APP_KEY=" not in edited_line \
                        else edited_line
                new_env_file_content.append(edited_line)

            with open(FileSystem.from_root(".env"), "w") as env_file:
                env_file.writelines(new_env_file_content)
                env_file.close()

        except Exception as e:
            self.stdout("Error while writing API_KEY to .env, please retry", "error")
            exit(0)
            pass

        key_str_len = len(f"∑9. Application key : {key} ") - 1

        self.stdout("Successfully generated application key !", "success", new_line=True)
        self.stdout("∑9." + (" " * key_str_len), new_line=True)
        self.stdout(f"∑9.  Application key : {key}  ")
        self.stdout("∑9." + (" " * key_str_len))
