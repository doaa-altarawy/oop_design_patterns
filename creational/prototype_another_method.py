"""
Prototype Design pattern

  - Needed when creating several similar objects.
  - Create a Prototype intstance then clone it whenever needed
"""

import copy

class ShapePrototype:
    """Protoype classs to clone objects"""
    cashe = {}

    @staticmethod
    def get_shape(name):
        car = ShapePrototype.cashe.get(name, None)
        return car.clone

    @staticmethod
    def load():
        ShapePrototype.cashe['circle'] = Circle()
        ShapePrototype.cashe['Square'] = Square()


class Shape:
    def __init__(self):
        self.type = None
        self.n_sides = None

    def clone(self):
        return copy.copy(self)

    def __str__(self):
        return 'Type: {} | # of sides: {} '.format(self.type, self.n_sides)

class Circle(Shape):
    pass
class Square(Shape):
    pass
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

car = Car()
prototype = Prototype()
prototype.register_object('Skylark', car)

c1 = prototype.clone('Skylark')
print(c1)
