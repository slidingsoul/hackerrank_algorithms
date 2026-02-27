# time conversion

def timeConversion(s):
  hour, minute, temp_second = s.split(":")
  hour = int(hour)
  minute = int(minute)
  second = temp_second[:-2]
  second = int(second)
  mer_indicator = temp_second[-2:]
  if mer_indicator == "PM" and hour == 12:
    pass
  elif mer_indicator == "PM":
    hour += 12
  if mer_indicator == "AM" and hour == 12:
    hour = 0
  return f"{hour:02}:{minute:02}:{second:02}"

def timeConversion_v2(s):
  time_part, mer_indicator = s[:-2], s[-2:]
  hour, minute, second = map(int, time_part.split(":"))
  if mer_indicator == "PM" and hour != 12:
    hour += 12
  elif mer_indicator == "AM" and hour == 12:
    hour = 0
  return f"{hour:02}:{minute:02}:{second:02}"

example = "12:45:54PM"

print(timeConversion_v2(example))