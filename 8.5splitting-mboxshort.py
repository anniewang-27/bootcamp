fname = input("Enter a file name: ")
if len(fname) < 1:
  fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
  if line.startswith("From"):
    if line.startswith("From:"):
      continue
    else:
      words = line.split()
      print(words[1])
      count+=1
  else:
    continue

print("the number of times a line started with From was", count)
