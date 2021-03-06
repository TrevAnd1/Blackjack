import random

print('Welcome to Blackjack!')
know_to_play = input('Do you know how to play blackjack? (yes/no)').lower()

if know_to_play == 'yes':
  print("Awesome, then let's get started!")
elif know_to_play == 'no':
  print('I will deal you two cards at random at the start of the game. The objective of the game is to get the sum of your cards as close to 21 as possible without going over. Once you have both of your cards, you have the option to either "hit" or you can "stand". When you hit, you get another card at random, so if you have a high sum with the first two cards, it could be risky to hit as you could go over 21. When you stand, you pass up your turn without receiving another card. If you receive an ACE, you can choose to either count it as one point or eleven (11) points, depending on how many points you have already. So, if your two first cards add up to 12 and you hit and get an ACE, you should choose to have the ACE count as one point because if it was eleven (11) points, you would be over 21, losing the game. After you go, the dealer then reveals their cards, and if their two cards are 17 or more, he/she has to stand. If the dealer has less than 17, he/she picks cards until the sum is over 17. The person to get closest to 21 without going over wins.')

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
player_win = False
dealer_win = False
player_blackjack = False
dealer_blackjack = False
player_bust = False
dealer_bust = False

user_input = ''

def add_new_card():
    global your_cards_sum
    your_cards.append(random.choice(card_list))
    card_list.remove(your_cards[-1])
    if your_cards[-1] != 'A':
        your_cards_sum += your_cards[-1]

def handle_player_ace():
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

def add_dealer_card():
    global dealer_cards_sum
    dealer_cards.append(random.choice(card_list))
    card_list.remove(dealer_cards[-1])
    if dealer_cards[-1] != 'A':
        dealer_cards_sum += dealer_cards[-1]

def player_blackjack_check():
    if your_cards_sum == 21:
        game_over = True
        player_blackjack = True
        return True

add_new_card()
add_dealer_card()
add_new_card()
add_dealer_card()

print(f"Your starting cards are {your_cards}, and the dealer's first card is {dealer_cards[0]}")

if ((dealer_cards[0] == 10 and dealer_cards[1] == 'A') or (dealer_cards[0] == 'A' and dealer_cards[1] == 10)) and ((your_cards[0] == 10 and your_cards[1] == 'A') or (your_cards[0] == 'A' and your_cards[1] == 10)):
    print("How lucky/unlucky, both you and the dealer got blackjacks! No one wins!")
    game_over = True
elif (dealer_cards[0] == 10 and dealer_cards[1] == 'A') or (dealer_cards[0] == 'A' and dealer_cards[1] == 10):
    dealer_blackjack = True
    game_over = True
elif (your_cards[0] == 10 and your_cards[1] == 'A') or (your_cards[0] == 'A' and your_cards[1] == 10):
    player_blackjack = True
    game_over = True

if not game_over:
    user_input = input("Press any key to continue, or press 'q' to quit: ")

if user_input == 'q':
    game_over = True

while user_input != 'q' and not game_over: # first main loop to control the player hitting or standing

    print(f'Your cards are {your_cards} with a sum of {your_cards_sum}')

    handle_player_ace()

    if player_blackjack_check():
        break
    
    hit_or_stand = input(f'You currently have {your_cards_sum} points, do you want to hit or stand? (hit/stand): ').lower()

    while hit_or_stand == 'hit':

        add_new_card()

        print(f"Your new cards are {your_cards} with a sum of {your_cards_sum}")

        handle_player_ace()

        if your_cards_sum > 21:
            game_over = True
            player_bust = True
            break
        if player_blackjack_check():
            game_over = True
            player_blackjack = True
            break

        hit_or_stand = input(f'You currently have {your_cards_sum} points, do you want to hit or stand? (hit/stand): ').lower()

    if hit_or_stand == 'stand':
        print(f"You chose to stand with {your_cards_sum} points.")
        break

if not game_over:

    if 'A' in dealer_cards:
        ace_spot = dealer_cards.index('A')
        if dealer_cards_sum <= 10:
            dealer_cards_sum += 11
            dealer_cards[ace_spot] = 11
        else:
            dealer_cards_sum += 1
            dealer_cards[ace_spot] = 1

    print(f"Dealer's cards are {dealer_cards} with a sum of {dealer_cards_sum}")

    if dealer_cards_sum < 17:
        while dealer_cards_sum < 17:
            add_dealer_card()
            if 'A' in dealer_cards:
                ace_spot = dealer_cards.index('A')
                if dealer_cards_sum <= 10:
                    dealer_cards_sum += 11
                    dealer_cards[ace_spot] = 11
                else:
                    dealer_cards_sum += 1
                    dealer_cards[ace_spot] = 1
            print(f"Dealer's cards are {dealer_cards} with a sum of {dealer_cards_sum}")

    if dealer_cards_sum >= 17 and dealer_cards_sum < 21:
        if dealer_cards_sum > your_cards_sum:
            dealer_win = True
        elif dealer_cards_sum < your_cards_sum:
            player_win = True
            
    if dealer_cards_sum == 21:
        dealer_blackjack = True

    if dealer_cards_sum > 21:
        dealer_bust = True

if player_blackjack:
    print("Blackjack! You win!")
elif dealer_blackjack:
    print("The dealer got a blackjack. You lose!")
elif player_win:
    print(f"You beat the dealer by {your_cards_sum - dealer_cards_sum} points!")
elif dealer_win:
    print(f"You lost to the dealer by {dealer_cards_sum - your_cards_sum} points!")
elif dealer_bust:
    print("You win, the dealer busted!")
elif player_bust:
    print("You busted, the dealer wins!")
elif dealer_cards_sum == your_cards_sum:
    print("You and the dealer tied! No one wins, but no one loses!")

print('Thanks for playing!')
