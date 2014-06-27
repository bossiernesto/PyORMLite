from ristrettoORM.utils.objectPool import ObjectPool,poolObj
from unittest import TestCase

# Fixture
class A:
    def bleh(self):
        return 3

    def aaa(self):
        return 34


class AWithkwargs(object):
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs

#Custom Pool
CUSTOM_POOL_SIZE = 3
class CustomPool(ObjectPool):
    pool_size = CUSTOM_POOL_SIZE

class ObjectPoolTest(TestCase):
    def setUp(self):
        self.a_pool = ObjectPool(A)
        self.custom_pool = CustomPool(A)

    def test_get_object(self):
        self.assertTrue(isinstance(self.a_pool.borrowObj(), A))

    def test_get_two_objects(self):
        obj1 = self.a_pool.borrowObj()
        obj2 = self.a_pool.borrowObj()

        self.assertTrue(isinstance(obj1, A))
        self.assertTrue(isinstance(obj2, A))
        self.assertNotEqual(obj1, obj2)

    def test_get_object_kwargs(self):
        expected_dict = {'a': 2}
        self.akwargs_pool = ObjectPool(AWithkwargs, kwargs=expected_dict)

        obj1 = self.akwargs_pool.borrowObj()
        self.assertTrue(isinstance(obj1, AWithkwargs))
        self.assertEqual(obj1.kwargs, expected_dict)


    def test_custom_pool_size(self):
        self.assertEqual(CUSTOM_POOL_SIZE,self.custom_pool.pool_size)

    def test_custom_pool_context(self):
        with poolObj(self.custom_pool) as borrowed_object:
            self.asserted_object = borrowed_object
            self.assertTrue(isinstance(borrowed_object,A))
            self.assertEqual(34,borrowed_object.aaa())
        self.assertEqual(1,self.custom_pool.queue.qsize())
        self.assertEqual(self.asserted_object,self.custom_pool.queue._get())
