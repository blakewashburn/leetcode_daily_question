"""
Title:
950. Reveal Cards In Increasing Order

Description:
	You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].
	You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.
	You will do the following steps repeatedly until all cards are revealed:

		Take the top card of the deck, reveal it, and take it out of the deck.
		If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
		If there are still unrevealed cards, go back to step 1. Otherwise, stop.
	Return an ordering of the deck that would reveal the cards in increasing order.
	Note that the first entry in the answer is considered to be the top of the deck.

Examples:
	Input: deck = [17,13,11,2,3,5,7]
	Output: [2,13,3,11,5,17,7]
	Explanation: 
	We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
	After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
	We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
	We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
	We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
	We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
	We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
	We reveal 13, and move 17 to the bottom.  The deck is now [17].
	We reveal 17.
	Since all the cards revealed are in increasing order, the answer is correct.

	Input: deck = [1,1000]
	Output: [1,1000]


Constrains:
	1 <= deck.length <= 1000
	1 <= deck[i] <= 10^6
	All the values of deck are unique.
"""


class Solution(object):
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:

        # First we need to sort the deck
        deck.sort()
        new_deck = [-1] * len(deck)
        remaining_indexes = [i for i in range(len(deck))]

        # Loop until we have placed a card at every index in the new_deck
        while remaining_indexes:
            new_remaining_indexes = []

            # Loop over our set of remaining_indexes
            for i in range(len(remaining_indexes)):

                # if even index, place next card
                if i % 2 == 0:
                    new_deck[remaining_indexes[i]] = deck.pop(0)
                else:
                    # add odd index to next loop over remaining indexes
                    new_remaining_indexes.append(remaining_indexes[i])
            
            # if the last thing we did was place a card, we need to move the "next in line card" to the back
            # also need to make sure that we did not place our last card
            if i % 2 == 0 and len(remaining_indexes) > 1:
                temp = new_remaining_indexes.pop(0)
                remaining_indexes = new_remaining_indexes
                remaining_indexes.append(temp)
            else:
                remaining_indexes = new_remaining_indexes
        
        return new_deck


        # Building an example
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        # [1, _, 2, _, 3, _, 4, _, 5, _, 6, _, 7, _, 8]
        # [1, A, 2, B, 3, C, 4, D, 5, E, 6, F, 7, G, 8]
        # [2, B, 3, C, 4, D, 5, E, 6, F, 7, G, 8, A]
        # [3, C, 4, D, 5, E, 6, F, 7, G, 8, A, B]
        # [4, D, 5, E, 6, F, 7, G, 8, A, B, C]
        # [5, E, 6, F, 7, G, 8, A, B, C, D]
        # [6, F, 7, G, 8, A, B, C, D, E]
        # [7, G, 8, A, B, C, D, E, F]
        # [8, A, B, C, D, E, F, G]
        # [B, C, D, E, F, G, A]          Now we want to repeat with what we have left!
        # [D, E, F, G, A, C]
        # [F, G, A, C, E]
        # [A, C, E, G]
        # [E, G, C]
        # [C, G]
        # [G]
        # []




if __name__ == "__main__":
	sol = Solution()


	deck = [17,13,11,2,3,5,7]			# -> [2,13,3,11,5,17,7]
	deck = [1,1000]						# -> [1,1000]


	print(sol.deckRevealedIncreasing(deck=deck))