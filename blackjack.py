# BETA version 1.1 09/22/2025

import random
import time

cards = [
    '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
    '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
    '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',
    '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠'
]
random.shuffle(cards)

coloda = cards.copy()

score = 0
dscore = 0
carddlr1 = 0
carddlr2 = 0
cardplr1 = 0
cardplr2 = 0
cardplr = 0
carddlr = 0
dealerchoice = 0
balance = 0
bet = 0
start = True
game = False
podskazka = ''
games_a = 0
wins_a = 0
loses_a = 0


def display_plr_first_cards():
    global cardplr1, cardplr2, score
    print(f"\n[INFO] ВАШИ КАРТЫ: {cardplr1} & {cardplr2}")


def add_first_score_plr():
    global score, cardplr1, cardplr2, gamedealer, gameplayer, bet, balance, wins_a, games_a, loses_a
    if cardplr1[:-1] == 'K':
        score += 10
    elif cardplr1[:-1] == 'J':
        score += 10
    elif cardplr1[:-1] == 'Q':
        score += 10
    elif cardplr1[:-1] == 'A':
        if score + 11 > 21:
            score += 1
        else:
            score += 11
    else:
        score += int(cardplr1[:-1])

    if cardplr2[:-1] == 'K':
        score += 10
    elif cardplr2[:-1] == 'J':
        score += 10
    elif cardplr2[:-1] == 'Q':
        score += 10
    elif cardplr2[:-1] == 'A':
        if score + 11 > 21:
            score += 1
        else:
            score += 11
    else:
        score += int(cardplr2[:-1])

    if score == 21 and dscore < score:
        gamedealer = False
        gameplayer = False
        display_plr_first_cards()
        display_dlr_first_cards_2()
        print("\n[INFO] БЛЭКДЖЕК! Вы выиграли.")
        balance += int(bet * 2.5)
        wins_a += 1
        games_a += 1


def player_take_first_cards():
    global cardplr1, cardplr2
    cardplr1 = random.choice(coloda)
    coloda.remove(cardplr1)
    cardplr2 = random.choice(coloda)
    coloda.remove(cardplr2)
    display_plr_first_cards()


def player_take_card():
    global cardplr
    time.sleep(0.5)
    cardplr = random.choice(coloda)
    coloda.remove(cardplr)
    print(f"\n[INFO] Вам выпала карта: {cardplr}")
    add_score_plr()


def add_score_plr():
    global score, cardplr
    if cardplr[:-1] == 'K':
        score += 10
    elif cardplr[:-1] == 'J':
        score += 10
    elif cardplr[:-1] == 'Q':
        score += 10
    elif cardplr[:-1] == 'A':
        if score + 11 > 21:
            score += 1
        else:
            score += 11
    else:
        score += int(cardplr[:-1])


def display_dlr_first_cards():
    global carddlr1, carddlr2, dscore
    print(f"\n[INFO] КАРТЫ ДИЛЕРА: ## & {carddlr2}")


def display_dlr_first_cards_2():
    global carddlr1, carddlr2, dscore
    print(f"\n[INFO] КАРТЫ ДИЛЕРА: {carddlr1} & {carddlr2}")


def add_first_score_dlr():
    global dscore, carddlr1, carddlr2, gamedealer, gameplayer, bet, balance, wins_a, games_a, loses_a
    if carddlr1[:-1] == 'K':
        dscore += 10
    elif carddlr1[:-1] == 'J':
        dscore += 10
    elif carddlr1[:-1] == 'Q':
        dscore += 10
    elif carddlr1[:-1] == 'A':
        if dscore + 11 > 21:
            dscore += 1
        else:
            dscore += 11
    else:
        dscore += int(carddlr1[:-1])

    if carddlr2[:-1] == 'K':
        dscore += 10
    elif carddlr2[:-1] == 'J':
        dscore += 10
    elif carddlr2[:-1] == 'Q':
        dscore += 10
    elif carddlr2[:-1] == 'A':
        if dscore + 11 > 21:
            dscore += 1
        else:
            dscore += 11
    else:
        dscore += int(carddlr2[:-1])

    if dscore == 21 and dscore > score:
        display_plr_first_cards()
        displaydlrFirstCards_2()
        print("\n[INFO] У ДИЛЕРА БЛЭКДЖЕК! Вы проиграли.")
        loses_a += 1
        games_a += 1
        gamedealer = False
        gameplayer = False


def dealer_take_first_cards():
    global carddlr1, carddlr2
    carddlr1 = random.choice(coloda)
    coloda.remove(carddlr1)
    carddlr2 = random.choice(coloda)
    coloda.remove(carddlr2)
    display_dlr_first_cards()


def dealer_take_card():
    global carddlr
    time.sleep(0.5)
    carddlr = random.choice(coloda)
    coloda.remove(carddlr)
    print(f"\n[INFO] Дилеру выпала карта: {carddlr}")
    add_score_dlr()


def add_score_dlr():
    global dscore, carddlr
    if carddlr[:-1] == 'K':
        dscore += 10
    elif carddlr[:-1] == 'J':
        dscore += 10
    elif carddlr[:-1] == 'Q':
        dscore += 10
    elif carddlr[:-1] == 'A':
        if dscore + 11 > 21:
            dscore += 1
        else:
            dscore += 11
    else:
        dscore += int(carddlr[:-1])
    print(f"[INFO] СЧЕТ ДИЛЕРА: {dscore}\n")


def dealer_choice():
    global dealerchoice
    dealerchoice = random.randint(1, 6)
    if dealerchoice == 1:
        return True
    elif dealerchoice == 2:
        return False
    elif dealerchoice == 3:
        return True
    elif dealerchoice == 4:
        return True
    elif dealerchoice == 5:
        return True
    elif dealerchoice == 6:
        return False


def check_game():
    global score, dscore, gamedealer, gameplayer, balance, bet, wins_a, games_a, loses_a
    if dscore > 21 and gamedealer:
        gamedealer = False
        print("[INFO] У дилера перебор! Вы выиграли.")
        balance += bet * 2
        games_a += 1
        wins_a += 1
    elif score == 21 and dscore == 21 and gamedealer:
        gamedealer = False
        print("[INFO] Ничья!")
        games_a += 1
        balance += bet
    elif dscore > score and gamedealer:
        gamedealer = False
        print(f"[INFO] У дилера {dscore} очков! Вы проиграли.")
        games_a += 1
        loses_a += 1
    elif dscore < score and not gamedealer:
        gamedealer = False
        print(f"[INFO] У дилера {dscore} (у вас {score})! Вы выиграли.")
        balance += bet * 2
        games_a += 1
        wins_a += 1
    elif score == dscore and not gamedealer:
        gamedealer = False
        print("[INFO] Ничья!")
        games_a += 1
        balance += bet


def dealer_playing():
    global dscore, score, carddlr, carddlr1, carddlr2, gamedealer, gameplayer, balance, bet, wins_a, games_a, loses_a
    dealer_choice()
    time.sleep(0.5)
    if dscore > 21:
        gamedealer = False
        print("[INFO] У дилера перебор! Вы выиграли.")
        balance += bet * 2
        games_a += 1
        wins_a += 1
    if gamedealer:
        if dscore > score:
            gamedealer = False
            time.sleep(0.5)
            print(f"[INFO] У дилера {dscore} очков! Вы проиграли.")
            games_a += 1
            loses_a += 1
        elif dscore < 12:
            dealer_take_card()
            time.sleep(0.1)
        elif 12 <= dscore < 16:
            if dealer_choice():
                dealer_take_card()
            if not dealer_choice():
                check_game()
                time.sleep(0.1)
                gamedealer = False
        elif 16 <= dscore < 20:
            if dealer_choice():
                dealer_take_card()
            else:
                check_game()
                time.sleep(0.1)
                gamedealer = False
        elif dscore == 20:
            check_game()
            time.sleep(0.1)
            gamedealer = False
        else:
            check_game()
            time.sleep(0.1)
            gamedealer = False
    time.sleep(0.25)
    check_game()


def start_new_game():
    global balance, coloda, bet, gameplayer, gamedealer, score, dscore, carddlr, carddlr1, carddlr2, cardplr, cardplr1, cardplr2, dealerchoice, game
    bet = 0
    while balance >= 1 and not game:
        try:
            bet = int(input(f"[INPUT] Введите ставку (Баланс - {balance} фишек.): "))
        except ValueError:
            print('[ERROR] Ошибка ввода!')
        except KeyboardInterrupt:
            exit()
        else:
            if balance >= bet >= 1:
                game = True
        if game:
            if len(coloda) < 52:
                coloda.clear()
                coloda = cards.copy()
            balance -= bet
            gameplayer = True
            gamedealer = False
            score = 0
            dscore = 0
            carddlr1 = 0
            carddlr2 = 0
            cardplr1 = 0
            cardplr2 = 0
            cardplr = 0
            carddlr = 0
            dealerchoice = 0
            player_take_first_cards()
            dealer_take_first_cards()
            add_first_score_plr()
            add_first_score_dlr()


def start_game():
    global balance, start, podskazka
    while balance < 1 and start:
        try:
            balance = int(input(f"[INPUT] Введите количество ваших фишек{podskazka}: "))
        except ValueError:
            print('[ERROR] Ошибка ввода!')
        except KeyboardInterrupt:
            exit()
        if balance < 1:
            podskazka = ' (от 1)'
        else:
            start_new_game()
            start = False


start_game()

while game:
    random.shuffle(coloda)
    while gameplayer:
        print(f"\n[INFO] ВАШ СЧЕТ: {score}")
        if score > 21:
            print("[INFO] ПЕРЕБОР! Вы проиграли.")
            games_a += 1
            loses_a += 1
            gameplayer = False
            gamedealer = False
            break
        try:
            decision = input("[INPUT] Хотите взять ещё карту? (+/-) ")
        except KeyboardInterrupt:
            exit()
        if decision == '+':
            player_take_card()
        elif decision == '-':
            gamedealer = True
            gameplayer = False
            display_dlr_first_cards_2()
            if score > dscore and dscore < 20:
                dealer_take_card()
        else:
            try:
                decision = input("[INPUT] Хотите взять ещё карту? (+/-) ")
            except KeyboardInterrupt:
                exit()
        while gamedealer:
            dealer_playing()
    game = False
    print(
        f"\n[INFO] ИГР СЫГРАНО: {games_a}, ПОБЕД: {wins_a}, ПРОИГРЫШЕЙ: {loses_a}. ВИНРЕЙТ: {int(round(wins_a / games_a, 2) * 100)}%\n")
    if balance < 1:
        try:
            newgame = input("[INPUT] Вы все проиграли! Желаете начать сначала? (+/-) ")
        except KeyboardInterrupt:
            exit()
        if newgame == '+':
            balance = 0
            games_a = 0
            wins_a = 0
            loses_a = 0
            start = True
            start_game()
        else:
            break
    else:
        start_new_game()

# by Deltysh