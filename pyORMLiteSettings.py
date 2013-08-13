from executors import sqlserverExecutor
from pyORMLite.PyORMLiteConverters import StringConverter,DateConverter
from datetime import date

EXECUTOR=sqlserverExecutor.SQLServerExecutor
PROPERTY_CONVERTERS={str:StringConverter(),date:DateConverter()}