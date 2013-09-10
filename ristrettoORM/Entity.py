from ristrettoORM.observer import Subject
from ristrettoORM.ristrettoORMUtils import inherit

class EntityMixin(Subject):

    def __setattr__(self, name, value):
        #notify changes and update
        super.__setattr__(self ,name,value)

def scope_ORM():
    def decorator(cls):
        new_class = inherit(cls, EntityMixin)
        return new_class
    return decorator

@scope_ORM()
class SomeClass(object):
    def new_method(self, value):
        return value * 3

if __name__ == '__main__':
    some =SomeClass()
    print(some.__class__.__bases__)
    a= SomeClass()
    a.e=2
    print(a.__class__.__bases__)
    print(a.e)
