from datetime import datetime,timedelta
current_date=datetime.now()
tomorrow=current_date+timedelta(days=1)
yesterday=current_date-timedelta(days=1)
print("tomorrow:",tomorrow)
print("current_date:",current_date)
print("yesterday:",yesterday)