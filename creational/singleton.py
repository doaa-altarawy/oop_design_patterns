"""
This an example singleton design pattern (DP)

A Singleton: allowing on instance to be instantiated from a class

Example usage:
    - The proper way to create a global variable in OOP
    - An information cashe, shared by multiple objects
    - Modules in Python are singletons
    -

We will use the Borg design pattern to impliment singleton, there are many
other ways to do it.

"""

class Singleton:
    """Shares its attributes among all its instances"""

    __shared_state = {}   # shared dictionary

    def __init__(self, **kwargs):
        self.__dict__ = self.__shared_state
        self.__shared_state.update(kwargs)

    def __str__(self):
        return str(self.__shared_state)

    def get_list(self):
        return self.__shared_state

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

param = Singleton(VT='Virginia Tech')

print(param)
print(param.VT)

y = Singleton(MSS='MolSSI software scientist')

print(param.MSS)
