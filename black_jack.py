import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

count_games = 0
game_active = 'y'

player = []
dealer = []
player_sum = 0
dealer_sum = 0

def shuffle_cards():
    global player
    global dealer
    global player_sum
    global dealer_sum

    player = [cards[random.randint(0, len(cards) - 1)], cards[random.randint(0, len(cards) - 1)]]
    dealer = [cards[random.randint(0, len(cards) - 1)]]
    player_sum = 0
    dealer_sum = 0

def sum_numbers():
    global player_sum
    global dealer_sum

    player_sum = 0
    dealer_sum = 0

    for num in player:
        player_sum += num

    for num in dealer:
        dealer_sum += num

def display_numbers():
    global player_sum
    global dealer_sum

    print(f'Player: {player}  sum: {player_sum}')
    print(f'Dealer: {dealer}  sum: {dealer_sum}')

def check_21():
    global player_sum
    global dealer_sum
    global game_active

    if (player_sum > 21 or dealer_sum == 21) or (dealer_sum <= 21 and dealer_sum > player_sum):
        print('You lose!')
        game_active = 'n'
        return
    elif dealer_sum > 21 or player_sum == 21:
        print('You win!')
        game_active = 'n'
        return
    elif dealer_sum == player_sum:
        print('Draw')
        game_active = 'n'
        return
    else:
        return 'continue'

def black_jack_game():
    global player_sum
    global dealer_sum
    global game_active

    shuffle_cards()

    # player_sum = 0
    # dealer_sum = 0
    sum_numbers()
    display_numbers()

    while game_active == 'y':
        if player_sum == 21:
            print('You win!')
            break

        decision = input('Decision: type "h" for hit another card / type "s" for hit another stand: ')

        if decision == 'h':
            player.append(cards[random.randint(0,len(cards)-1)])
        elif decision == 's':
            while dealer_sum < 17:
                dealer.append(cards[random.randint(0,len(cards)-1)])
                sum_numbers()
        sum_numbers()
        display_numbers()

        if check_21() is None:
            break



while type(count_games) == int:
    if count_games == 0:
        print(art.logo)
        black_jack_game()
        count_games += 1
    else:
        if input('Another game? (y/n) ') == 'y':
            game_active = 'y'
            black_jack_game()
            count_games += 1
        else:
            print(f'You played {count_games} rounds! Thank you!')
            count_games = ''