'''
Create a list comprehension for the integer 1-100 with following condition.
if num divided by 3 write Fizz
if num divided by 5 write Buzz
if num divided by both write FizzBuzz
els ewrite num
'''

mylist = [num for num in range(1,101)]
resultlist = ['FizzBuzz' if (num%3==0 and num%5==0) else 'Fizz' if (num%3==0) else 'Buzz' if (num%5==0) else num for num in mylist]
print(resultlist)

'''
Create 4 lists from the resultList using (num,Fizz,Buzz and Fizzbuzz) using loop and statement
'''

numlist = []
fizzlist = []
buzzlist = []
fizbuzzlist = []
for x in resultlist:
  if x == 'Fizz':
    fizzlist.append(x)
  elif x == 'Buzz':
    buzzlist.append(x)
  elif x == 'FizzBuzz':
    fizbuzzlist.append(x)
  else:
    numlist.append(x)
    continue
  
print(f"numlist is: {numlist}")
print(f"fizzlist is: {fizzlist}")
print(f"buzzlist is: {buzzlist}")
print(f"fizbuzzlist is: {fizbuzzlist}")

'''
Create list a of the first three letter of the words available in this senetence
'''

st = 'Create list a of the first three letter of the words available in this senetence'
stlist = [word[0:3] for word in st.split()] 
print (stlist)

'''
Create a list of even number words available in this sentence
'''

st1 = 'Create a list of even number words available in this sentence'
st1list = [word for word in st1.split() if len(word)%2 == 0]
print(st1list)