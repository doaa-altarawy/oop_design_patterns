"""
     A real singleton class
     provides only one object of a particular type
"""


class OnlyOne:

    class __OnlyOne:

        def __init__(self, arg):
            self.arg = arg

        # def __str__(self):
        #     return repr(self) + self.val

    instance = None     # static (class) attribute

    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.arg = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)

# --------------------------------------------------


x = OnlyOne('apple')
print(x)
y = OnlyOne('orange')
print(y)
z = OnlyOne('pear')
print(z)


print('z.arg: ', z.arg)
print('x.arg: ', x.arg)

print(x)
print(y)
print(z)
