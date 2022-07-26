# Files

def file():
  f=open("dataset/mbox-short.txt")
  count = 0
  sum=0
  for line in f:
      if line.startswith('X-DSPAM-Confidence'):
          count = count + 1
          x=float(line[20::1])
          sum=sum+x
  print('There were', count, 'subject lines in', "dataset/mbox-short.tx")
  avg=sum/(count)
  print("Average spam confidence: ",avg)
  

file()
