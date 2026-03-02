# bill division

def bonAppetit(bill, k, b):
  refused = bill[k]
  actual = (sum(bill) - refused) / 2
  if actual == b:
    print("Bon Appetit")
  else:
    print(int(b - actual))

n = 4
k = 1
bill = [3, 10, 2, 9]
b = 7

bonAppetit(bill, k, b)