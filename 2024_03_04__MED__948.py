"""
Title: 
948. Bag of Tokens

Description: 
	You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] donates the value of tokeni.
	Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):
		Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
		Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
	Return the maximum possible score you can achieve after playing any number of tokens.

Example:
	Input: tokens = [100], power = 50
	Output: 0
	Explanation: Since your score is 0 initially, you cannot play the token face-down. You also cannot play it face-up since your power (50) is less than tokens[0] (100).

   	Input: tokens = [200,100], power = 150
	Output: 1
	Explanation: Play token1 (100) face-up, reducing your power to 50 and increasing your score to 1.
	There is no need to play token0, since you cannot play it face-up to add to your score. The maximum score achievable is 1.

	Input: tokens = [100,200,300,400], power = 200
	Output: 2
	Explanation: Play the tokens in this order to get a score of 2:
	Play token0 (100) face-up, reducing power to 100 and increasing score to 1.
	Play token3 (400) face-down, increasing power to 500 and reducing score to 0.
	Play token1 (200) face-up, reducing power to 300 and increasing score to 1.
	Play token2 (300) face-up, reducing power to 0 and increasing score to 2.
	The maximum score achievable is 2.

Constraints:
	0 <= tokens.length <= 1000
	0 <= tokens[i], power < 10^4

"""

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:

        # sort tokens so we can grab smallest and largest in O(1)
        tokens.sort()
        current_score = 0
        max_score = 0

        # loop through all tokens
        while tokens:

            # Check if we can increase score
            if power >= tokens[0]:

                # increase score by 1 and reduce power by smallest token value
                token_value = tokens.pop(0)
                power -= token_value
                current_score += 1
                max_score = max(current_score, max_score)

            else:

                # check if we can increase power
                if current_score > 0:

                    # increase power by largest token value and reduce score by 1
                    token_value = tokens.pop()
                    power += token_value
                    current_score -= 1
                else:

                    # if we cannot increase power or score, return max
                    return max_score
        
        return max_score
        

if __name__ == "__main__":
     
	sol = Solution()


	tokens, power = [100], 50			# -> 0
	# tokens, power = [200,100], 150			# -> 1
	# tokens, power = [100,200,300,400], 200		# -> 2
    
	print(sol.bagOfTokensScore(tokens=tokens, power=power))
