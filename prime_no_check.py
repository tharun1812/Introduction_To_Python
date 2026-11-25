n = int(input("Number: "))

is_prime = n >= 2

for d in range(2, n):

    if n % d == 0:
        is_prime = False
        print(f"{n} is divisible by {d}")
        break

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")