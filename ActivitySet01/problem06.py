def computepay(hours,rate):
  
  if hours>40:
    x = rate * hours
    y = (hours-40.0) * (rate * 0.5)
    Pay = x+y
    
  else:    
    pay= hours * rate
    
  return Pay
    
hrs=float(input("enter hours:"))
rate=float(input("enter rate:"))

xp=computepay(hrs,rate)

print("Pay",xp)
