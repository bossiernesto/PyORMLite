import queue
from contextlib import contextmanager


class ObjectPool(object):
    """A simple object pool with thread safe fro python 3"""
    POOL_DEFAULT_SIZE = 1

    def __init__(self, objectFn, *args, **kwargs):
        super(ObjectPool, self).__init__()
        self.objectFn = objectFn
        self.objectCls = None
        self._myInit(*args, **kwargs)

    def __init__(self, objectCls, *args, **kwargs):
        super(ObjectPool, self).__init__()
        self.objectCls = objectCls
        self.objectFn = None
        self._myInit(*args, **kwargs)

    def _myInit(self, *args, **kwargs):
        self.args = args or []
        self.maxSize = int(kwargs.get("maxSize", self.POOL_DEFAULT_SIZE))
        self.kwargs = kwargs.get("kwargs") or {}
        self.queue = queue.Queue()

    def _getObj(self):
        if self.objectFn:
            return self.objectFn(self.args, self.kwargs) if self.args else self.objectFn()
        else:
            return self.objectCls(self.args, self.kwargs) if self.args else self.objectCls()

    def borrowObj(self):
        if self.queue.qsize() < self.maxSize or self.queue.empty():
            self.queue.put(self._getObj())
        return self.queue.get()

    def returnObj(self, obj):
        self.queue.put(obj)


@contextmanager
def poolObj(pool):
    obj = pool.borrowObj()
    try:
        yield obj
    except Exception as e:
        yield None
        raise e
    finally:
        pool.returnObj(obj)