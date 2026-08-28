def main():
    n1=int(input("Enter the num1:"))
    n2=int(input("Enter the num2:"))
    op=input("Ënter the operator:")
    if op=='+':
        print("Result :",n1+n2)
    elif op=='-':
        print("Result :",n1-n2)
    elif op=='*':
        print("Result :",n1*n2)
    elif op=='/':
        print("Result:",n1/n2)
    else:
        print("PLease enter the valid operator")

   
main()    