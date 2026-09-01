game=[["." for i in range(5) ]for j in range(5)]
game[2][3]="F" 
row=int(input("Enter the row"))
col=int(input("Enter the column"))

game[row][col]='S'

if row==2 and col==3:
    print("Yum!snake ate the food")

for row in range(5):
    for col in range(5):
        print(game[row][col],end=" ")
    print()