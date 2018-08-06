'''
name = 'Jose'
occupation = 'manager'
print(f'{name} is Manchester United {occupation}')

# String formating
pi = 22/7
print('Pi value is {p:1.4f}'.format(p=pi))

#list
alpha_list = ['a','c','g','b','d','f','e']
num_list = [5,3,1,2,4,7,6]
multi_list = [8,"quick",3.256]

#list Indexing and Slicing
print (alpha_list[3])
print (num_list[2:])

#list functions

alpha_list.sort()
num_list.sort()
print(alpha_list)
print(num_list)

num_list.reverse()
print(num_list)

print("multi list before append {}".format(multi_list))
multi_list.append("End")
print("multi list after append {}".format(multi_list))
multi_list.insert(0,"Start")  #indexing insert
print("multi list after indexing append {}".format(multi_list))
multi_list.pop()
print("multi list after pop {}".format(multi_list))
multi_list.pop(0)  #indexing pop
print("multi list after indexing pop {}".format(multi_list)) 

mgr_names =[]
name = input("Enter Manager name:")
print("Manger name is : ",name)
mgr_names.append(name)
print("Manager name from list : ",mgr_names)
'''













