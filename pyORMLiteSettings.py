from datetime import date
from pyORMLite.PyORMLiteConverters import StringConverter, DateConverter


CONNECTOR = 1
PROPERTY_CONVERTERS = {str:StringConverter(), date:DateConverter()}