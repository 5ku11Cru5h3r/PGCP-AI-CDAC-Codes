def main():
    num=int(input("Enter the  positive number: "))
   
    if num<0:
        print("Please retry the number")
        return

    limit=num//2
    d=2

    while d<=limit:
        if num%d==0:
            print(f"{num} is not a prime number, it is divisible by {d}")
            break
        d+=1

    if d>limit:
        print(f"{num} is a prime number")

            
     


main()      