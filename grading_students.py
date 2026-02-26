def gradingStudents(grades):
  n = len(grades)
  for i in range(n):
    if grades[i] < 38:
      grades[i] = grades[i]
    elif (((grades[i] // 5) + 1) * 5) - grades[i] < 3:
      grades[i] = (((grades[i] // 5) + 1) * 5)
  
  return grades

grades = [73, 67, 38, 33]
print(gradingStudents(grades)) # 75 67 40 33