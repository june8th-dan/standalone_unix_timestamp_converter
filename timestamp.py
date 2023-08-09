block_4y = [365, 730, 1096, 1461, 0]
month_norm = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365, 0]
month_leap = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366, 0]

def timestamp_to_readable(timestamp):
    hms = timestamp % 86400
    timestamp //= 86400
    year = 1970 + timestamp // 1461 * 4
    timestamp %= 1461
    for i in range(4):
        if timestamp < block_4y[i]: break
    year += i
    timestamp -= block_4y[i - 1]
    if i == 2: _month = month_leap
    else: _month = month_norm
    for i in range(12):
        if timestamp < _month[i]: break
    month = i + 1
    day = timestamp - _month[i - 1] + 1
    hour = hms // 3600
    hms %= 3600
    minute = hms // 60
    second = hms % 60
    return year, month, day, hour, minute, second

def readable_to_timestamp(year, month, day, hour, minute, second):
    timestamp = 0
    for i in range(year - 1970):
        if i % 4 == 0: timestamp += 31622400
        else: timestamp += 31536000
    if year % 4 == 0: _month = month_leap
    else: _month = month_norm
    timestamp += _month[month - 1] * 86400
    timestamp += (day - 1) * 86400
    timestamp += hour * 3600
    timestamp += minute * 60
    timestamp += second
    return timestamp

print(timestamp_to_readable(1691600692))
print(readable_to_timestamp(2023, 8, 10, 0, 4, 52))