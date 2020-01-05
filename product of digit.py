kk = int(input())
temp = kk
product = 1;
while(temp != 0):
	product = product * (temp % 10);
    temp = int(temp / 10)
print("\nProduct of all digits in", kk, ":", product)
