import io
"""
Advent of Code
Day 4 Challenge Part 1

Task: 
Given a series of bingo numbers, and a list of bingo boards, determine which board would win first.
Then calculate the score of that board by summing the numbers that have not been called together, and multiplying it by the last number called.
"""
def main():
    ###First, read the input from a file in the same directory.
	f = open("day4puzzle1input.txt",'r')
	input = f.readlines()
	f.close()
	###Then extract the bingo numbers in the order that they will be called.
	bingoNums=[]
	temp = input[0].split(',')
	for num in temp:
		bingoNums.append(int(num))
	###Next, extract each board as a list of lists of integers of size 5x5, and add it to a list of boards.
	bingoBoards = [[]]
	boardNum = 0
	
	for line in input[2:]:
		if line=='\n':
			boardNum += 1
			bingoBoards.append([])
			continue;
		else:
			line = line.split()
			temp=[]
			for num in line:
				temp.append(int(num))
			bingoBoards[boardNum].append(temp)
	
    ###Call the numbers one by one, mark off each board with that number in it, and check if it has a bingo.
    ####Once one board wins, print its score to the console.
	for numcall in bingoNums:
		for boardnum in range(len(bingoBoards)):
			for x in range(5):
				for y in range(5):
					if bingoBoards[boardnum][x][y] == numcall:
						bingoBoards[boardnum][x][y] = 'x'
			sumUnchecked = checkWin(bingoBoards[boardnum])
			if sumUnchecked!=-1:
				print(boardnum)
				for line in bingoBoards[boardnum]:
					print(line)
				print(sumUnchecked)
				print(numcall*sumUnchecked)
				return

def checkWin(board):
    """
    Checks a board to see if it is has a bingo. 
    Input: A list of lists of integers, of size 5x5.
    Output: The sum of the unmarked squares on the board as an integer if it has a bingo, or -1 otherwise.
    """
	for horizontal in range(5):
		numX = 0
		for i in range(5):
			if board[horizontal][i] == 'x':
				numX += 1
		if numX == 5:
			return calcScore(board)
	
	for vertical in range(5):
		numX = 0
		for i in range(5):
			if board[i][vertical] == 'x':
				numX += 1
		if numX == 5:
			print(vertical)
			print(board[0][vertical],board[1][vertical],board[2][vertical],board[3][vertical],board[4][vertical])
			return calcScore(board)
	
	numX = 0
	for diag in range(5):
		if board[diag][diag] == 'x':
			numX += 1
	if numX == 5:
		return calcScore(board)
	
	numX = 0
	for diag in range(5):
		if board[diag][4-diag] == 'x':
			numX += 1
	if numX == 5:
		return calcScore(board)
		
	return -1
	
def calcScore(board):
    """
    Calculates part of the score of a bingo board. Sums all the unmarked numbers.
    Input: A list of lists of integers of size 5x5.
    """
	sum = 0
	for i in range(5):
		for j in range(5):
			if board[i][j] != 'x':
				sum += int(board[i][j])
	return sum
	
def printBoard(board):
    """
    A custom print function for bingo boards.
    Input: A list of lists.
    """
	for line in board:
		print(line)
	
if __name__ == "__main__":
	main()