with open("a.txt", "r") as file:
    words_a = file.read().split()

with open("b.txt", "r") as file:
    words_b = file.read().split()

unique_a = set(words_a)
unique_b = set(words_b)

print(f"Words in a.txt: {len(words_a)}")
print(f"Unique words in a.txt: {len(unique_a)}")

common_words = unique_a & unique_b
only_a = unique_a - unique_b

print("Common words:", sorted(common_words))
print("Only in a.txt:", sorted(only_a))