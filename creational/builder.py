"""
    Builder DP (building complex objects (with different types) step by step)

    - solves the anti-pattern telescoping constructor problem
    - Problem: build a complex object without complexity
    - the object can have different flavors (thus different builders)
    - provides better control over the construction process
    - supports changing the internal representation of an object

"""

class Director:
    """Director classs
       for instance, the shop selling cars
    """

    def __init__(self, builder):
        self._builder = builder

    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()

        return self._builder.car


class Builder:
    """ Abstract Builder (car builder) (an interface)
        Note: can make it abstract with metaclass=abc.ABCMeta (Abstract Base Class)
    """
    def __init__(self):
        self.car = None

    def create_new_car(self): # build_parts
        self.car = Car()


class SkyLarkBuilder(Builder):
    """Concrete Builder, provides parts and tools
       for a specific product kind
    """

    def add_model(self):
        self.car.model = 'Skylark'

    def add_tires(self):
        self.car.tires = 'Regular tires'

    def add_engine(self):
        self.car.engine = 'Turbo engine'


class Car:
    """The product to build"""

    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

builder = SkyLarkBuilder()
director = Director(builder)
car = director.construct_car()

print(car)
