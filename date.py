#dates, times, datetimes, timezones, timedeltas
#naive date times - doesnt include time zone and day light savings
#aware date time - includes time zones and day light savings

import datetime

d = datetime.date(2019, 11, 3)
print(d)

currentDate = datetime.date.today()
print(currentDate)
print(currentDate.year)

#timedelta - difference between two dates and time
#adding gets future date whereas subtracting gets past date
tdelta = datetime.timedelta(days=30)
print(f'Next date for paying subscription is: {currentDate + tdelta}')

#TIME
t = datetime.time(10, 30, 10, 10000)
print(t)


#DATETIME
dt = datetime.datetime(2019, 11, 3, 10, 30, 10, 10000)
tdelta2 = datetime.timedelta(days=30)
print(dt)
#calculate date difference with time
print(dt + tdelta2)

dt_today = datetime.datetime.today()
print(dt_today)     # prints current datetime with no timezone


# thou it is recommended to use the PYTZ LIBRARY IF YOU ARE DEALING WITH TIMEZONE
#pip install pytz

import pytz
dt_tz = datetime.datetime(2019, 11, 4, 8, 53, 4, tzinfo=pytz.UTC)
print(dt_tz)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

# converting this timezone to another
dt_kampala = dt_utcnow.astimezone(pytz.timezone('Africa/Kampala'))
print(f'Kampala timezone is: {dt_kampala}')

# format code ---- python datetime documentation
print(dt_kampala.strftime('%B %d, %Y'))

# list of timezones
# for tz in pytz.all_timezones:
#     print(tz)
