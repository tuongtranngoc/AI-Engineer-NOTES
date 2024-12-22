import time
import threading
import numpy as np
from queue import Queue, LifoQueue, Empty


def _do_state(result: LifoQueue):
    t = np.random.uniform(0, 1)
    time.sleep(t)
    result.put({
        'state': 'successfully',
        'time': t
    })


class ThreadingState:
    def __init__(self, timeout, maxsize=1):
        self.timeout = timeout
        self.results = LifoQueue(maxsize=maxsize)
        
    def process_state(self):
        process = threading.Thread(target=_do_state, args=(self.results,))
        
        process.start()
        process.join(self.timeout)
        
        if process.is_alive():
            try:
                state = self.results.get_nowait()
                return {'state': 'failed', 'time': state['time']}
            except Empty:
                return {'state': 'failed', 'time': None}
            
        else:
            try:
                state = self.results.get_nowait()
                return {'state': state['state'], 'time': state['time']}
            except Empty:
                return {'state': 'failed', 'time': None}
            

if __name__ == "__main__":
    state1 = ThreadingState(timeout=0.5)
    for __ in range(10):
        s1 = state1.process_state()
        print(s1)