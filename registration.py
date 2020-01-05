userid=str(input())
email=str(input())

#EMAIL
mail=[i for i in email]
if mail[0].isdigit():
	print('invaliddd')
elif mail[6]>='@' and '@' in mail:
	lenn=len(mail)-5
	if mail[lenn+1]=='.' and mail[lenn+2]=='c' and mail[lenn+3]=='o' and mail[lenn+4]=='m':print('valid')
	else:
		print('invalid')
else:
	print('invalid')

#PASSWORD
password=str(input())
pasword1=[word for word in password]
if len(pasword1)>=8 and len(pasword1)<=15:
	if pasword1[0].isupper():
		count=0
		for i in range(0,len(pas)):
			mid=ord(pasword1[i])
			if (mid>=27 and mid<=47) or (mid>=58 and mid<=64):
				count=count+1
		if count==1:
			count1=0
			for j in range(0,len(pasword1)):
				nn=ord(pasword1[j])
				if (nn>=48 and nn<=57):
					count1=count1+1
			if count1>0:
				print('valid')
			else:
				print('Enter the valid password')
		else:
			print('Enter the valid password')
	else:
		print('Enter the valid password')
else:
	print('password is too short')
