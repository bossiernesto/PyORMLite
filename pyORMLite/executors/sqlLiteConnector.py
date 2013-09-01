from PyORMLiteConnector import AbstractDBConnector


class SQLLiteConnector(AbstractDBConnector):

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