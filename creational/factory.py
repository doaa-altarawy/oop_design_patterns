"""
    Factory DP

    - When a class doesn't know what sub-classes will be required to create
    at runtime.
    - To hide instantiation logic inside the factory
    - This implementation is Python3 specific


"""
from abc import ABC, abstractmethod  # Abstract Base Class

# Classes and their implementations
# can have a super Pet class if needed


class Pet(ABC):  # abstract class
    @abstractmethod
    def speak(self):
        pass


class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Woof!"


class Cat(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Meow!"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Factory class/Method:
class PetFactory:
    """Factory class, contains a static method that returns the
        desired object
    """
    
    @staticmethod
    def get_pet(pet='dog'):
        """The factory method"""
        if pet == 'dog':
            return Dog('Hope')
        elif pet == 'cat':
            return Cat("Peace")

        return None

# or:
pet_factory = dict(dog=Dog('Hope'), cat=Cat("Peace"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


pet = PetFactory.get_pet('dog')
print(pet.speak())    # "Woof!"

pet = PetFactory.get_pet('cat')
print(pet.speak())    # "Meow!"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
