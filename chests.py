# BETA version 1.2.1 09/22/2025

# Импорты

import random
import time
import collections

# Режим разработчика (0 - выкл, 1 - вкл, 2 - на функции, 3 - на карты, 4 - на ходы свина)

DebugMode = '0'

# Карты

cards = [
    '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
    '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
    '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',
    '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠'
]

cards_names = {
    '2': 'двойки',
    '3': 'тройки',
    '4': 'четверки',
    '5': 'пятерки',
    '6': 'шестерки',
    '7': 'семерки',
    '8': 'восьмерки',
    '9': 'девятки',
    '10': 'десятки',
    'J': 'валеты',
    'Q': 'дамы',
    'K': 'короли',
    'A': 'тузы'
}

cards_in_game, cards_not_in_game = [], []  # Колода в игре

chests_fox, chests_pig = 0, 0  # Кол-во наборов у игрока, свина

pig_cards, fox_cards = [], []  # Карты с мастью

true_fox_cards, true_pig_cards = [], []  # Карты без масти

current_turn_cards = []  # Ходы свина

# Реплики

pig_quotes_nocards = [
    'Карту, мистер Лис',
    'Нет, сэр, берите карту',
    'Берите карту, сэр',
    'Нет, сэр',
    'Берите карту'
]

fox_quotes_nocards = [
    'Берите карту, мистер Свин',
    'Неплохой ход, но вам придётся взять карту',
    'Берите карту',
    'А вы говорили, что хорошо играете в карты, берите карту',
    'Нет,берите карту'
]

pig_quotes_chest = ['Я собрал всю четверку']

fox_quotes_chest = ['Вот и собран набор карт']

fox_quotes_yescards = ['Мне нравится эта игра', 'Мне всегда везет в карточных играх']

pig_quotes_yescards = ['Мне это определенно подходит', 'Я неплохо играю в карточные игры']

# Прочие переменные

game_Flag = True  # Игра

game_Turn = 'Player'  # Ход

memory_choice_fox, memory_choice_pig = [], []  # Память о ходах игрока, неудачных ходах свина

delay = 1.75  # Задержка
if '0' not in DebugMode:
    delay = 0.5


# Функции

def refresh_cards():  # Обновление карт
    global cards_in_game, cards, fox_cards, pig_cards, true_pig_cards, true_fox_cards, cards_not_in_game
    if '1' in DebugMode or '2' in DebugMode:
        print('\n[DEBUG] Обновление карт')

    cards_in_game.clear()

    pig_cards.clear()
    fox_cards.clear()

    true_fox_cards.clear()
    true_pig_cards.clear()

    cards_in_game = cards.copy()
    for i in range(10):
        random.shuffle(cards_in_game)

    cards_not_in_game.clear()


def final_check():  # Проверка на лишние карты
    global fox_cards, pig_cards, true_pig_cards, true_fox_cards
    if '1' in DebugMode or '2' in DebugMode:
        print('\n[DEBUG] Проверка на лишние карты')
    for i in fox_cards:
        if i[:-1] in cards_not_in_game:
            fox_cards.remove(i)

    for e in pig_cards:
        if e[:-1] in cards_not_in_game:
            pig_cards.remove(e)

    for h in true_pig_cards:
        if h in cards_not_in_game:
            true_pig_cards.remove(h)

    for g in true_fox_cards:
        if g in cards_not_in_game:
            true_fox_cards.remove(g)


def check_for_chests():  # Проверка на наборы карт
    global fox_cards, pig_cards, true_fox_cards, true_pig_cards, chests_fox, chests_pig, cards_names, cards_not_in_game
    if '1' in DebugMode or '2' in DebugMode:
        print('\n[DEBUG] Проверка на наборы')

    a = [item for item, count in collections.Counter(true_fox_cards).items() if count > 3]
    if len(a) > 0:
        cards_not_in_game.append(a[0])
        for i in fox_cards:
            if i[:-1] == a[0]:
                fox_cards.remove(i)
        for g in true_fox_cards:
            if g == a[0]:
                true_fox_cards.remove(g)
        chests_fox += 1
        print(f'\n[FOX] - {random.choice(fox_quotes_chest)}')
        print(f'[INFO] Вы собрали набор карт из: {cards_names.get(a[0])}. Ваших наборов: {chests_fox}')
        final_check()
        a.clear()

    b = [item for item, count in collections.Counter(true_pig_cards).items() if count > 3]
    if len(b) > 0:
        cards_not_in_game.append(b[0])
        for e in pig_cards:
            if e[:-1] == b[0]:
                pig_cards.remove(e)
        for h in true_pig_cards:
            if h == b[0]:
                true_pig_cards.remove(h)
        chests_pig += 1
        print(f'\n[PIG] - {random.choice(pig_quotes_chest)}')
        if '1' in DebugMode or '3' in DebugMode:
            print(f'[DEBUG] Свин собрал набор карт из {cards_names.get(b[0])}. Наборов свина: {chests_pig}')
        else:
            print(f'[INFO] Свин собрал набор карт. Наборов свина: {chests_pig}')
        final_check()
        b.clear()


def start_game():  # Начать игру
    global fox_cards, pig_cards, cards_in_game, true_fox_cards, true_pig_cards, chests_pig, chests_fox, game_Flag, game_Turn, memory_choice_pig, memory_choice_fox

    if '1' in DebugMode or '2' in DebugMode:
        print('\n[DEBUG] Запуск игры')

    refresh_cards()

    chests_fox = 0
    chests_pig = 0

    for x in range(7):
        f = random.choice(cards_in_game)
        fox_cards.append(f)
        cards_in_game.remove(f)
        p = random.choice(cards_in_game)
        pig_cards.append(p)
        cards_in_game.remove(p)

    for y in fox_cards:
        true_fox_cards.append(y[:-1])

    for z in pig_cards:
        true_pig_cards.append(z[:-1])

    check_for_chests()

    memory_choice_pig.clear()
    memory_choice_fox.clear()

    game_Turn = 'Player'

    game_Flag = True

    player_turn()


def player_turn():  # Ход игрока
    global fox_cards, chests_fox, true_fox_cards, true_pig_cards, pig_cards, game_Turn, cards_in_game, memory_choice_fox, memory_choice_pig, chests_pig, game_Flag

    if '1' in DebugMode or '2' in DebugMode:
        print('\n[DEBUG] Ход игрока')

    final_check()

    if len(true_fox_cards) == 0 or len(true_pig_cards) == 0:
        if chests_pig > chests_fox:
            print(f'\n[PIG] - Я надеюсь поражение вас не расстроит. Свин: {chests_pig} - Лис: {chests_fox}')
        elif chests_pig == chests_fox:
            print(f'[FOX] - Ничья! Хорошая получилась игра. Лис: {chests_fox} - Свин: {chests_pig}')
            print(f'[PIG] - Да, хорошо сыграно.')
        else:
            print(f'[FOX] - Я победил. Лис: {chests_fox} - Свин: {chests_pig}')
        game_Flag = False
        game_Turn = 'None'
        try:
            ask = input('\nЖелаете начать новую игру (+/-) : ')
        except KeyboardInterrupt:
            exit()
        if ask == '+':
            start_game()
        else:
            exit()

    print('\n[INFO] Ваши карты: ' + ' ; '.join(sorted(fox_cards)))
    print(f'[INFO] Ваши наборы карт: {chests_fox}, наборы карт свина: {chests_pig}')

    if '1' in DebugMode or '3' in DebugMode:
        print('[DEBUG] Карты свина: ' + ' ; '.join(sorted(pig_cards)))
        print(f'[DEBUG] Truecards fox {sorted(true_fox_cards)}')
        print(f'[DEBUG] Truecards pig {sorted(true_pig_cards)}')
    try:
        choice = input('[INPUT] Выберите, какую карту вы хотите взять у соперника : ')
    except KeyboardInterrupt:
        exit()
    choice = choice.upper()

    while choice not in true_fox_cards:
        print('\n[ERROR] Вы должны обладать картой указанного номинала!\n')
        try:
            choice = input('[INPUT] Выберите, какую карту вы хотите взять у соперника : ')
        except KeyboardInterrupt:
            exit()
        choice = choice.upper()
    print(f'\n[FOX] - У вас есть {cards_names.get(choice)}?')
    time.sleep(delay)

    if choice in true_pig_cards:  # Если выбранная карта есть у свина
        print('[FOX] - ' + random.choice(fox_quotes_yescards))
        while choice in true_pig_cards:
            for i in pig_cards:
                if i[:-1] == choice:
                    pig_cards.remove(i)
                    fox_cards.append(i)
                    print(f'[INFO] Вы получили {i}')
            true_pig_cards.remove(choice)
            true_fox_cards.append(choice)

        check_for_chests()

    else:
        print('[PIG] - ' + random.choice(pig_quotes_nocards))
        newcard = random.choice(cards_in_game)
        if len(cards_in_game) > 0:
            fox_cards.append(newcard)
            true_fox_cards.append(newcard[:-1])
            cards_in_game.remove(newcard)
            print(f'[INFO] Вы получили {newcard}')
            print(f'[INFO] Карт в колоде: {len(cards_in_game)}')
        check_for_chests()
        time.sleep(delay)
        game_Turn = 'Pig'

    if choice not in memory_choice_fox:
        memory_choice_fox.append(choice)
    if choice in memory_choice_pig:
        memory_choice_pig.remove(choice)


def pig_turn():  # Ход свина
    global fox_cards, chests_fox, true_fox_cards, true_pig_cards, pig_cards, game_Turn, cards_in_game, memory_choice_fox, memory_choice_pig, chests_pig, game_Flag, current_turn_cards

    if '1' in DebugMode or '2' in DebugMode:
        print('\n[DEBUG] Ход свина')

    if '1' in DebugMode or '4' in DebugMode:
        print(f'\n[DEBUG] MemoryChoicePig : {memory_choice_pig}')
        print(f'[DEBUG] MemoryChoiceFox : {memory_choice_fox}')

    final_check()

    if len(true_pig_cards) == 0 or len(true_fox_cards) == 0:
        if chests_pig > chests_fox:
            print(f'\n[PIG] - Я надеюсь поражение вас не расстроит. Свин: {chests_pig} - Лис: {chests_fox}')
        elif chests_pig == chests_fox:
            print(f'[PIG] - Полагаю, у нас ничья. Свин: {chests_pig} - Лис: {chests_fox}')
            print(f'[FOX] - Да, хорошая была игра.')
        else:
            print(f'[FOX] - Я победил. Лис: {chests_fox} - Свин: {chests_pig}')
        game_Flag = False
        game_Turn = 'None'
        try:
            ask = input('\nЖелаете начать новую игру (+/-) : ')
        except KeyboardInterrupt:
            exit()
        if ask == '+':
            start_game()
        else:
            exit()

    prob = random.randint(0, 10)
    pig_choice = random.choice(true_pig_cards)
    old_choice = pig_choice
    tries = 0
    karta_list = []
    telepath_list = []

    while len(set(true_pig_cards)) > 1 and prob < 9 and pig_choice in memory_choice_pig:  # Проверка хода (self 1, 2)
        tries += 1
        pig_choice = random.choice(true_pig_cards)
        if pig_choice == old_choice or pig_choice in memory_choice_pig:
            if tries >= 10:
                if '1' in DebugMode or '4' in DebugMode:
                    print(
                        f'\n[DEBUG] PigChoice : self -> 1 (unable to change after {tries} tries) - old_choice({old_choice}) ; pig_choice({pig_choice})')
                if old_choice in memory_choice_pig:
                    memory_choice_pig.remove(old_choice)
                break
        else:
            if '1' in DebugMode or '4' in DebugMode:
                print(
                    f'\n[DEBUG] PigChoice : self -> 2 (changed after {tries} tries) - old_choice({old_choice}) ; pig_choice({pig_choice})')
            if old_choice in memory_choice_pig:
                memory_choice_pig.remove(old_choice)
            break

    if pig_choice in current_turn_cards:  # Проверка хода (current_turn 3)
        for karta_choice in true_pig_cards:
            if karta_choice not in current_turn_cards:
                karta_list.append(karta_choice)
        if len(karta_list) > 1:
            pig_choice = random.choice(karta_list)
        if '1' in DebugMode or '4' in DebugMode:
            print(
                f'\n[DEBUG] PigChoice : current_turn -> 3 (changed) - old_choice({old_choice}) ; pig_choice({pig_choice})')

    for i in true_pig_cards:  # Проверка хода (player 4)
        if i in memory_choice_fox:
            pig_choice = i
            memory_choice_fox.remove(pig_choice)
            if '1' in DebugMode or '4' in DebugMode:
                print(
                    f'\n[DEBUG] PigChoice : player -> 4 (changed) - old_choice({old_choice}) ; pig_choice({pig_choice})')
            break

    if prob >= 9:  # Проверка хода (telepath 5)
        for u in true_fox_cards:
            for e in true_pig_cards:
                if u == e and u not in telepath_list:
                    telepath_list.append(u)
        if len(telepath_list) > 0:
            pig_choice = random.choice(telepath_list)
            telepath_list.clear()
        if '1' in DebugMode or '4' in DebugMode:
            print(
                f'\n[DEBUG] PigChoice : telepath -> 5 (changed) - old_choice({old_choice}) ; pig_choice({pig_choice})')

    print(f'\n[PIG] - У вас есть {cards_names.get(pig_choice)}?')
    time.sleep(delay)

    if pig_choice in true_fox_cards:  # Если выбранная карта есть у игрока
        current_turn_cards.append(pig_choice)
        print('[PIG] - ' + random.choice(pig_quotes_yescards))
        if pig_choice not in memory_choice_pig:
            memory_choice_pig.append(pig_choice)
        while pig_choice in true_fox_cards:
            for i in fox_cards:
                if i[:-1] == pig_choice:
                    fox_cards.remove(i)
                    pig_cards.append(i)
                    print(f'[INFO] Вы потеряли {i}')
            true_fox_cards.remove(pig_choice)
            true_pig_cards.append(pig_choice)
        check_for_chests()
    else:
        print('[FOX] - ' + random.choice(fox_quotes_nocards))
        if pig_choice not in memory_choice_pig:
            memory_choice_pig.append(pig_choice)
        if len(cards_in_game) > 0:
            newcard = random.choice(cards_in_game)
            pig_cards.append(newcard)
            true_pig_cards.append(newcard[:-1])
            cards_in_game.remove(newcard)
            if '1' in DebugMode or '3' in DebugMode:
                print(f'[DEBUG] Свин получил {newcard}')
            print(f'[INFO] Карт в колоде: {len(cards_in_game)}')
        check_for_chests()
        time.sleep(delay)
        current_turn_cards.clear()
        game_Turn = 'Player'


start_game()

while game_Flag:  # Игровой процесс
    time.sleep(0.25)
    if game_Turn == 'Player':
        player_turn()
    elif game_Turn == 'Pig':
        pig_turn()
    else:
        break

# by Deltysh