with open("products.csv", "r") as file:
    lines = file.readlines()

total_value = 0
highest_value = 0
highest_product = ""

print(f"{'Product':<12} {'Price':>8} {'Qty':>5} {'Value':>10}")
print("-" * 39)

for line in lines[1:]:
    name, price, qty = line.strip().split(",")

    value = float(price) * int(qty)
    total_value += value

    print(f"{name:<12} {float(price):>8.2f} {int(qty):>5} {value:>10.2f}")

    if value > highest_value:
        highest_value = value
        highest_product = name

print("-" * 39)
print(f"{'Total':<27} {total_value:>10.2f}")
print(f"Highest value product: {highest_product} ({highest_value:.2f})")