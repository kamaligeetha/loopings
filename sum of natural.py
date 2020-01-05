num=int(input())
if num < 0:
   print("Enter a positive number")
else:
   ss = 0
   while(num > 0):
       ss += num
       num -= 1
   print("The ss is", ss)
