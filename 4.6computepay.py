def computepay(h, r):
  if h<40.0:
    p = h*r
  else:
    diff = h-40.0
    p = (40.0*r)+(diff*(1.5*r))
  return p

hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
p = computepay(h, r)

print("Pay", p)