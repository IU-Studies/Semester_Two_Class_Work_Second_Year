import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def decorator(func):
    def gx(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        logging.info(f"'{func.__name__}' executed in {time.time() - start:.6f} seconds.")
        return result
    return gx

@decorator
def demo(n):
    time.sleep(n)
    return f"Completed after {n} seconds"

demo(3)
