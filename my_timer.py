import time

def run_time(prog):
    a = time.perf_counter_ns()
    prog
    b = time.perf_counter_ns()

    print(f"This took {b-a} ns")

class TimerError(Exception):
    """This throws Exceptions to report errors in Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """"Starts a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop.")
        
        self._start_time = time.perf_counter()
    
    def stop(self):
        """This stops the timer and reports the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"The timer is NOT running. Use .start() to start a timer.")
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")