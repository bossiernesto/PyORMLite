"""
.. module:: Dao Engine
   :platform: Linux
   :synopsis: Main object that holds converters and mappers.
   :copyright: (c) 2013 by Ernesto Bossi.
   :license: GPL v3.

.. moduleauthor:: Ernesto Bossi <bossi.ernestog@gmail.com>

"""
import inspect
from ristrettoORMExceptions import DAOEngineException
from ristrettoORM.propertyMapper import PropertyMappings
from ristrettoORMSettings import CONNECTOR


class DAOEngine(object):

    def __init__(self, mappedClass, tableName, mappings=[], connector=CONNECTOR):
        if not inspect.isclass(mappedClass):
            raise DAOEngineException('{0} is not a valid Class'.format(mappedClass))
        self.mappedClass = mappedClass
        self.tableName = tableName
        self.mappings = mappings
        self.executor = connector()

    def update(self, instance):
        pass

    def addMany(self, instanceCollection):
        pass

    def add(self, instance):
        fieldNames = ','.join([mapping.columnName for mapping in self.mappings])
        
        values = tuple([mapping.getvalue(instance) for mapping in self.mappings])
        questionMarks = ','.join(['?' for value in values])
        self.executor.insert(self.tableName, fieldNames, questionMarks, [values])

    def findAll(self):
        self.find(filters=[])

    def find(self, filters=[]):

        whereClause = ""
        query = "SELECT * FROM {0}".format(self.tableName)

        if filters:
            whereClause = " AND ".join(f.get_condition_string() for f in filters)
            query += " WHERE {0};".format(whereClause)

        self.executor.query(query, RowMapper(self.mappedClass, self.mappings))

    def addProperty(self, propertyMapping):
        if not isinstance(propertyMapping, PropertyMappings):
            raise DAOEngineException('{0} is not an instance of {1}'.format(propertyMapping, PropertyMappings))
        self.mappings.append(propertyMapping)

    def remove(self, instance):
        fieldNames = ','.join([mapping.columnName for mapping in self.mappings])
        questionMarks = ','.join(['?' for mapping in self.mappings])
        values = tuple([mapping.getvalue(instance) for mapping in self.mappings])



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
