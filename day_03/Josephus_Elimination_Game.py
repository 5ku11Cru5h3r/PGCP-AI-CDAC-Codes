n = int(input("Ënter no. of soldiers:"))
k = int(input("Enter the interval:"))

soldiers = list(range(1, n + 1))

print(f"soldiers activated:{soldiers}")

index = 0

while len(soldiers) > 1:
    index = (index + k - 1) % len(soldiers)
    eliminated = soldiers.pop(index)
    print(f"Eliminates soldier {eliminated}" + f"Remainining soldier: {soldiers}")

print(f"The sole soldier:{soldiers[0]}")
