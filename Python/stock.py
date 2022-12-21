stock = int(input("Please enter an initial stock level: "))
months = int(input("Please enter the number of month to plan: "))

sales = []
for i in range(months):
    sales.append(int(input("Please enter the planned sales quantity: ")))

print("The resulting production quantities are: ")
prod = 0

for i in range(months):
    stock = stock-sales[i]
    if stock <= 0:
        prod = 0 - stock
        stock = 0
    print("Production quantity month ", i+1, " - ", prod, " Stock has left: ", stock)
