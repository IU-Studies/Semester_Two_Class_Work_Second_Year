#Write a Python program to create a custom decorator that logs the name and execution time of a function.

import time

def decorator(func):
    def gx(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Function executed in", end - start, "seconds.")
        return result
    return gx

@decorator
def demo():
    name = input("Enter your name: ")
    print("Hello", name)

demo()
