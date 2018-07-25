#File Handling
fo=open("filetest.txt","w")
fo.write("This is written by test file handler program..!\n")
fo=open("filetest.txt","r")
str =fo.read(100)
print ("Name of the file is: ",fo.name)
print ("File is Read: ",str);
fo.close()