import pytz
from datetime import datetime, timezone, timedelta

date = datetime.now(pytz.timezone("Europe/Oslo"))
date2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(date)
print(date2)


date_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(date_oslo)
print(data_sao_paulo)