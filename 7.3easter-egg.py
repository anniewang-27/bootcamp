fname = input("Enter file name: ")
count = 0

try:
  fh = open(fname)
  for line in fh:
    if line.startswith("Subject:"):
      count +=1
    else:
      continue
  print("The total number of subject lines is:", count)
except:
  if fname == "na na boo boo":
    print("YOU'VE BEEN PUNKED!!")
  else:
    print("error opening the file")
