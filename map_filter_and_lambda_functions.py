'''
lambda,map and filter functions
'''

def square(num):
  return num ** 2

def check_even(num):
  return num%2 == 0

def check_string(mystring):
  for string in mystring:
    if len(mystring)%2 == 0:
      return "EVEN"
    else:
      return string[0]

mynums = [1,2,3,4,5]
my_name =['Saran','Guru','Prasath']

#----------map function-----------------------------
'''
map and filter functions used to iterate the function in single line 
'''
map(square,mynums)  # Return only map address
print (list(map(square,mynums)))
print (list(map(check_string,my_name)))

#------------------filter function-------------------
'''
Filter function will work based on boolean True or false value.
'''
filter(check_even,mynums)   # Returns only filter func address
print (list(filter(check_even,mynums)))

#--------------lambda function------------------------
'''
lambda function is used to eliminate the unnecessary function definitions which mostly used for single time 
'''
print ("Lambda function")
print(list(map(lambda num: num **2,mynums)))  #this line don't use square function
print(list(filter(lambda num: num%2==0,mynums))) # this line don't use check_even function