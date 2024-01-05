import os
import sys

from core.Kernel import Kernel


def boot():

    (Kernel(
        os.path.dirname(os.path.realpath(__file__)),
        sys.argv[0] == "console",
    )).finalize().boot()


if __name__ == "__main__":
    boot()
