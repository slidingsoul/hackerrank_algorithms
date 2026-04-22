# library fine

def libraryFine(d1: int, m1: int, y1: int, d2: int, m2: int, y2: int) -> int:
  NO_FINE = 0
  DAILY_FINE = 15
  MONTHLY_FINE = 500
  YEARLY_FINE = 10000
  returnDate = (d1, m1, y1)
  borrowDate = (d2, m2, y2)
  if borrowDate == returnDate or y1 < y2:
    return NO_FINE
  elif m1 == m2 and y1 == y2:
    numberOfDaysLate = d1 - d2
    if numberOfDaysLate < 0:
      numberOfDaysLate = 0
    return DAILY_FINE * numberOfDaysLate
  elif y1 == y2:
    numberOfMonthsLate = m1 - m2
    if numberOfMonthsLate < 0:
      numberOfMonthsLate = 0
    return MONTHLY_FINE * numberOfMonthsLate
  else:
    return YEARLY_FINE

def normalizeInput(returnDate: str, borrowDate: str) -> (int):
  d1, m1, y1 = map(int, returnDate.split(" "))
  d2, m2, y2 = map(int, borrowDate.split(" "))
  return d1, m1, y1, d2, m2, y2

returnDate = "6 6 2015"
borrowDate = "9 6 2016"
d1, m1, y1, d2, m2, y2 = normalizeInput(returnDate, borrowDate)

print(libraryFine(d1, m1, y1, d2, m2, y2))