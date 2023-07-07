rows = int(input("How many rows?: "))
cols = int(input("How many columns?: "))
symbol = input("What symbol?: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end="")
    print()