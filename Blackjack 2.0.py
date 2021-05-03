import random

print('Welcome to Blackjack!')
know_to_play = input('Do you know how to play blackjack? (yes/no)').lower()

if know_to_play == 'yes':
  print("Awesome, then let's get started!")
elif know_to_play == 'no':
  print('I will deal you two cards at random at the start of the game. The objective of the game is to get the sum of your cards as close to 21 as possible without going over. Once you have both of your cards, you have the option to either "hit" or you can stand. When you hit, you get another card at random, so if you have a high sum with the first two cards, it could be risky to hit as you could go over 21. When you stand, you pass up your turn without receiving another card. If you receive an ACE, you can choose to either count it as one point or eleven (11) points, depending on how many points you have already. So, if your two first cards add up to 12 and you hit and get an ACE, you should choose to have the ACE count as one point because if it was eleven (11) points, you would be over 21, losing the game. After you go, the dealer then reveals his card, and if his two cards are 17 or more, he/she has to stand. If the dealer has less than 17, he/she picks cards until the sum is over 17. The one to get closest to 21 without going over wins.')

J = 10
Q = 10
K = 10

card_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, 'A'] * 4
random.shuffle(card_list)
your_cards = []
dealer_cards = []
your_cards_sum = 0
dealer_cards_sum = 0
game_over = False

def add_new_card():
    global your_cards_sum
    your_cards.append(random.choice(card_list))
    card_list.remove(your_cards[-1])
    if your_cards[-1] != 'A':
        your_cards_sum += your_cards[-1]

def handle_ace():
    global your_cards_sum
    if 'A' in your_cards:
        ace_spot = your_cards.index('A')
        ace_input = input("Do you want the ace to count as one or eleven? (one/eleven): ").lower()
        if ace_input == 'one':
            your_cards[ace_spot] = 1
            your_cards_sum += 1
            print(f'Your cards are {your_cards} with a sum of {your_cards_sum}')
        if ace_input == 'eleven':
            your_cards[ace_spot] = 11
            your_cards_sum += 11
            print(f'Your cards are {your_cards} with a sum of {your_cards_sum}')

# def add_dealer_card():
#     dealer_cards.append(random.choice(card_list))
#     card_list.remove(dealer_cards[-1])
#     return (f'The dealer\'s cards are {dealer_cards}')

# def check_for_ace_dealer():
#     for i in range(len(dealer_cards)):
#       if (dealer_cards[i] == 'A'):
#         if dealer_cards.index(i) == 0:
#           if dealer_cards[i + 1] >= 6:
#             dealer_cards[i] = 11
#           else:
#             dealer_cards[i] = 1
#         elif dealer_cards.index(i) == 1:
#           if dealer_cards[i - 1] >= 6:
#             dealer_cards[i] = 11
#           else:
#             dealer_cards[i] = 1
#     return (f'The dealer\'s cards are {dealer_cards} with a sum of {dealer_cards_sum}')

user_input = input("Press any key to draw two cards ('q' to quit): ")

while user_input != 'q' and not game_over:

    add_new_card()
    add_new_card()

    # for i in range(len(your_cards)):
    #     if your_cards[i] != 'A':
    #         your_cards_sum += your_cards[i]
    #     else:
    #         i += 1
    
    print(f'Your cards are {your_cards} with a sum of {your_cards_sum}')

    handle_ace()

    if your_cards_sum == 21:
        print("Blackjack! You win!")
        game_over = True
    
    hit_or_stand = input(f'You currently have {your_cards_sum} points, do you want to hit or stand? (hit/stand): ').lower()

    while hit_or_stand == 'hit':

        add_new_card()

        print(f"Your new cards are {your_cards} with a sum of {your_cards_sum}")

        handle_ace()

        if your_cards_sum > 21:
            print(f"You busted with {your_cards_sum} points!")
            game_over = True
            break
        if your_cards_sum == 21:
            print("Blackjack! You win!")
            game_over = True
            break

        hit_or_stand = input(f'You currently have {your_cards_sum} points, do you want to hit or stand? (hit/stand): ').lower()

    if hit_or_stand == 'stand':
        print(f"You chose to stand with {your_cards_sum} points.")
        break

print('Thanks for playing!')
