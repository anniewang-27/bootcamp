largest = 0
smallest = None
type = 0  #1 means int, 2 means float, -1 means string

def checkingVal(num):
  try:
    val = int(num)
    valType = 1
  except ValueError:
    try:
      val = float(num)
      valType = 2
    except ValueError:
      valType = -1
  return valType

while True:
  num = input("Enter a number: ")
  print(num)

  type = checkingVal(num)

  if (num == "done"):
    break
  elif type == -1:
    print("Invalid input")
  else:
    num = float(num)
    if (num>largest):
      largest = num
    if (smallest == None) or (num < smallest):
      smallest = num

print("---")
print ("Maximum:", int(largest))
print ("Minimum:", int(smallest))