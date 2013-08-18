from datetime import date
from pyORMLite.executors import sqlserverExecutor
from pyORMLite.PyORMLiteConverters import StringConverter, DateConverter


EXECUTOR = sqlserverExecutor.SQLServerExecutor
PROPERTY_CONVERTERS = {str:StringConverter(), date:DateConverter()}