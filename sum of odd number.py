msd = int(input())
sum = 0
 
for k in range(1, msd+1):
    if(k % 2 == 1):
        print("{0}".format(k))
        sum = sum + k
 
print("The Sum of Even Numbers are 1 to {0} = {1}".format(k,sum))
