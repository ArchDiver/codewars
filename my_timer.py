import time

# def run_time(prog):
#     a = time.perf_counter_ns()
#     prog
#     b = time.perf_counter_ns()

#     print(f"This took {b-a} ns")

def timed(prog):
    t = Timer()
    t.start()

    print(prog)

    t.stop()

class TimerError(Exception):
    """This throws Exceptions to report errors in Timer class"""


class Timer:
    def __init__(self, text="Elapsed time: {} ns", logger=print):
        self._start_time = None
        self.text = text
        self.log = logger

    def start(self):
        """"Starts a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop.")
        
        self._start_time = time.perf_counter_ns()
    
    def stop(self):
        """This stops the timer and reports the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"The timer is NOT running. Use .start() to start a timer.")
        elapsed_time = time.perf_counter_ns() - self._start_time
        self._start_time = None
        # print(self.text.format(elapsed_time))
        if self.log:
            self.log(self.text.format(elapsed_time))
        
        return elapsed_time