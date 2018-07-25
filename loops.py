n=int(input("Enter any numeric number: "))
for i in range(n):
	print ("executing for loop", i)

print ("Number after for: ",n)
	
while n>0:
	print ("executing while loop", n)
	n=n-1
	
print ("Number after while: ",n)

n=int(input("Enter any numeric number for nested if else: "))

if (n>=5):
	print ("Number is greater than or equal to 5")
elif (n>0 and n<5):
	print ("Number is between 0 and 5")
else:
	print ("Number is less than or equal to 0")



