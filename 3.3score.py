score = input("Enter Score: ")
s = float(score)

if s>= 0.9 and s<=1.0:
  val = "A"
elif s>=0.8:
  val = "B"
elif s>=0.7:
  val = "C"
elif s>0.6:
  val = "D"
elif s<0.6 and s>=0.0:
  val = "F"
else:
  print("This score is not in range")

print("Your score is " + val)
