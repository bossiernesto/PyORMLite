from abc import ABCMeta


class AbstractExecutor(object):

    __metaclass__ = ABCMeta

    def execute(self, query):
        self.interface.run(query)

    def update(self, query, values):
        pass

    def query(self, query, rowMapper):
        pass


class SQLServerExecutor(AbstractExecutor):

    pass

