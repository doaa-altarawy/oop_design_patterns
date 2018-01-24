"""
    Iterator classs in python

    - Compatiable with python 2
"""

class Iterator(object):

    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def next(self):  # for Compatiablity with python 2
        return self.__next__()

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            tmp = self.current
            self.current += self.step
            return tmp

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

iterator = Iterator(0, 10)
for i in iterator:
    print(i)

print('Again')
for i in iterator:
    print(i)

print('Double')
for i in Iterator(0, 10, 2):
    print(i)

print('None')
for i in Iterator(10, 5):
    print(i)
