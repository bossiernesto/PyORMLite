
class AbstractExecutor(object):

    def execute(self,query):
        self.interface.run(query)


class SQLServerExecutor(object):

    pass