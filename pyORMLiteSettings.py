from datetime import date
from pyORMLite.PyORMLiteConverters import StringConverter, DateConverter
from pyORMLite.executors.sqlLiteConnector import SQLLiteConnector

CONNECTOR = SQLLiteConnector
PROPERTY_CONVERTERS = {str:StringConverter(), date:DateConverter()}