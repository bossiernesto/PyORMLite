from pyORMLite.DAOEngine import DAOEngine, DAOEngineException
from unittest import TestCase

class TestDAOEngine(TestCase):

    def setUp(self):
        self.engine = DAOEngine()