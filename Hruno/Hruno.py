import random


# the dictionary with all cards in the game

class GameState():
    cards = {'1gr': ['1', 'green', 'general'], '2gr': ['2', 'green', 'general'], '3gr': ['3', 'green', 'general'],
             '4gr': ['4', 'green', 'general'], \
             '5gr': ['5', 'green', 'general'], '6gr': ['6', 'green', 'general'], '7gr': ['7', 'green', 'general'], \
             '1pk': ['1', 'pink', 'general'], '2pk': ['2', 'pink', 'general'], '3pk': ['3', 'pink', 'general'],
             '4pk': ['4', 'pink', 'general'], \
             '5pk': ['5', 'pink', 'general'], '6pk': ['6', 'pink', 'general'], '7pk': ['7', 'pink', 'general'], \
             '1yl': ['1', 'yellow', 'general'], '2yl': ['2', 'yellow', 'general'], '3yl': ['3', 'yellow', 'general'],
             '4yl': ['4', 'yellow', 'general'], \
             '5yl': ['5', 'yellow', 'general'], '6yl': ['6', 'yellow', 'general'], '7yl': ['7', 'yellow', 'general'], \
             '1bl': ['1', 'blue', 'general'], '2bl': ['2', 'blue', 'general'], '3bl': ['3', 'blue', 'general'],
             '4bl': ['4', 'blue', 'general'], \
             '5bl': ['5', 'blue', 'general'], '6bl': ['6', 'blue', 'general'], '7bl': ['7', 'blue', 'general'], \
             'modulation1': ['modulation', 'neutral', 'changecolor'],
             'modulation2': ['modulation', 'neutral', 'changecolor'], \
             'modulation3': ['modulation', 'neutral', 'changecolor'],
             'modulation4': ['modulation', 'neutral', 'changecolor'], \
             'drumsolo1': ['drumsolo', 'neutral', 'changedigit'], 'drumsolo2': ['drumsolo', 'neutral', 'changedigit'], \
             'drumsolo3': ['drumsolo', 'neutral', 'changedigit'], 'drumsolo4': ['drumsolo', 'neutral', 'changedigit'], \
             'contrabassgr': ['contrabass', 'green', 'revdirect'], 'contrabasspk': ['contrabass', 'pink', 'revdirect'], \
             'contrabassyl': ['contrabass', 'yellow', 'revdirect'], 'contrabassbl': ['contrabass', 'blue', 'revdirect'], \
             'saxophonegr': ['saxophone', 'green', 'skip'], 'saxophonepk': ['saxophone', 'pink', 'skip'], \
             'saxophoneyl': ['saxophone', 'yellow', 'skip'], 'saxophonebl': ['saxophone', 'blue', 'skip'],
             'kakophonia': ['kakophonia', 'neutral', 'spoil']}

    def __init__(self, players):
        # self.choice = choice
        self.players = players

    def nextPlayer(self):
        pass

    def getCurrentPlayer(self):
        currentPlayer = self.players[0]
        return currentPlayer

    def getGameOrder(self):
        '''gets the order in which the game is played'''
        return self.players

    def modulation(self):
        '''what happens when the Modulation card is played:
        the color is changed to the one called by the player 
        who plays this card
        the next player can play only the card with this color'''
        pass

    def drumSolo(self):
        '''what happens when the Drum Solo card is played:
        this card can be played on any other card,
        the player who plays this card names a digit (1-7) and all other players can only play a card with this digit
        the last one in the round is the initial player who has to play the card with the digit
        then the game goes in a normal way'''
        pass

    def contraBass(self):
        '''what happens when the Contarbass-Barabass card is played:
        the next player takes 2 cards and skips his turn'''

    def saxoPhoneWater(self):
        '''what happens when the Saxophone-Water-in-it card is played:
        the game flow is reverted, the player who played before the card takes one card and skips his turn'''
        pass


class PlayedCards(object):
    def __init__(self, playedCardStack):
        self.playedCardStack = playedCardStack

    def addCards(self, card):
        self.playedCardStack.append(card)

    def getPlayedCardStack(self):
        return self.playedCardStack

    def getTopCard(self):
        self.topCard = self.playedCardStack[-1]
        return self.topCard

    def refillNonPlayedCards(self):
        self.topCard = self.playedCardStack.pop()
        return self.playedCardStack

class NonPlayedCards(object):
    def __init__(self, nonPlayedCardsStack):
        self.nonPlayedCardsStack = nonPlayedCardsStack

    def addCards(self, cards):
        self.nonPlayedCardsStack.append(cards)

    def takeCard(self):
        takenCard = self.nonPlayedCardsStack.pop()
        return takenCard

    def getNonPlayedCardsStack(self):
        return self.nonPlayedCardsStack


class Player(object):
    def __init__(self, name, personalCardStack):
        self.name = name
        self.personalCardStack = personalCardStack

    def getName(self):
        return self.name

    def addCards(self, card):
        # self.card = card
        self.personalCardStack.append(card)

    def playCard(self, card):
        self.personalCardStack.remove(card)

    def getPersonalCardStack(self):
        return self.personalCardStack


class ArtificialPlayer(Player):
    def __init__(self, name, personalCardStack):
        Player.__init__(self, name, personalCardStack)

    def getPlayerType(self):
        return 'artificial'


class HumanPlayer(Player):
    def __init__(self, name, personalCardStack):
        Player.__init__(self, name, personalCardStack)

    def getPlayerType(self):
        return 'human'


print '\n\nhello, we are going to play Hruno card game\n\n'
print 'first of all, we take the box with cards'
print 'then we shuffle the cards'

# cardsInBox - total amount of cards in a card box
# initial list of all cards. not shuffled, always in the same order

cardsInBox = GameState.cards.keys()

# let's shuffle the cards
random.shuffle(cardsInBox)

# generate players based on the initial conditions: 3 artificial players + 1 human
numberOfPlayers = 4

players = []

print '\n\nwe are going to play with 3 computer players and one human player\n'

for i in range(1, numberOfPlayers):
    playerName = 'player' + str(i)
    print '\tname of the player is: ', playerName
    player = ArtificialPlayer(playerName, [])
    players.append(player)

humanPlayerName = raw_input('\n\nOK, we have 3 computer players, \nnow it is time to invite a human player to the game\
    \n\nplease enter your name: ')

humanPlayer = HumanPlayer(humanPlayerName, [])

print '\nso your name is %s, \nnice to meet you!' % humanPlayer.getName()

players.append(humanPlayer)

print 'players', players


def generateGameOrder(choice, players):
    first = players.index(choice)
    beginning = players[first:]
    end = players[:first]
    players = beginning + end
    return players


def gamePlay(players, cardsInBox):
    print '\nLet`s decide who is going to be the first to play and in which direction\
    will the game go'

    choice = random.choice(players)

    players = generateGameOrder(choice, players)
    gameFlow = GameState(players)

    print '\nnow we are going to distribute 5 cards to each player\n'

    for i in range(5):
        for player in players:
            player.addCards(cardsInBox.pop())

    openCard = cardsInBox.pop()
    pc = PlayedCards([])
    pc.addCards(openCard)
    print '\ncards are distributed among the players, so each player gets 5 cards'
    print 'all the rest of the cards are in a stack that is upside-down'
    print 'except for one card we start with: ', pc.getTopCard()

    npc = NonPlayedCards(cardsInBox)

    print '\nthe cards of the human player are:', players[-1].getPersonalCardStack()

    print 'the current player is: ', gameFlow.getCurrentPlayer().getName()

    while True:
        current = gameFlow.getCurrentPlayer()
        if current.getPlayerType() == 'human':
            print '\n\nIt is your turn now. Please choose, which card to play'
            for card in current.getPersonalCardStack():
                print '\n\t [', current.getPersonalCardStack().index(card) + 1, ']', card
            chosen_card = GameState.cards[current.getPersonalCardStack[
                raw_input('Enter the # of the card you want to play [1-', len(current.getPersonalCardStack() + 1),
                          ']') - 1]]

            while True:
                if chosen_card[0] != GameState.cards[pc.getTopCard][0] and \
                                chosen_card[1] != GameState.cards[pc.getTopCard][1]:
                    chosen_card = GameState.cards[current.getPersonalCardStack[
                        raw_input('Enter the # of the card you want to play [1-',
                                  len(current.getPersonalCardStack() + 1), ']') - 1]]
                else:
                    False


gamePlay(players, cardsInBox)

'''
every Player has: cards
28 reg + 16 spec +1 = 
every card has: weight (1-7,10), color(green, pink, yellow, blue), action()

special card has: weight(10), color(green, pink, yellow, blue), action(modulation(neutral), drumsolo(neutral), contrabass(4colors), saxophone(4colors), kakophonia(neutral))

gameplay: 

Beginning
1. new GeneralCardStack is generated (always the same 45 cards, new order)
2. all Players are given a PersonalCardStack (5 cards from GeneralCardStack * number of Players). 
GeneralCardStack = GeneralCardStack - (PersonalCardStack * n Players)
3. The first card in the GeneralCardStack is shown to players. A PlayCardStack is created.
4. The order in which the players play is generated (PlayersOrder).

GeneralGameplay
1. if ArtificialPlayer is the first in PlayersOrder.
         this ArtificialPlayer's Ability to play the card is calculated
2. if Ability is True
         The bestChoice is calculated
         Player plays a card based on the bestChoice and adds it to PlayCardStack
3. if Ability is False
         First card from the GeneralCardStack is moved to the Player's PersonalCardStack
         Players Ability to play is calculated 
         if Ability is True
             The bestChoice is calculated
             Player plays a card based on the bestChoice and adds it to PlayCardStack
         if Ability is False
             the move goes to the next Player 
4.   '''
