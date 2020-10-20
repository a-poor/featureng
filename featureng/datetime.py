
from typing import Union

import time
import datetime as dt

def is_weekend(d: Union[dt.datetime,dt.date]):
    return d.weekday() >= 5

def is_weekday(d: Union[dt.datetime,dt.date]):
    return not is_weekend(d)

def get_date(d: dt.datetime):
    return d.date()

def get_time(d: dt.datetime):
    return d.time()

def to_ordinal(d: dt.datetime):
    return d.toordinal()
    
