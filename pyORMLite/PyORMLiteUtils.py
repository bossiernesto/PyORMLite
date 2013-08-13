import sys
from PyORMLiteExecptions import  PyORMLiteException,DAOEngineException

def wrapPyORMException(message):
    wrapException(PyORMLiteException,message)

def wrapDAOException(message):
    wrapException(DAOEngineException,message)

def wrapException(exceptionName,message):
    trace = sys.exc_info()[2]
    raise exceptionName(message), None, trace