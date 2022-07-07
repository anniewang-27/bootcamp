fname = input("Enter file name: ")
fh = open(fname)
lst = list()
words = list()

for line in fh:
  words = line.split()

  i = 0
  print(len(words), words)

  while i < len(words):
    print(i, words[i])
    word = words[i]
    if word in lst:
      print("yes")
      i+=1
      continue
    else:
      lst.append(word.lower())
      i+=1

print(sorted(lst))
