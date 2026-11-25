direction = input("Convert to (C/F): ").upper()

temperature = float(input("Temperature: "))

if direction == "F":
    c = (temperature - 32) * 5 / 9
    f = temperature
    print(f"{c:.1f}°C = {f:.1f}°F")

elif direction == "C":
    f = temperature * 9 / 5 + 32
    c = temperature
    print(f"{c:.1f}°C = {f:.1f}°F")

else:
    print("Unknown direction")