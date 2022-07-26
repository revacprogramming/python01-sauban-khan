# Lists
def fuc():
  filename = open("dataset/romeo.txt")
  lst=list(filename)
  l=[]
  for word in lst:
    for letter in word:
      if letter != l:
        l.append(letter)
        l.sort()
        
  print(l)
        

fuc()
