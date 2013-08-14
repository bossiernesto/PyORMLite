import sys
from PyORMLiteExecptions import PyORMLiteException,DAOEngineException


def wrapPyORMException(message):
    """
    Function that wraps an existing Exception in stackTrace with a PyORMLiteException

    :param message: Description of the message that the developer wants to show when the wrap Exception is raised
    :type message: str
    """
    wrapException(PyORMLiteException, message)


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
    raise exceptionClass(message), None, trace