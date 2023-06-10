import os
import sys

from core.Kernel import Kernel


def boot():
    _path = os.path.dirname(os.path.realpath(__file__))
    _console = sys.argv[0] == "console"
    _kernel = Kernel(_path, _console)
    _kernel.boot()


if __name__ == "__main__":
    boot()
