def main():
    email=input("Ënter your email:")
    if '@' not in email:
        print("Invalid email")
    #for i in range(len(email)):
    index_symbol=email.find('@')
    index_symbol+=1
    print(email[index_symbol:])





main()    