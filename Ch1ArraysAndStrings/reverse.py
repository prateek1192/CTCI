import sys

s = input("Please enter the string to be reversed\n")
rev=""
for i in s:
    rev = i + rev
print (rev)

