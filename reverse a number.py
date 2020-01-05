mm = int(input())
Rev = 0
while(mm > 0):
    Rem = mm %10
    Rev = (Rev *10) + Rem
    mm = mm //10
print("\n Reverse number is = %d" %Rev)
