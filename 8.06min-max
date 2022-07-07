lst = list()
condition = True
type = 0

while condition == True:
  num = input("Enter a number:")
  try:
    valFloat = float(num)
    lst.append(num)
  except:
    if num == "done":
      condition = False
      break
    else:
      print("invalid input")
      continue


lstSort = sorted(lst)
print("The minimum is:", lstSort[0])
print("The maximum is", lstSort[len(lstSort)-1])


