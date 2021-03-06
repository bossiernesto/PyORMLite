from unittest import TestCase
from ristrettoORM.observer import Subject, notify, Observer


class ObservableData(Subject, object):
    def __init__(self):
        super(ObservableData, self).__init__()
        Subject.__init__(self)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @notify
    def updateValue(self, value):
        print("Update with value,{0}".format(value))
        self.data = value


class ObserverOverseer(Observer):
    def update(self, subject):
        self.data = subject.data + 1


class TestObserver(TestCase):
    def setUp(self):
        self.data = ObservableData()
        self.observer = ObserverOverseer()
        self.data.attach(self.observer)

    def testUpdate(self):
        self.data.updateValue(4)
        self.assertEquals(self.data.data, 4)
        self.assertEquals(self.observer.data, 5)