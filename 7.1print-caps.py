fname = input("Enter file name: ")
fh = open(fname)

fr = fh.read()
print(fr.upper())
