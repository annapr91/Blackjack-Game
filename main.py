import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal():
    return random.choices(cards, k=2)


def calculate_score(seq):
    summa = sum(seq)
    if len(seq) == 2 and summa == 21:
        return 0
    if summa > 21 and 11 in seq:
        seq.remove(11)
        seq.append(1)
    return summa


def compare(computer_score, user_score):
    if computer_score == user_score:
        print('It is a draw')
    elif computer_score == 0:
        print('USER lost')
    elif user_score == 0:
        print('USER win')
    elif user_score > 21:
        print('USER lost')
    elif computer_score > 21:
        print('USER win.CoMPUTER lost')
    else:
        if computer_score > user_score:
            print('COMPUTER WON')
        else:
            print('USER WON')


def game():
    user_cards = deal()
    computer_cards = deal()
    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards {user_cards}, your score {user_score}')
        print(f'Computer cards {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            res = input("Do you want to take another card? Type 'y' or 'n':")
            if res == 'y':
                card = random.choice(cards)
                user_cards.append(card)
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        card = random.choice(cards)
        computer_cards.append(card)
        computer_score = calculate_score(computer_cards)

    print(f'YOur final hand {user_cards}, and score {user_score}')
    print(f'Computer {computer_cards}, and score {computer_score}')
    compare(computer_score, user_score)



while input("DO you want ot play Blackjack? Type 'y' or 'n'") == 'y':
    print(logo)
    game()