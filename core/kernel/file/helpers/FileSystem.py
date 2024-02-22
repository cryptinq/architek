import os
from os.path import isfile, join
from pathlib import Path


class FileSystem:
    rootDir = os.path.join(
        os.path.dirname(__file__),
        "..", "..", "..", ".."
    )

    @staticmethod
    def from_root(path):
        return os.path.abspath(
            os.path.join(
                FileSystem.rootDir, *path.split("/")
            )
        )

    @staticmethod
    def join(*args): return os.path.join(*args)

    @staticmethod
    def remove(path):
        if isfile(path): os.remove(path)

    @staticmethod
    def write(path, content):
        with open(path, "w") as file:
            file.write(content)
            file.close()

    @staticmethod
    def file_exist(path):
        return os.path.isfile(path)

    @staticmethod
    def list_files(path, extensions=None):

        if extensions is None: extensions = ["*"]
        files = []

        try:
            # List all files in the given directory
            all_files = [f for f in os.listdir(path) if isfile(join(path, f))]

            # Filter files based on the specified extensions
            for file in all_files:
                for ext in extensions:
                    if ext == "*" or file.endswith(ext):
                        files.append(file)
                        break  # Move to the next file once it matches an extension
        except FileNotFoundError:
            # Handle the case where the directory does not exist
            print(f"Directory '{path}' does not exist.")
        return files

    @staticmethod
    def get_extension(path):

        file_ext = "__unknown"
        file_name = (path.split("/")[-1]).split(".")[0]
        dir_path = Path("/".join(path.split("/")[:-1]))
        files = [file for file in dir_path.iterdir() if file.is_file()]

        for file in files:
            full_name = (str(file).split("/")[-1])
            name, extension = full_name.split(".")
            if name == file_name:
                file_ext = "." + extension

        if file_ext == "__unknown": raise FileNotFoundError("")

        return file_ext
