def main():
    n=input().split()
    shift_by=int(input("Enter the shift"))
    for word in n:
        new_word=" "
        for ch in word:
            new_word+=chr(ord(ch)+shift_by)
        print(new_word)

main()