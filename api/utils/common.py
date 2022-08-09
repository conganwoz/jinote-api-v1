from datetime import datetime, timezone
import pytz

def is_empty(value):
    return value == 'undefined' or value == 'null' or value == '' or (value is None)

def convert_to_vn_time(utc_dt):
    if is_empty(utc_dt):
        return None
    return utc_dt.astimezone(pytz.timezone('Asia/Bangkok'))

def format_datetime(dt):
    if is_empty(dt):
        return None
    return dt.strftime('%H:%M:%S %d-%m-%Y')

