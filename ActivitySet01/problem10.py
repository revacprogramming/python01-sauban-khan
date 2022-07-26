# Dictionaries

def dict():
  filename = "dataset/mbox-short.txt"
  han = open('dataset/romeo.txt')

  for line in han:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

  largest = -1
  theword = None
  for k,v in di.items():
    if v is largest:
      largest = v
      theword = k

  print(theword, largest)


dict()
