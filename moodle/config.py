from dacite import Config
from datetime import datetime

DACITE_CONFIG = Config(type_hooks={datetime: datetime.fromtimestamp})
