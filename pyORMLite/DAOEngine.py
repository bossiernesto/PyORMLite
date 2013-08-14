import inspect
from PyORMLiteExecptions import DAOEngineException
from pyORMLiteSettings import EXECUTOR
from pyORMLiteMapper import PropertyMappings


class DAOEngine(object):

    def __init__(self, mappedClass, tableName, mappings=[]):
        if not inspect.isclass(mappedClass):
            raise DAOEngineException('{0} is not a valid Class'.format(mappedClass))
        self.mappedClass = mappedClass
        self.tableName = tableName
        self.mappings = mappings
        self.executor = EXECUTOR()

    def update(self, instance):
        pass

    def add(self, instance):
        fieldNames = ','.join([mapping.columnName for mapping in self.mappings])
        questionMarks = ','.join(['?' for mapping in self.mappings])
        values = [mapping.getvalue(instance) for mapping in self.mappings]

        query = " INSERT INTO {0} ({1}) VALUES ({2});".format(self.tableName, fieldNames, questionMarks)
        self.executor.update(query, values)

    def findAll(self):
        self.find(filters=[])

    def find(self, filters=[]):

        whereClause = ""
        query = "SELECT * FROM {0}".format(self.tableName)

        if filters:
            whereClause = " and ".join(f.getConditionString() for f in filters)
            query += " WHERE {0};".format(whereClause)

        self.executor.query(query, RowMapper(self.mappedClass, self.mappings))

    def addProperty(self, propertyMapping):
        if not isinstance(propertyMapping, PropertyMappings):
            raise DAOEngineException('{0} is not an instance of {1}'.format(propertyMapping, PropertyMappings))
        self.mappings.append(propertyMapping)


class RowMapper(object):

    def __init__(self, mappedClass, mappings):
        self.mappedClass = mappedClass
        self.mappings = mappings

    def mapRow(self, resultSet):
        try:
            result = self.mappedClass()
            for mAp in self.mappings:
                mAp.setValue(result, resultSet)
        except Exception:
            pass
