# importing the datetime module
from datetime import datetime

# Printing the current_date as the date object itself.
date_str = '2022-12-01 01:00:00'
date_format = '%Y-%m-%d %H:%M:%S'

date_obj = datetime.strptime(date_str, date_format)
print("Original date and time object:", date_obj)

print("Date and Time in Integer Format:",
      int(date_obj.strftime("%Y%m%d%H%M%S")))