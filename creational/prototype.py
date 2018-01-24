"""
Prototype Design pattern

  - Needed when creating several similar objects.
  - Maybe when the cost of creating an object from scratch is large
  - Create a Prototype intstance then clone it whenever needed
"""

import copy

class Prototype:
    """Protoype classs to register and clone objects"""

    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)   # possibly update some attr's
        return obj


class Car:
    def __init__(self):
        self.name = 'Skylark'
        self.color = 'Red'
        self.options = 'Ex'

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

car = Car()
prototype = Prototype()
prototype.register_object('Skylark', car)

c1 = prototype.clone('Skylark')
print(c1)
