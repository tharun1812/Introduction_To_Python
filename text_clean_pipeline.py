line_count = 0

with open("raw.txt", "r") as file:
    with open("clean.txt", "w") as output:
        for line in file:
            cleaned_line = " ".join(line.split()).lower()

            if cleaned_line == "":
                continue

            line_count += 1
            output.write(f"{line_count}. {cleaned_line}\n")

print(f"Lines kept: {line_count}")