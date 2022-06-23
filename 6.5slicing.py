text = "X-DSPAM-Confidence:    0.8475"

positions = [text.find("0"), text.find("1"), text.find("2"), text.find("3"), text.find("4"), text.find("5"), text.find("6"), text.find("7"), text.find("8"), text.find("9")]

pos = None #smallest position of a number
for num in positions:
  if (num == -1):
    continue
  elif (pos == None) or (num < pos):
    pos = num

print(pos)

num = text[pos:]
print(str(num))