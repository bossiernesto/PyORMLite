from pyORMLiteSettings import CONNECTOR

class PyORMLiteExecutor(object):

    def __int__(self):
        self.connector = CONNECTOR

    def execute(self, query):
        self.connector.executeQuery(query)

    def update(self, query, values):
        pass

    def query(self, query, rowMapper):
        pass

    def createTable(self, tableName, values):
        pass

    def dropTable(self, tableName):
        pass


class AbstractDBConnector(object):

    def executeSQL(self, query):
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

        def createTable(self):
            self.outer.createTable()

    def DBBridge(self):
        return DBAdapter.InnerAdapter(self)
