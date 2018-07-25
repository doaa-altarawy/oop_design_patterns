"""
  Observer Design Pattern

  - one-to-many relation
  - We have a subject object, and there are other objects (observers) that are
    interested to be notified whenever that subject changes.
  - When one object change state, other observers get notified (updated)
  - allows for the Open Closed principle, you can register many observers
    to do many actions without changing the main class
"""

import abc


class Subject(object):
    """ The subject class the many observers want to watch
        Keeps track of everybody who wants to be informed when a change happens
    """

    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)


class Observer(object):
    """Observer class that wants to listen on a subject"""

    @abc.abstractmethod
    def update(self, subject):
        """This method is called by the object that’s being observed
           When called, it means the subject you are listening on has changed
           Do what you want to do about it """
        pass

# ~~~~~~~~~~~~~~ Example using the Observer Design Pattern ~~~~~~~~~~~~

class Facebook(Subject):
    """Subject that that others are watching"""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def new_msg(self, msg):
        print('A new message is being processed, DB, ...')
        # Do some processing, then
        self.notify_observers()


class Device(Observer):
    """An observer class"""

    def __init__(self, name):
        self.name = name

    def update(self, subject):
        print('Showing a new message on {}'.format(self.name))


class LoggingServer(Observer):

    def update(self, subject):
        print('Message is saved on server')

# ~~~~~~~~~~~~~~ Test the example ~~~~~~~~~~~~~

doaa_fb = Facebook('Doaa')
logging_server = LoggingServer()
my_desktop = Device('Desktop')
my_phone = Device('iPhone')
my_laptop = Device('X1 Carbon')

doaa_fb.register_observer(logging_server)
doaa_fb.register_observer(my_desktop)
doaa_fb.register_observer(my_phone)
doaa_fb.register_observer(my_laptop)

doaa_fb.new_msg('Hello there!')
