import random

typ = "text"

intro ='''\nWelcome to War-Card game. In this game you opponent is computer. Basically this is a card game.The card with greater value takes opponent flash up card, if both cards are equal then the actual war begins.During war, the program automatically takes first 3 cards from computer and player, after that nxt flash up card decide who is bigger, if the nxt flash up card also equal, the war continues.
             who got all 52 cards won the game.'''
ins ='''\nTo play the game
        Type \'p\' to play game.
        Type \'s\' to shuffler player card.
        Type \'q\' to exit game.'''
print(intro)
print(ins)
computer = []
player = []
war_mem = []
cards = [2,3,4,5,6,7,8,9,10]
alp = 'J,Q,K,A'.split(",")
cards.extend(alp)


def val(i):
    if  i == "J":
        return 11
    elif i == "Q":
        return 12
    elif i == "K":
        return 13
    elif i == "A":
        return 14
    else:
        return i

class Deck:
    def __init__(self,c):
        self.c = c

    def extend_deck(self):
        for i in range(2):
            self.c.extend(self.c)

    def shuffle_deck(self):
        random.shuffle(self.c)

    def divide_cards(self):
        for i in range(0,52,2):
            computer.append(self.c[i])
        for i in range(1,52,2):
            player.append(self.c[i])

class Play:
    def __init__(self, computer, player):
        self.computer = computer
        self.player = player
    
    def com(self):
        com_temp = self.computer.pop(0)
        return val(com_temp)
        

    def opp(self):
        opp_temp = self.player.pop(0)
        return val(opp_temp)


def check(a,b):

    if a>b:
        computer.append(a)
        computer.append(b)
        if war_mem != []:
            computer.extend(war_mem)
            war_mem.clear()
        print("computer is big")
        return False

    elif a<b:
        player.append(b)
        player.append(a)
        if war_mem != []:
            player.extend(war_mem)
            war_mem.clear()
        print("Player is big")
        return False
    elif a == b:
        if len(computer)>=6 and len(player)>=6:
            print("both are equal")
            print("\n The war begins.. each player 3 cards must be flash down automatically.. ")
            war_mem.append(a)
            war_mem.append(b)
            for i in range(3):
                war_mem.append(computer.pop(i))
                war_mem.append(player.pop(i))
    
            print("war mem ",war_mem)
            return True
        else:
            c = len(computer)
            p = len(player)
            print("both are equal")
            if c<6:
                print("\nPlayer won the game....")
                return 5
            elif p<6:
                print("\ncomputer won the game....")
                return 5


mycard=Deck(cards)
mycard.extend_deck()
mycard.shuffle_deck()
mycard.divide_cards()


while 1 :
    data = input("")
    game = Play(computer,player)

    if data == "p":
        print("computer is ", computer[0])
        print("player is ", player[0])

        store = check(game.com(),game.opp())
        if store != True:
            print("remaining cards of computer",len(computer))
            print("remaining cards of player",len(player))
    elif data == "q":
        break
    elif computer == []:
        print("\nPlayer won the game....")
        break
    elif player == []:
        print("\n computer won the game...")
        break
    elif data == "s":
        random.shuffle(player)
    elif store == 5:
        break
    else:
        print("\n Please enter flash to play game or quit to exit game...")