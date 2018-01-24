"""
     A real singleton class
     provides only one object of a particular type
"""

class OnlyOne:

    class __OnlyOne:

        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val

    instance = None     # static (class) variable

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)

# --------------------------------------------------

x = OnlyOne('apple')
print(x)
y = OnlyOne('organge')
print(y)
z = OnlyOne('pear')

print('z.val', z.val)
print(z)
print(x)
print(y)
