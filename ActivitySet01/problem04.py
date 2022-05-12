# Conditional Execution
sh=input("enter the hours:")
sr=input("enter the rate:")
fh= float(sh)
fr=float(sr)

if fh > 40:
  print("overtime")
  reg= fr * fh
  xp= fh * fr
  print("pay:",xp)
  otp= (fh-40) * (fr * 0.5)
  print(reg,otp)
  xp=reg + otp

else:
  print("regular")
  xp=fh*fr
print("pay:",xp)
  

    
  

