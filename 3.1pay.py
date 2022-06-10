hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
pay = 0

if h<40.0:
  pay = h*r
else:
  diff = h-40.0
  pay = (40.0*r)+(diff*(1.5*r))

print("The final pay is " + str(pay))