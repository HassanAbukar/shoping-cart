#  shoping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter food you want to buy (q to quite): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)


print(F"------------Your Cart------------")

for food in foods:
    print(food, end=' ')

for price in prices:
    total += price

print()
print(f"Your Total is ${total}")