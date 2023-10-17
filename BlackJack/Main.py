

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
house_cards = []
your_cards = []
game_over = False
#Game start
house_card = deal()
house_cards.append(house_card)
house_card = deal()
house_cards.append(house_card)
print(f"House's cards: {house_cards}")
house_sum = sum(house_cards)
print(f"House's total: {house_sum}")
check(house_sum)
input("Press Enter to deal a card!")
your_card = deal()
your_cards.append(your_card)
print(f"Your cards: {your_cards}")
your_sum = sum(your_cards)
print(f"Your total: {your_sum}")
check(your_sum)

    while not game_over:
        house_card = deal()
        house_cards.append(house_card)
        print(f"House's cards: {house_cards}")
        house_sum = sum(house_cards)
        print(f"House's total: {house_sum}")
        check(house_sum)
        input("Press Enter to deal a card!")
        your_card = deal()
        your_cards.append(your_card)
        print(f"Your cards: {your_cards}")
        your_sum = sum(your_cards)
        print(f"Your total: {your_sum}")
        check(your_sum)
    if your_sum == 21 or your_sum > house_sum and your_sum<= 21:
        print("You win!")

    elif your_sum > 21 or house_sum == 21:
        print("You lose")



