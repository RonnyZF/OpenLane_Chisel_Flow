import builtins
import math
import sys
import threading

class ProgressConsole:
    def __init__(self, size, width=80, output=sys.stdout):
        self.size = size
        self.width = width
        self.current = 0
        self.output = output
        # [...] and space take 3 characters, plus max width of size (log10 + 1)
        self._bar_size = width - 4 - int(math.log10(size))
        self._bar_step = self._bar_size / self.size
        self._lock = threading.Lock()

    def print(self, *message):
        with self._lock:
            self._clear()
            builtins.print(*message, file=self.output)
            self._display()

    def increment(self, step=1):
        with self._lock:
            self.current = min(self.current + step, self.size)
            self._display()

    def _clear(self):
        self.output.write('\r')
        self.output.write(' ' * self.width)
        self.output.write('\r')

    def _display(self):
        bar = '#' * int(round(self._bar_step * self.current))
        blank = ' ' * (self._bar_size - len(bar))
        self.output.write(f"\r[{bar}{blank}] {self.current}")