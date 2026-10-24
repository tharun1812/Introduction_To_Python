scores = [12, 17, 9, 15, 14]

best = -1
best_position = 0
for pos, s in enumerate(scores, start=1):
    if s > best:
        best = s
        best_position = pos

print(f"BEST: {best} student {best_position}")