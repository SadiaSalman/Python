print("What you want to check for palindrome?")
a = input()
c = a[ : : -1]
	
if c == a :
	print('It is a palindrome')
	
else:
	print('It is not a palindrome')
print("What you want to check for palindrome?")
a = input()
while True:
	if a.replace(" ", "") != "":
		c = a[ : : -1]
			
		if c == a :
			print('It is a palindrome')
			break
			
		else:
			print('It is not a palindrome')
			break
	else:
		a=input("Please give some value:\n")
