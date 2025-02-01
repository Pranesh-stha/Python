email = input("Enter your email address: ")

at = email.find("@")

print("your domain is:", email[at+1:])