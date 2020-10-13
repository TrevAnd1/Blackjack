import random

print('Welcome to Blackjack!')
know_to_play = input('Do you know how to play blackjack? (yes/no)').lower()

if know_to_play == 'yes':
  print("Awesome, then let's get started!")
elif know_to_play == 'no':
  print('I will deal you two cards at random at the start of the game. The objective of the game is to get the sum of your cards as close to 21 as possible without going over. Once you have both of your cards, you have the option to either "hit" or you can stand. When you hit, you get another card at random, so if you have a high sum with the first two cards, it could be risky to hit as you could go over 21. When you stand, you pass up your turn without receiving another card. If you receive an ACE, you can choose to either count it as one point or eleven (11) points, depending on how many points you have already. So, if your two first cards add up to 12 and you hit and get an ACE, you should choose to have the ACE count as one point because if it was eleven (11) points, you would be over 21, losing the game. After you go, the dealer then reveals his card, and if his two cards are 17 or more, he/she has to stand. If the dealer has less than 17, he/she picks cards until the sum is over 17. The one to get closest to 21 without going over wins.')

a = 0
card_list = [a, a, a, a, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
your_cards = []
dealer_cards = []
your_cards_sum = 0
dealer_cards_sum = 0
playing = True

while playing:

    for card in your_cards:
        your_cards_sum += your_cards[card]

    for card in dealer_cards:
        dealer_cards_sum += dealer_cards[card]

    def add_new_card():
        your_cards.append(random.choice(card_list))
        card_list.remove(your_cards[-1])
        return (f'Your cards are {your_cards} with a sum of {your_cards_sum}!')

    def check_for_ace():
        pass
print('Thanks for playing!')