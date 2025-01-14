sum = 0
while True:
    number = input()
    if number == "0":
        break

    try:
        number = float(number)
        sum +=number
        print(f"The total is now {sum}")
    except ValueError:
        print("That wasn’t a number.")

print(f"The grand total is {sum}")