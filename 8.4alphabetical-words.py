fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  words = line #so that i am able to modify it
  count = line.count(" ")
  while count>0:
    word = words[:words.index(" ")]
    lst.append(word.lower())
    words = words[words.index(" ")+1:]
    count-=1

print(sorted(lst))