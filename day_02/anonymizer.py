def main():
    full_name=input("Ënter your full name: ").strip().split()
    formatted_name='.'.join(name[0].upper() for name in full_name[0:2])+'.'
    print(formatted_name+full_name[2])
main()    