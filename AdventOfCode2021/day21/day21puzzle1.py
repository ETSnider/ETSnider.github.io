"""
Advent of Code 2021
Day 21 Challenge Part 1

Task:
You are challenged to a game of Dirac Dice. This consists of a single die, two pawns, and a game board with a circular track and spaces marked 1 through 10 clockwise.
You start on a random space given by your puzzle input. Player 1 goes first.

Players take turns moving. Each player rolls the die 3 times, sums the numbers, and moves that many spaces forward around the track.
Each space you stop on, the space number is added to your score. The game ends when any player's score reaches 1000.
Because the first game is a practice game, you use a deterministic D100 instead.
	This always rolls 1 first, then 2, then 3, all the way to 100, then it goes back to 1.
What do you get when you multiply the score of the losing player by the number of times the die was rolled during the game?	
"""

def getInput():
	with open("day21input.txt",'r') as f:
		lines = f.readlines()
	out = []
	for line in lines:
		out.append(int(line.strip().split()[-1]))
	return out
	
class DD100:
	"""
	A deterministic D100. Rolls numbers in range(1,101) in increasing order. 
	"""
	def __init__(self):
		self.rollCount = 0
		self.value = 0

	def roll(self):
		self.rollCount += 1
		out = self.value 
		self.value += 1
		self.value = self.value % 100
		return out + 1
		
	def getRollCount(self):
		return self.rollCount

class Player:
	def __init__(self,start):
		self.position = start - 1
		self.score = 0
		
	def getPosition(self):
		return self.position + 1
		
	def getScore(self):
		return self.score
	
	def move(self,steps):
		self.position += steps
		self.position = self.position % 10

def turn(die, player):
	###Rolls the given die 3 times, then moves the player forward and increases their score accordingly.
	moveSum = 0
	for _ in range(3):
		moveSum += die.roll()
	player.move(moveSum)
	player.score += player.getPosition()
	
def main():
	###First, read the starting positions of the characters from a file.
	startPositions = getInput()
	###Use these to create the players.
	player1 = Player(startPositions[0])
	player2 = Player(startPositions[1])
	###Also initialize the deterministic d100
	die = DD100()
	###Play through the games until one player wins
	while(player1.getScore()<1000 and player2.getScore()<1000):
		turn(die,player1)
		if player1.getScore()>=1000:
			break
		turn(die,player2)
	###Check the scores of the players to determine the score of the loser
	loserScore = min(player1.getScore(),player2.getScore())
	###Multiply the loser's score by the number of dice rolls, and output the result to the console
	rolls = die.getRollCount()
	print(rolls,loserScore,rolls*loserScore)

if __name__ == "__main__":
	main()