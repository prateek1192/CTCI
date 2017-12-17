import sys


#public check(str, data)
data = input("Please enter the string\n")
if ((len(set(data))) == len(data)):
    print ("True")
else:
    print ("False")

