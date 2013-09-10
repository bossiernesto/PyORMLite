from datetime import date
from ristrettoORM.converters import StringConverter, DateConverter
from ristrettoORM.executors.sqlLiteConnector import SQLLiteConnector

CONNECTOR = SQLLiteConnector
PROPERTY_CONVERTERS = {str:StringConverter(), date:DateConverter()}