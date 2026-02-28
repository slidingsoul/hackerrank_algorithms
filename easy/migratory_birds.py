# migratory birds

def migratoryBirds(arr):
  sightings = [0, 0, 0, 0, 0]
  for i in range(len(arr)):
    sightings[arr[i] - 1] += 1
  max_occurence = 0
  minimum_id = 0
  for j in range(len(sightings) - 1, -1, -1):
    if sightings[j] >= max_occurence:
      max_occurence = sightings[j]
      minimum_id = j + 1
  return minimum_id

arr = [1, 4, 4, 4, 5, 3]

print(migratoryBirds(arr))