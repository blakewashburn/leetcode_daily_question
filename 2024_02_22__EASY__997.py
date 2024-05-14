"""
Title: 
997. Find the Town Judge

Description: 
  In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
  If the town judge exists, then:
    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
  You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
  Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example:
  Input: n = 2, trust = [[1,2]]
  Output: 2

  Input: n = 3, trust = [[1,3],[2,3]]
  Output: 3

  Input: n = 3, trust = [[1,3],[2,3],[3,1]]
  Output: -1

Constraints:
  1 <= n <= 1000
  0 <= trust.length <= 10^4
  trust[i].length == 2
  All the pairs of trust are unique.
  a_i != b_i
  1 <= ai, bi <= n

"""


class Solution:
  def findJudge(self, n: int, trust: list[list[int]]) -> int:
    
    # create a map of trust relationships
    trust_map = {}
    potential_trustees = []
    for i in range(1, n + 1):
      trust_map[i] = []
      potential_trustees.append(i)
    
    # keep track of people that give trust
    people_that_trust = set()

    # fill out map of trust relationships
    for trustee, trusted in trust:
      trust_map[trusted].append(trustee)
      
      # update set of people that have given trust
      if trustee not in people_that_trust:
        people_that_trust.add(trustee)

    # find who trusts no one
    potential_judge = list(set(potential_trustees) - people_that_trust)
    if len(potential_judge) != 1:
      return -1 

    # check that potential judge is trusted by everyone
    if len(list(set(potential_trustees) - set(trust_map[potential_judge[0]]))) > 1:
      return -1

    return potential_judge[0]
        


if __name__ == "__main__":
  sol = Solution()
  
  n, trust = 2, [[1,2]]     # -> 2
  # n, trust = 3, [[1,3],[2,3]]     # -> 3
  # n, trust = 3, [[1,3],[2,3],[3,1]]     # -> -1

  print(sol.findJudge(n=n, trust=trust))
