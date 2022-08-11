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
playercards = []
pccards = []
def score(cards):
    if sum(cards) == 21 and cards == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.insert(cards.index(11),1)
        cards.remove(11)
    return sum(cards)

def dealcard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    while pccards != 0 and sum(pccards) < 17:
        pccards.append(random.choice(cards))
    return playercards.append(random.choice(cards))

def compare(playercards, pccards):
    playercards = score(playercards)
    pccards = score(pccards)
    if playercards == pccards:
        return '\033[33mDRAW!!\033[m'
    elif playercards == 0 or playercards == 21:
        return '\033[32mBLACK JACK!! YOU WIN!!\033[m'
    elif pccards == 0 or pccards == 21:
        return '\033[31mCOMPUTER HAS A BLACK JACK!! YOU LOSE!!\033[m'
    elif playercards > 21:
        return '\033[31mMORE THAN 21, YOU LOSE!!\033[m'
    elif pccards > 21:
        return '\033[32mPC GETS MORE THAN 21 YOU WIN!!\033[m'
    elif playercards !=0 and playercards > pccards:
        return '\033[32mYOU WIN!!\033[m'
    elif pccards !=0 and pccards > playercards:
        return '\033[31mYOU LOSE!!\033[m'


def playgame():
    while True:
        x = input('Do you want to play a game of Blackjack? [y/n]')
        playercards.clear()
        pccards.clear()
        if x == 'n':
            break
        print(logo)
        for c in range(0,2):
            dealcard()
        print(f'    Your cards: {playercards}, score: {score(playercards)}')
        print(f'    Computer first card: {pccards[0]}')
        if score(playercards) >= 21 or score(pccards) >= 21:
            compare(playercards, pccards)
        while input('Type "y" to get another card, type "n" to pass') == 'y':
            dealcard()
            if score(playercards) >= 21 or score(pccards) >= 21:
                break
            print(f'    Your hand: {playercards}, score: {score(playercards)}')
            print(f'    Computer hand:{pccards}, score:{score(pccards)}')
        print(f'    Your final hand: {playercards}, score: {score(playercards)}')
        print(f'    Computer final hand:{pccards}, score:{score(pccards)}')
        print(compare(playercards,pccards))

playgame()