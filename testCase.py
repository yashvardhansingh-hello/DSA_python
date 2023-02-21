from jovian.pythondsa import evaluate_test_case
import math, numpy

# def locate_card(cards, query):
#     mid = math.floor(len(cards)/2)
#     npy_cards = numpy.array(cards)
#     if query == cards[mid]:
#         return mid
#     elif len(cards) <= 1: 
#         return -1
#     elif query < cards[mid]:
#         return locate_card(npy_cards[mid+1, len[cards]], query)
#     elif query > cards[mid]:
#         return locate_card(npy_cards[0,mid-1], query)

def locate_card(cards, query):
    position = 0
    while True:
        if(query == cards[position]):
            return position
        if(not len(cards)):
            return -1
        position += 1


test = {
    "input": {
        "cards" : [11, 10, 9, 8, 6, 5, 5, 3, 2, 0],
        "query" : 3
    },
    "output" : 7
}
evaluate_test_case(locate_card, test)