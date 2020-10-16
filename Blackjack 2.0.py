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

    for i in your_cards:
        your_cards_sum += your_cards[i]

    for j in dealer_cards:
        dealer_cards_sum += dealer_cards[j]

    def add_new_card():
        your_cards.append(random.choice(card_list))
        card_list.remove(your_cards[-1])
        return (f'Your cards are {your_cards} with a sum of {your_cards_sum}!')

    def check_for_ace():
        for i in range(your_cards):
          if i == a:
            print(f'Your cards are {your_cards}')
            one_or_eleven = input('You have an ace! Do you want it to count as a 1 or 11? (one/eleven) ').lower()
            if one_or_eleven == 'one':
              your_cards[i] = 1
            else:
              your_cards[i] = 11
            return (f'Your new cards are {your_cards} with a sum of {your_cards_sum}')
          return (f'Your cards are {your_cards} with a sum of {your_cards_sum}')

    def add_dealer_card():
      dealer_cards.append(random.choice(card_list))
      card_list.remove(dealer_cards[-1])
      return (f'The dealer\'cards are {dealer_cards}')

    def check_for_ace_dealer():
      for i in range(dealer_cards):
        if (dealer_cards[i] == a):
          if dealer_cards.index(i) == 0:
            if dealer_cards[i + 1] >= 6:
              dealer_cards[i] = 11
            else:
              dealer_cards[i] = 1
          elif dealer_cards.index(i) == 1:
            if dealer_cards[i - 1] >= 6:
              dealer_cards[i] = 11
            else:
              dealer_cards[i] = 1
      return (f'The dealer\'s cards are {dealer_cards} with a sum of {dealer_cards_sum}')


    def check_if_bust():
      hit_or_stand= True
      if your_cards_sum > 21:
        print('You busted!')

    add_new_card()

    check_for_ace()

print('Thanks for playing!')
