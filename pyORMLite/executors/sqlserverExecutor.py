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

"""
class WhatIHave:
    def g(self): pass
    def h(self): pass

class WhatIWant:
    def f(self): pass

class WhatIUse:
    def op(self, whatIWant):
        whatIWant.f()

# Approach 4: use an inner class:
class WhatIHave3(WhatIHave):
    class InnerAdapter(WhatIWant):
        def __init__(self, outer):
            self.outer = outer
        def f(self):
            self.outer.g()
            self.outer.h()

    def whatIWant(self):
        return WhatIHave3.InnerAdapter(self)

"""