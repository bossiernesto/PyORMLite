class AbstractDBConnector(object):

    def insert(self, tableName, fieldNames, questionMarks, values):
        query = " INSERT INTO {0} ({1}) VALUES ({2});".format(tableName, fieldNames, questionMarks)
        self.executeSQL(query, values)

    def query(self, query, rowMapper):
        resultSet = self.executeSQL(query)
        for row in resultSet:
            rowMapper.mapRow(row)

    def delete(self, ):

    def executeSQL(self, query, values=None):
        raise NotImplementedError

    def createTable(self, tableName, values):
        raise NotImplementedError

    def dropTable(self, tableName):
        raise NotImplementedError

    def beginTran(self):
        raise NotImplementedError

    def endTran(self):
        raise NotImplementedError


class DBAdapter(AbstractDBConnector):

    class InnerAdapterDBBridge(object):
        def __init__(self, outer):
            self.outer = outer

        def executeQuery(self, query):
            self.outer.beginTran()
            self.outer.executeSQL(query)
            self.outer.endTran()

        def createTable(self, name, values):
            self.outer.createTable(name, values)

        def dropTable(self, name):
            self.outer.dropTable(name)

    def DBBridge(self):
        return DBAdapter.InnerAdapter(self)
