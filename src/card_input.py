''' cardscheme Card Input Class
    @author: Johnny Lindon Robinson (john@johnlindon.com)
    @version: 0.0.1

    https://github.com/JohnLindonRobinson/cardscheme

    This class is used to input cards into the cardscheme database in a fast manner
    It is designed to be used in a command line environment

    @dependencies:
    Python 3.6+
    requests
'''

__author__ = "Johnny Lindon Robinson (john@johnlindon.com)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2023-2023 Johnny Lindon Robinson"
__license__ = "GPLv3"

import os
import sys

import requests

from card_class import UnprocessedCard


def remove_leading_zeroes(no):
    '''Removes leading zeroes from a string
    @param no: The string to remove leading zeroes from
    
    @return: The string with leading zeroes removed
    '''
    while no[0] == '0':
        no = no[1:]
    return no

def is_foil(isfoil):
    '''Converts a string to a boolean
    @param isfoil: The string to convert
    
    @return: True if the string is '1', False otherwise
    '''
    if isfoil == 'f' or isfoil == 'F' or isfoil == '1':
        return True
    else:
        return False

def get_card_from_API(set, collectors_no, condition):
    '''Gets a card from Scryfall API returning useful information about the card
    @param set: The set code of the card
    @param collectors_no: The collectors number of the card
    @param condition: The condition of the card (Baseball Scale)
    
    @return: A dictionary containing the card information
    '''
    collectors_no = remove_leading_zeroes(collectors_no)
    api_url = "https://api.scryfall.com/cards/" + set + "/" + collectors_no
    print(api_url)

def get_card_input_cli():
    '''Gets a card from the command line interface
    @return: A dictionary containing the card information
    '''
    UID = input("Enter the card's UID: ")
    # Split the UID into set (3ch), condition (2ch), isfoil (1ch), collectors number (3ch), and language (2ch)
    set = UID[0:3]
    condition = UID[3:5]
    isfoil = is_foil(UID[5])
    collectors_no = UID[6:9]
    if len(UID) == 11:
        language = UID[9:11]
    else:
        language = "en"
    
    return UnprocessedCard(set, collectors_no, condition, isfoil, language)
    

card = get_card_input_cli()
if card.verify_card_exists():
    print(card.get_card_name())
else:
    print("Card does not exist")
