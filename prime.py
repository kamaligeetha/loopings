n=int(input())
if n>1:
    for k in range(2, n):
        if(n % k)==0:
            print('not a prime number')
            break
    else:
        print('prime number')
else:
    print('not a prime number')
