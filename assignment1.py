import a1

print(a1.seconds_difference(1800.0, 3600.0))
print(a1.seconds_difference(3600.0, 1800.0))
print(a1.seconds_difference(1800.0, 2160.0))
print(a1.seconds_difference(1800.0, 1800.0))

print(a1.hours_difference(1800.0, 3600.0))
print(a1.hours_difference(3600.0, 1800.0))
print(a1.hours_difference(1800.0, 2160.0))
print(a1.hours_difference(1800.0, 1800.0))

print (a1.to_float_hours(0, 15, 0))
print (a1.to_float_hours(2, 45, 9))
print (a1.to_float_hours(1, 0, 36))

print (a1.get_hours(3800))
print (a1.get_minutes(3800))
print (a1.get_seconds(3800))

print (a1.time_to_utc(+0.5, 12.0))
print (a1.time_to_utc(+1, 12.0))
print (a1.time_to_utc(-1, 12.0))
print (a1.time_to_utc(-11, 18.0))
print (a1.time_to_utc(-1, 0.0))
print (a1.time_to_utc(-1, 23.0))
# ^ last test in time_to_utc
