import re
def validate_email(email):
    r=r"^[a-z0-9._]+@[a-z0-9]+\.(edu|res\.in)$"
    email_checker=re.match(r,email)
    if email_checker== None:
        return False
    else:
        return True

print(validate_email("aryak@gmail.edu"))
print(validate_email("arham.khan@cdac.res.in"))  # Output: True
print(validate_email("lisa_stud12@mit.edu"))      # Output: True
print(validate_email("vinod@gmail.com"))          # Output: False (invalid suffix)
print(validate_email("ALICE@college.edu"))        # Output: False (contains uppercase letters)
print(validate_email("bob@mit.edu.com"))          # Output: False (does not end in .edu or .res.in)
