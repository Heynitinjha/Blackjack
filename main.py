import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def Calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(User_score, Computer_score):
    # Bug fix. If you and the computer are both over, you lose.
    if User_score > 21 and Computer_score > 21:
        return "You went over. You lose 😤"

    if User_score == Computer_score:
        return "Draw 🙃"
    elif Computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif User_score == 0:
        return "Win with a Blackjack 😎"
    elif User_score > 21:
        return "You went over. You lose 😭"
    elif Computer_score > 21:
        return "Opponent went over. You win 😁"
    elif User_score > Computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def Game():
    User_card = []
    Computer_card = []
    game_over = False

    for _ in range(2):
        User_card.append(deal_card())
        Computer_card.append(deal_card())
    while not game_over:
        User_score = Calculate_score(User_card)
        Computer_score = Calculate_score(Computer_card)

        print(f"user card {User_card}, and Score is {User_score}")
        print(f"Computer card {Computer_card[0]}")

        if User_score == 0 or Computer_score == 0 or User_score > 21:
            game_over = True
        else:
            User_input = input("Enter Y to continue and N to exit")
            if User_input == "Y":
                User_card.append(deal_card())
            else:
                game_over = True
    while Computer_score != 0 and Computer_score < 21:
        Computer_card.append(deal_card())
        Computer_score = Calculate_score(Computer_card)

    print(f"   Your final hand: {User_card}, final score: {User_score}")
    print(f"   Computer's final hand: {Computer_card}, final score:")
    print(compare(User_score, Computer_score))


while input("want to play more ? Type Y to play and N to exti") == "Y":
    Game()