name = input("Enter your full name: ")

space = name.find(" ")

first = name[0:1].upper()
last = name[space+1:space+2].upper()
print("Your initials are:",first,".",last)
