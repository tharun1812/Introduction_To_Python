ans = ["b", "a", "d", "c", "e"]
crt = ["b", "c", "d", "c", "e"]

score = 0

for given, right in zip(ans, crt):
    if given == right:
        score += 1

print(f"Score: {score}/5")