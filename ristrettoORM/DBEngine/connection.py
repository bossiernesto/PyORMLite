from ristrettoORM.utils.urlConnectorParser import URLConnectorParser

DEFAULT_HOST = 'localhost'


class Connector:
    def create_connection(self, url_connector, *kwargs):
        URLConnectorParser().process_url(self, url_connector)
        self.options = *kwargs

    def connect(self, user, password, host=DEFAULT_HOST):
        pass

    def set_connection_data(self, options_dictionary):
        pass




