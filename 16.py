def gen_timestamp():
year = random.randint(1980, 2015)
month = random.randint(1, 12)
day = random.randint(1, 28)
hour = random.randint(1, 23)
minute = random.randint(1, 59)
second = random.randint(1, 59)
microsecond = random.randint(1, 999999)
date = datetime.datetime(year, month, day, hour,minute, second,microsecond).isoformat(" ")
return date
