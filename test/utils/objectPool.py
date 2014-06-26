from ristrettoORM.utils.objectPool import ObjectPool
from unittest import TestCase

# Fixture
class A:
    def bleh(self):
        return 3

    def aaa(self):
        return 34

class AWithkwargs(object):

    def __init__(self,*args,**kwargs):
        self.kwargs = kwargs


pool = ObjectPool(A, maxSize=4)

for i in range(10):
    obj = "obj{0}".format(i)
    globals()[obj] = pool.borrowObj()
    print(globals()[obj])

class ObjectPoolTest(TestCase):

    def setUp(self):
        self.a_pool = ObjectPool(A)
        self.akwargs_pool = ObjectPool(AWithkwargs)

    def test_get_object(self):
        self.assertTrue(isinstance(self.a_pool.borrowObj,A))

    def test_get_two_objects(self):
        obj1 = self.a_pool.borrowObj()
        obj2 = self.a_pool.borrowObj()

        self.assertTrue(isinstance(obj1,A))
        self.assertTrue(isinstance(obj2,A))
        self.assertNotEqual(obj1,obj2)

    def test_