"""
    Example using Object oriented features in Python 2 and 3
"""

import abc
import sys
print(sys.version_info)

if sys.version_info >= (3, 4):
    ABC = abc.ABC
else:
    ABC = abc.ABCMeta('ABC', (), {})


# optional to extend from abc.ABC (abstract base class)
class AbstractOrder(ABC):

    def __init__(self, name):
        self.name = name

    # Abstract method has no implementation and must be implemented by subclasses
    @abc.abstractmethod
    def order_details(self):
        pass

    def say_hello(self):
        return "hello from parent class"

# class Order(object): # python 2 style
class Order(AbstractOrder):  # python 3 style

    # class attribute
    _in_stock = 10

    # initialization
    # self references the object
    def __init__(self, num_items, name):
        super(Order, self).__init__(name)
        Order._in_stock -= num_items      # access class attribute

        # instance attribute, naming conventions:
        # self.name     public
        # self._name    protected
        # self.__name   private
        self.num_items = num_items


    # instance method, or just a method
    def order_details(self):
        return "{} ordered {} items.".format(self.name, self.num_items)


    @classmethod
    def class_method(cls):
        return 'In stock: {}.'.format(cls._in_stock)

    @staticmethod
    def static_method():
        return "I'm static, I don't know my class."


order = Order(3, 'Joe')
print(order.order_details())
order2 = Order(2, 'Dan')
print(order2.order_details())

print(order.say_hello())

# both are okay
print(order.class_method(), Order.class_method())
print(order.static_method(), Order.static_method())

# can access, but discouraged
print(Order._in_stock, order._in_stock)

try:
    wont_work = AbstractOrder('Tom')
except Exception as err:
    print('Error: ', err)

