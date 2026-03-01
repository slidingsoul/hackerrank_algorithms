def isLeapYearGregorian(year):
  return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
  
def isLeapYearJulian(year):
  return year % 4 == 0
    
def dayOfMonth(month, year):
  if month == 2 and year == 1918:
    return 15
  if month == 2:
    if (year <= 1917 and isLeapYearJulian(year)) or (year >= 1919 and isLeapYearGregorian(year)):
      return 29
    else:
      return 28
  else:
    if (month % 2 == 1 and month <= 7) or (month % 2 == 0 and month > 7):
      return 31
    else:
      return 30
def dayOfProgrammer(year):
  month = 1
  days = 0
  addend = 0
  while days + addend <= 256:
    addend = dayOfMonth(month, year)
    month += 1
    days += addend
  return(f"{256 - days}.{month:02d}.{year}")
