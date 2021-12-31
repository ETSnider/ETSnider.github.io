"""
Advent of Code 2021
Day 21 Challenge Part 2

Task:
You are challenged to a game of Dirac Dice. This consists of a single die, two pawns, and a game board with a circular track and spaces marked 1 through 10 clockwise.
You start on a random space given by your puzzle input. Player 1 goes first.

Players take turns moving. Each player rolls the die 3 times, sums the numbers, and moves that many spaces forward around the track.
Each space you stop on, the space number is added to your score. The game ends when any player's score reaches 21.
This game uses a dirac die: when rolled, it splits the universe into 3, with the first univers rolling a 1, the second rolling a 2, and the third rolling a 3.
Find all possible outcomes. Which player wins in more universes, and how many universes does the player win in?
"""

from collections import Counter,defaultdict
from itertools import product

def getInput():
	with open("day21input.txt",'r') as f:
		lines = f.readlines()
	out = []
	for line in lines:
		out.append(int(line.strip().split()[-1]))
	return out

def findWinners(multiverse,winCounts):
    """
    Counts the number of completed games won by each player in the current multiverse, and removes those games.
    Input: a multiverse (player1_position, player2_position, player1_score, player2_score), and a list [player1_victories, player2_victories]
    Modifies in place the inputs.
    """
    for universe in list(multiverse):
        (p1,p2,s1,s2) = universe
        if s1>=21:
            winCounts[0] += multiverse[universe]
            del multiverse[universe]
        elif s2>=21:
            winCounts[1] += multiverse[universe]
            del multiverse[universe]
	
def main():
    ###Read the starting positions from file
	starts = getInput()
	#starts = [4,8]
    ###Add the initial state to the multiverse
	multiverse = {(starts[0],starts[1],0,0):1}
    ###Find the sum of each permutation of rolls, and the frequency of each possible sum
	possibleMoves = [sum(x) for x in product((1,2,3), repeat = 3)]
	moveCounts = sorted(Counter(possibleMoves).items())
	#print(possibleMoves)
	#print(moveCounts)
	def mov1(multiverse):
        """
        Enacts player 1's turn on each universe in the multiverse
        Input: a multiverse
        Output: a multiverse
        """
		nonlocal moveCounts, possibleMoves
		outMultiverse = defaultdict(int)
		for ((p1,p2,s1,s2), numUniverses), (move,moveCount) in product(multiverse.items(),moveCounts):
			p1 = p1+move
			if p1>10:
				p1 -= 10
			s1 += p1
			outMultiverse[(p1,p2,s1,s2)] += numUniverses*moveCount
		return outMultiverse
			
	def mov2(multiverse):
        """
        Enacts player 2's turn on each universe in the multiverse
        Input: a multiverse
        Output: a multiverse
        """
		nonlocal moveCounts, possibleMoves
		outMultiverse = defaultdict(int)
		for ((p1,p2,s1,s2), numUniverses), (move,moveCount) in product(multiverse.items(),moveCounts):
			p2 = p2+move
			if p2>10:
				p2 -= 10
			s2 += p2
			outMultiverse[(p1,p2,s1,s2)] += numUniverses*moveCount
		return outMultiverse
	###Alternate turns on the multiverse, removing universes with completed games and counting how many games each player won	
	winCounts = [0,0]
	while len(multiverse)>0:
		multiverse = mov1(multiverse)
		findWinners(multiverse,winCounts)
		multiverse = mov2(multiverse)
		findWinners(multiverse,winCounts)
    ###Output the win counts to the console
	print(winCounts)
	
if __name__ == "__main__":
	main()