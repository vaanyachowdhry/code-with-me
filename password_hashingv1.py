import hashlib

#DAY 3: TODAY I WILL LEARN HOW TO hash A PASSWORD
#ALONG WITH VARIOUS NEW FUNCTIONS OF PYTHON

while True:
 password = input("Enter your password: ")
 pw_length = len(password)>=8 and len(password)<32
 pw_upper = any (char.isupper() for char in password)
 pw_digit = any (char.isdigit() for char in password)
 pw_lower = any (char.islower() for char in password)



 errors = []

 if pw_length == False:
   errors.append("\nLength needs to be between 8 to 32 characters.")
 if pw_upper == False:
   errors.append("\nNo uppercase letter found. Please add atleast one uppercase alphabet")
 if pw_lower == False:
   errors.append("\nNo lowercase letter found. Please enter atleast one lowercase alphabet")
 if pw_digit == False:
   errors.append("\nNo digits found. Please enter atleast one number")
 if errors:
    print("Weak password. Please change the following: ")
    for err in errors:
     print(err)
 else:
    print("Hashing password...")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print(hashed_password)
    break