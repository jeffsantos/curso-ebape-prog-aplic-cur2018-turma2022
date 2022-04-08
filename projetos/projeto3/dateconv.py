from datetime import datetime
from datetime import timedelta
import time

TIME_FORMAT='%Y-%m-%d %H:%M:%S'

def convert_to_unix(date_str):
	date_time_obj_brazil_tz = datetime.strptime(date_str+ "+0000", TIME_FORMAT + '%z')

	unixtime = int(time.mktime(date_time_obj_brazil_tz.timetuple()))

	return unixtime

def convert_from_unix(unix_date):
	date_time_obj_brazil_tz = datetime.fromtimestamp(unix_date)

	date_str = date_time_obj_brazil_tz.strftime(TIME_FORMAT + '%z')

	return date_str

