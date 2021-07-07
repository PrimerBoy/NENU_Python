import types
from functools import wraps
from lxml import etree
from os import path
from optparse import OptionParser


class XMLDealer:
    def __init__(self, func, file_name):
        self.ncalls = 0
        self.nelem = 0
        self.file_name = file_name
        self.context = etree.iterparse(self.file_name)

    def __call__(self):

        self.ncalls += 1

        def wrapper(*args, **kwargs):
            for event, elem in self.context:
                self.nelem = self.nelem + 1
                func(elem)

        return wrapper

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@XMLDealer(file_name="P00734.xml")
def deal_with_elem(elem: object):
    if isinstance(elem, object) and hasattr(elem, "text"):
        print(elem.text)
    else:
        print(f"{elem} not a XML element.")


if __name__ == '__main__':
    deal_with_elem()
    print(deal_with_elem)
    print("Parsed %10d XML elements."%deal_with_elem.nelem)
