from datetime import datetime
from time import strftime
import time

dt = datetime(2019, 1, 1)
dt = datetime.now()
dt = datetime.strptime("2019/1/1", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())

print(f"{dt.year}/{dt.month}")
dt.strftime()
