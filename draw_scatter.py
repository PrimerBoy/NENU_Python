import matplotlib.pyplot as plt
from functools import wraps
import random

def generate_random(limit_min:float, limit_max:float, length:int):
    # generate random float list with length
    x = [random.uniform(limit_min, limit_max) for ii in range(length)]
    y = [random.uniform(limit_min, limit_max) for ii in range(length)]
    # call draw function
    def inner(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            func(x, y)
        return wrap
    return inner

@generate_random(0, 10, 100)
def draw_random(x, y):
    plt.scatter(x, y, alpha=0.5)
    plt.show()

if __name__ == '__main__':
    draw_random()