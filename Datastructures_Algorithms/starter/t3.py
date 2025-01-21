amount = int(input())
dictionary = {}
i = 1
while i <= amount:
    dictionary.update({i:i**2})
    i += 1

print(dictionary)

