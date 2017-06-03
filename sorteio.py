#Vitor Daynno 30/04/2017
import random
from trello import TrelloApi
from Config import Config

chaves = Config()
quadroID = 'fLiSU3im' #Nome do quadro
trello = TrelloApi(chaves.get_Api_Key(),'none')  #API Key
trello.set_token(chaves.get_Token()) #Token
board = trello.boards.get(quadroID)
lista = trello.boards.get_list(board['id'])
cards = trello.lists.get_card(lista[0]['id'])
print cards[random.randint(0,len(cards))]['name']

