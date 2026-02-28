from datetime import datetime
date1=input("DD.MM.YYYY:")
date2=input("DD.MM.YYYY:")
date1=datetime.strptime(date1,"%d.%m.%Y")
date2=datetime.strptime(date2,"%d.%m.%Y")
difference=abs(date1-date2)
print("difference:",difference.days)