import re

# Read the input file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Define thresholds for each color
thresholds = {"red": 12, "green": 13, "blue": 14}

# Remove lines containing cubes with numbers larger than the specified thresholds
filtered_lines = [
    line.strip()  # remove leading/trailing whitespaces
    for line in lines
    if not any(
        int(count) > thresholds[color]
        for count, color in re.findall(r'(\d+) (\w+)', line)
        if color in thresholds
    )

]
sum = 0
for line in filtered_lines:
    colon_index = line.find(":")
    result = line[:colon_index].strip()
    result2 = result.replace("Game", "").strip()
    #print(result2)
    sum += int(result2)

print(sum)