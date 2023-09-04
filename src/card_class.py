'''cardscheme Card Object Class
    @author: John Lindon Robinson (john@johnlindon.com)
    @version: 0.0.1

    https://github.com/JohnLindonRobinson/cardscheme

    This class is used to represent a card in the cardscheme database

    @dependencies:
    Python 3.6+
    requests
'''
import requests


class UnprocessedCard:
    '''A class to represent an unprocessed card
    '''


    def __init__(self, set, collectors_no, condition, isfoil, language):
        self.set = set
        self.collectors_no = collectors_no
        self.condition = condition
        self.isfoil = isfoil
        self.language = language

    def verify_card_exists(self):
        '''Verifies that the card exists in the Scryfall database
        @return: True if the card exists, False otherwise
        '''
        api_url = "https://api.scryfall.com/cards/" + self.set + "/" + self.collectors_no
        response = requests.get(api_url)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def get_card_name(self):
        '''Gets the name of the card
        @return: The name of the card
        '''
        api_url = "https://api.scryfall.com/cards/" + self.set + "/" + self.collectors_no
        response = requests.get(api_url)
        return response.json()['name']