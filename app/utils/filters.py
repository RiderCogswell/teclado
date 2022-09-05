def format_date(date):
  return date.strftime('%m/%d/%y')

from datetime import datetime
print(format_date(datetime.now()))