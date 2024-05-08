file = open("E:\\jupi.txt")
grade = 0
count = 0
text = file.read()
print(text)
words = text.split()
for line in text:
    line.split(" ")
    if line.isdigit():
        print(line)
        #grade += int(line)
        #count += 1
print(words)
print(f"Average grade is : {grade / count}")

for i in words:
