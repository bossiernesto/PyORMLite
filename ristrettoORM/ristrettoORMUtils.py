import sys
from ristrettoORMExceptions import RistrettoORMException,DAOEngineException


def wrapPyORMException(message):
    """
    Function that wraps an existing Exception in stackTrace with a RistrettoORMException

    :param message: Description of the message that the developer wants to show when the wrap Exception is raised
    :type message: str
    """
    wrapException(RistrettoORMException, message)


def wrapDAOException(message):
    """
    Function that wraps an existing Exception in stackTrace with a DAOEngineException

    :param message: Description of the message that the developer wants to show when the wrap Exception is raised
    :type message: str
    """
    wrapException(DAOEngineException, message)


def wrapException(exceptionClass, message):
    """
    Function that given an Exception class, wraps an existing exception in the stack trace with the given one.

    :param exceptionClass: Exception class that will wrap the current raised exception
    :param message: Description of the message that the developer wants to show when the wrap Exception is raised
    :type message: str
    """
    trace = sys.exc_info()[2]
    raise(exceptionClass, message, None, trace)

def inherit(cls,*supercls):
    for superclass in supercls:
        if cls.__name__ == superclass.__name__:
                raise TypeError("Class name collision trying to inherit class {0} to {1}"
                .format(superclass.__name__,cls.__name__))
    return type(cls.__name__, supercls + (object,), dict(cls.__dict__))

def add_mixin(cls, mixin, force=False):

    for name, value in mixin.__dict__.items():
        if name.startswith("_"):
            continue
        if not force and hasattr(cls, name):
            raise TypeError("name collision ({})".format(name))
        setattr(cls, name, value)
    try:
        mixin.register(cls)
    except AttributeError:
        pass

def mixin_classes(*mixins, force=False):
    """A class decorator factory that adds mixins using add_mixin.

    """
    def decorator(cls):
        for mixin in mixins:
            add_mixin(cls, mixin, force)
        return cls
    return decorator