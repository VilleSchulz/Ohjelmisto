

def deal():
    import random
    card1 = random.randint(1,14)
    return card1

def check(card):
    if card >= 21:
        return False
    elif card < 21:
        return True


input("Welcome to Ville´s legal BlackJack! Press Enter to continue!")
house_hand = []
your_hand = []
game_over = False
#Game start
user_input = input("You want to start new round? (y/n)").lower()
while user_input == "y":

    while not game_over:
        house_card = deal()
        house_hand.append(house_card)
        house_card = deal()
        house_hand.append(house_card)
        print(f"House's cards: {house_hand}")
        house_sum = sum(house_hand)
        print(f"House's total: {house_sum}")
        if not check(house_sum):
            game_over = True
            break
        input("Press Enter to deal a card!")
        your_card = deal()
        your_hand.append(your_card)
        your_card = deal()
        your_hand.append(your_card)
        print(f"Your cards: {your_hand}")
        your_sum = sum(your_hand)
        print(f"Your total: {your_sum}")
        if not check(your_sum):
            game_over = True
            break
        house_card = deal()
        house_hand.append(house_card)
        print(f"House's cards: {house_hand}")
        house_sum = sum(house_hand)
        print(f"House's total: {house_sum}")
        if not check(house_sum):
            game_over = True
            break
        input("Press Enter to deal a card!")
        your_card = deal()
        your_hand.append(your_card)
        print(f"Your cards: {your_hand}")
        your_sum = sum(your_hand)
        print(f"Your total: {your_sum}")
        if not check(your_sum):
            game_over = True
            break

    if your_sum == 21 or your_sum > house_sum and your_sum<= 21 or house_sum > 21:
        print("You WIN")
        house_hand.clear()
        your_hand.clear()
    else:
        print("You lose")
        house_hand.clear()
        your_hand.clear()
    user_input = input("You want to start new round? (y/n)").lower()
    if user_input == "y":
        game_over = False






