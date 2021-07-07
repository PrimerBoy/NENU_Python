import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        self.func = func
        wraps(self.__iter_func__)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

    def __iter_func__(self, *args, **kwargs):
        for ii in range(10):
            self.func(ii, ii + 1)

@Profiled
def add(x, y):
    print(x, y)
    return x + y

if __name__ == '__main__':
    z = add(3,4)
    print(z)
    print(add.ncalls)