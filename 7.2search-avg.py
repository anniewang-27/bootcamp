fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0

for line in fh:
  #print(line)
  if not line.startswith("X-DSPAM-Confidence:"):
    continue
  else:
    numStr = (line[19:])
    numFlo = float(numStr.rstrip())
    count +=1
    tot = tot + numFlo

print("The average is:", (tot/count))
print("Done")