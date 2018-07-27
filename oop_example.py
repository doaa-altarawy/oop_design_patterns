"""
    Example using Object oriented features in Python 3
"""

import abc


# optional to extend from abc.ABC (abstract base class)
# in python 2 use super class: abc.ABCMeta('ABC', (), {})
# or use: __metaclass__ = abc.ABCMeta
class AbstractOrder(abc.ABC):

    def __init__(self, name):
        self.name = name

    # Abstract method has no implementation
    # must be implemented by subclasses
    @abc.abstractmethod
    def order_details(self):
        pass

    def say_hello(self):
        return "Hello from parent class"


# class Order(object): # python 2 style
class Order(AbstractOrder):  # python 3 style

    # class attribute
    _in_stock = 10

    # initialization
    # self references the object
    # method overloading: using default values
    def __init__(self, num_items=0, name=None):
        # in python 2 use:
        # super(Order, self).__init__(name)
        super().__init__(name)
        Order._in_stock -= num_items      # access class attribute

        # instance attribute, naming conventions:
        # self.name     public
        # self._name    protected
        # self.__name   private
        self.num_items = num_items

    # instance method
    def order_details(self):
        return "{} ordered {} items.".format(self.name, self.num_items)

    @classmethod
    def class_method(cls):
        return 'In stock: {}.'.format(cls._in_stock)

    @staticmethod
    def static_method():
        return "I'm static, I don't know my class."


class StoreOrder(Order):
    """Special kind of order from stores, we have no name"""

    # method override (polymorphism)
    def order_details(self):
        return "From Store, ordered {} items.".format(self.num_items)


# ------ Example -------

# create objects
order1 = Order(3, 'Sarah')
order2 = StoreOrder(2)

# Use Python duck typing, and polymorphism
for order in (order1, order2):
    print(order.order_details())

# Class and static methods, both are okay
print(order1.class_method(), 'OR', Order.class_method())
print(order1.static_method(), 'OR', Order.static_method())

# method from super/parent class
print(order1.say_hello())

# can access private attributes, but discouraged
print("Shouldn't access these: ", Order._in_stock, order1._in_stock)

# Can't instantiate (make an object of) an abstract class
try:
    wont_work = AbstractOrder('Tom')
except Exception as err:
    print('Error: ', err)
