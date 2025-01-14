file = open("E:\\arvosanat.txt")
grade = 0
count = 0
text = file.read()
for line in text:

    if line.isdigit():
        print(line)
        grade += int(line)
        count += 1

print(f"Average grade is : {grade / count}")

