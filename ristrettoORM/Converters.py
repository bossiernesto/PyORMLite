from datetime import date
from abc import ABCMeta, abstractmethod
from ristrettoORM.ristrettoORMUtils import wrap_dao_exception, wrap_pyorm_exception

class PropertyConverter(object):

    __metaclass__ = ABCMeta

    def getValue(self, propertyName, obj):
        try:
            return getattr(obj, propertyName)()
        except Exception as e:
            wrap_pyorm_exception("Failed getting value of {0} because of: {1}".format(propertyName, e.message))

    @abstractmethod
    def getConverterFromType(self):
        raise NotImplementedError

    @abstractmethod
    def getValueFromResultSet(self, columnName, resultSet):
        raise NotImplementedError

    @staticmethod
    def getConverterForType(type):
        try:
            return CONVERTERS[type]
        except Exception:
            wrap_dao_exception("Invalid converter Type queried")


class StringConverter(PropertyConverter):

    def getConverterFromType(self):
        return str.__class__

    def getValueFromResultSet(self, columnName, resultSet):
        return resultSet.getString(columnName)


class DateConverter(PropertyConverter):

    def getConverterFromType(self):
        return date.__class__

    def getValueFromResultSet(self, columnName, resultSet):
        return resultSet.getDate(columnName)

CONVERTERS = {str:StringConverter(), date:DateConverter()}
