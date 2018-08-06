def name_function(name='Name'):
  print("Hello " + name)

name_function('Saran')
name_function()

def add_function(num1,num2):
  return (num1 + num2)

result = add_function(23,59)
print(result)

'''
PROBLEM 1: check word dog in a sentence using function
'''

def dog_check(word):
  return 'dog' in word.lower()

print (dog_check('my Dog ran away'))
print (dog_check('my cat ran away'))

'''
PROBLEM 2: PIG_LATIN
if word starts with vowel add ay in last else take and add firstletter + ay at last
apple --- appleay
word --- ordway
'''

def pig_latin(word):
  # checking the vowel letter
  if word[0] in 'aeiou':
    pig_word = word + 'ay'
  else:
    pig_word = word[1:] + word[0] + 'ay'
  return pig_word

print (pig_latin('apple'))
print (pig_latin('word'))