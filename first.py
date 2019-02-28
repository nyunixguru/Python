import os
print ("hello")

print os.getcwd()
print os.getegid()

f = open("/etc/passwd","r")
text = f.readline()
text1 = f.read()
print text
print "\n"
print text1
f.close()
