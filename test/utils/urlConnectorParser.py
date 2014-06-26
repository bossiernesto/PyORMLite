from unittest import TestCase
from ristrettoORM.utils.urlConnectorParser import URLConnectorParser

class URLParseTest(TestCase):
    def test_parse_portgresql_url(self):
        url = "postgresql://scott:tiger@localhost:5432/mydatabase"
        expected_directory = {'password': 'tiger', 'database': 'mydatabase', 'name': 'postgresql', 'ipv6host': None, 'ipv4host': 'localhost', 'username': 'scott', 'port': '5432'}
        self.assertEqual(URLConnectorParser().parse_URL(url), expected_directory)

    def test_parse_sqlite_url(self):
        url = "sqlite:///tutorial.db"
        expected_dictionary = {'password': None, 'database': 'tutorial.db', 'name': 'sqlite', 'ipv6host': None, 'ipv4host': None, 'username': None, 'port': None}
        self.assertEqual(URLConnectorParser().parse_URL(url),expected_dictionary)
