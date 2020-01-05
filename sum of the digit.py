mk = int(input())
Sum = 0
 
while(mk > 0):
    Rem = mk % 10
    Sum = Sum + Rem
    mk = mk //10
 
print("\n Sum of the digits  = %d" %Sum)
