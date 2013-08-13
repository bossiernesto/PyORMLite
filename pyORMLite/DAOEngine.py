import inspect
from PyORMLiteExecptions import DAOEngineException
from pyORMLiteSettings import EXECUTOR
from pyORMLiteMapper import PropertyMappings

class DAOEngine(object):

    def __init__(self,mappedClass,tableName,mappings=[]):
        if not inspect.isclass(mappedClass): raise DAOEngineException('{0} is not a valid Class'.format(mappedClass))
        self.mappedClass=mappedClass
        self.tableName=tableName
        self.mappings=mappings
        self.executor=EXECUTOR()

    def update(self,object):
        pass

    def add(self,object):
        fieldNames=','.join([mapping.columnName for mapping in self.mappings])
        questionMarks=','.join(['?' for mapping in self.mappings])
        values=[mapping.getvalue(object) for mapping in self.mappings]

        query = " INSERT INTO {0} ({1}) VALUES ({2});".format(self.tableName,fieldNames,questionMarks)
        self.executor.update(query,values) #TODO: create an update method in executor

    def findAll(self):
        self.find(filters=[])

    def find(self,filters=[]):

        whereClause=""
        query="SELECT * FROM {0}".format(self.tableName)

        if filters:

            whereClause=" and ".join(filter.getConditionString() for filter in filters)
            query+= " WHERE {0};".format(whereClause)

            self.executor.query(query,)#TODO: finish executor, create a RowMapper class that can handle each rowMapping

        """return this.jdbcTemplate.query(query, new RowMapper() {
            public Object mapRow(ResultSet rs, int rowNum) throws SQLException {
        try {
            Object result = mappedClass.newInstance();
        for (PropertyMapping mapping : GenericDao.this.mappings) {
            mapping.setValue(result, rs);
        }
        return result;
        }
        catch (Exception e) {
        throw new RuntimeException(e);"""

    def addProperty(self,propertyMapping):
        if not isinstance(propertyMapping,PropertyMappings):
            raise DAOEngineException('{0} is not an instance of {1}'.format(propertyMapping,PropertyMappings))
        self.mappings.append(propertyMapping)



