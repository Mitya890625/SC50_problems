total = 0
dict = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
print("What would you like to order?")
while True:
    purchase = input()
    if purchase in dict:
        total += dict[purchase]
    if purchase == 'q':
        break
print(f"Your order will be {total}$")

