'''
PRIME NUMBER FINDER
'''

num = int(input("Enter number for prime check :"))

def prime_finder(num):
  if num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        print (f"{num} is not a prime number")
        print (i,"times",num//i,"is ",num)
        break
    else:
      print (f"{num} is a prime number")
  else:
    print (num, " is not a prime number")

prime_finder(num)

'''
FIBONACCI SERIES
'''
num = int(input("Enter number for Fibonacci series:"))

def recur_fibonacci(num):
  '''
  Recursive fibonacci function
  '''
  if num <=1:
    return num
  else:
    return (recur_fibonacci(num-1) + recur_fibonacci(num-2))

if num <=0:
  print ("Enter Positive Interger for the finonacci series")
else:
  print ("Fibonacci Series:")
  for i in range(num):
    print(recur_fibonacci(i))

'''
Returning Only Even Numbers in the List using *args
'''
evennums =[]
def myfunc(*args):
  for i in range(len(args)):
    if (args[i]%2 ==0):
      evennums.append(args[i])
    else:
      continue
  return evennums
 
print(myfunc(1,2,3,4,5,6))

'''
Changing alternate character to upper and lower in a string using **kwargs
'''

def myfunc(**kwargs):
  st1=[]
  mystring=kwargs.pop('st')
  for char in range(len(mystring)):
    if char%2==0:
      st1.append(mystring[char].lower())
      continue
    else:
      st1.append(mystring[char].upper())
      continue
  return " ".join(st1)

print(myfunc(st="Thisisit"))
#------------------------OR---------------------------
def myfunc(mystring):
    st1=[]
    for char in range(len(mystring)):
        if char%2==0:
            st1.append(mystring[char].lower())
            continue
        else:
            st1.append(mystring[char].upper())
            continue
    return ''.join(st1)

print(myfunc("Anthropomorphism"))


'''
Lesser of two numbers
1. return lesser if both even
2. return greater if one of the number is odd
'''
result =None
def lesser_of_two_even(a,b):
  if ((a%2 == 0) and (b%2==0)):
    if a < b:
      result = a
    else:
      result = b
  else:
    if a > b:
      result = a
    else:
      result = b
  return result

print(lesser_of_two_even(2,4))
print(lesser_of_two_even(3,5))
print(lesser_of_two_even(2,3))

#-------------------OR-------------------------------
def lesser_of_two_even(a,b):
  if (a%2==0 and b%2==0):
    return min(a,b)
  else:
    return max(a,b)

print(lesser_of_two_even(2,4))
print(lesser_of_two_even(3,5))
print(lesser_of_two_even(2,3))

'''
SUMMER 69 Problem
'''
def summer_69(arr):
  total=0
  add=True
  for num in arr:
    while add:
      if num!=6:
        total+=num
        break
      else:
        add = False
    while not add:
      if num!=9:
        break
      else:
        add=True
        break
  return total

print(summer_69([1,3,6,5,9]))


