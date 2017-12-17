import sys

s = input("Please enter the string\n")
ascii = []
for i in range(0,255):
    ascii.append(0)
for i in range(0,len(s)):
    c = s[i]
    ascii[ord(c)] = ascii[ord(c)] + 1
    if ascii[ord(c)] > 1:
        print ("Repeating character found "+c)
