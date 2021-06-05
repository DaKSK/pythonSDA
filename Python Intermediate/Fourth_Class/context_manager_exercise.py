import time
from contextlib import contextmanager
import datetime


@contextmanager
def do_some_function():
    tick = time.perf_counter()
    try:
        yield print("Printing function to be measured")
    finally:
        tok = time.perf_counter()
        print(f"{tick-tok} second of duration")


do_some_function()
