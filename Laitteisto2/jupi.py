import re
file = open("E:\\jupi.txt")
all_numbers = 0
count = 0
text = file.read()
print(text)
words = text.split()
for i in words:
    number = re.sub(r'[^\d]', '', i)
    if number:
        all_numbers += int(number)
        count += 1

average = all_numbers/count
print(f"\n\nJupi teki viikossa töitä {all_numbers}h ja keskimäärin päivässä {average}h ")

