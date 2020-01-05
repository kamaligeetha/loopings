s1=input()
c1=0
c2=0
for i in range(0,len(s1)):
  if(s1[i]=="("):
    c1=c1+1
  elif(s1[i]==")"):
    c2=c2+1
if(c1==c2):
  print("yes")
else:
  print("no")
