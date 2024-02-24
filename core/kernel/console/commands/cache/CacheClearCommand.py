from time import time

from core.kernel.console.base.BaseCommand import BaseCommand
from core.kernel.file.helpers.FileSystem import FileSystem as fs


class CacheClearCommand(BaseCommand):

    def __init__(self):
        super().__init__()

    def invoke(self):

        start_time = time()

        cache_files = fs.list_files(
            fs.from_root(fs.join("storage", "cache"))
        )

        for file in cache_files:
            file_path = fs.from_root(fs.join("storage", "cache", file))
            self.console.info(f"Clearing {file_path}")
            fs.remove(file_path)

        print("")
        self.console.success(f"Cache file cleared successfully in {((time() - start_time) * 1000):.2f}ms")
