string = input().lower()
vowels = "aeiouyäö"
count = 0
for character in string:
    if character in vowels:
        count += 1


print(f"Number of vowels: {count}")
