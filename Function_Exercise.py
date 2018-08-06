'''
Functions HomeWork
1. define a function to find volumne of sphere
'''
radius = float(input("Enter sphere's radius for volume calculation:"))
def volume_sphere(radius):
  return (4/3 * 22/7 * radius ** 3)

print (f'the volume of sphere is: {volume_sphere(radius)}')
print ('the volume of sphere is: {0:.2f}'.format(volume_sphere(radius)))


#----------------------------------------------------

'''
Palindrome check
'''
pstring=input("Enter string for palindrome check:")
def palindrome(pstring):
  return pstring == pstring[::-1]

print(f'Given String is: {palindrome(pstring)}')