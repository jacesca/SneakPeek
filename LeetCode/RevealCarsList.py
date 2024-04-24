"""
Reveal Cards In Increasing Order
You are given an integer array deck.
There is a deck of cards where every card has a unique integer.
The integer on the ith card is deck[i].

You can order the deck in any order you want.
Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

1. Take the top card of the deck, reveal it, and take it out of the deck.
   The sequence is based on the index.
2. If there are still cards in the deck then put the next top card of the
   deck at the bottom of the deck.
3. If there are still unrevealed cards, go back to step 1. Otherwise, stop.

Return an ordering of the deck that would reveal the cards in increasing
order.
Note that the first entry in the answer is considered to be the top of the
deck.

Example 1:
Input: deck = [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]

Example 2:
Input: deck = [1,1000]
Output: [1,1000]

Constraints:
1 <= deck.length <= 1000
1 <= deck[i] <= 106
All the values of deck are unique.
"""


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck = sorted(deck)
        size = len(deck)
        deck_index = list(range(size))
        result = [None] * size
        while len(deck_index) > 0:
            i = deck_index.pop(0)
            result[i] = deck.pop(0)
            if len(deck_index):
                deck_index.append(deck_index.pop(0))

        return result


m = Solution()
print(m.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
