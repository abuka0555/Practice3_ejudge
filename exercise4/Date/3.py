from datetime import datetime
current_date=datetime.now()
withoutMicrosec=current_date.replace(microsecond=0)
print("current_date:",current_date)
print("withoutMicrosec:",withoutMicrosec)