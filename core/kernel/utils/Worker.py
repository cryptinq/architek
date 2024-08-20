import threading
from typing import Optional, Callable


class Worker:
    def __init__(self, target: Callable, daemon: bool = True, on_finish: Optional[Callable] = None):
        self.target = target
        self.daemon = daemon
        self.on_finish = on_finish

    def run(self, *args, **kwargs):
        # Define a wrapper function to call the target and on_finish
        def worker_wrapper():
            self.target(*args, **kwargs)
            if self.on_finish:
                self.on_finish()

        # Create and start the thread with the wrapper function
        thread = threading.Thread(target=worker_wrapper, daemon=self.daemon)
        thread.start()
