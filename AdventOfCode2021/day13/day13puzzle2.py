"""
Advent of Code 2021
Day 13 Challenge Part 2

Task: A large sheet of transparent paper has dots on it at certain points. 
Let the x axis increase to the right, and the y axis increase downward, with the origin in the top left corner.
Folding the paper along given horizontal and vertical lines transforms the dots.
Dots may overlap, which reduces the number of visible dots.
Dots will not be on folding lines.
After all folds, the dots will form a passcode of 8 capital letters.
Given the coordinates of dots, and a series of fold lines, what is the passcode?
"""

def getInput():
	"""
	Reads the input data from a file in the same directory.
	Output: a list of lists, with the list at 0 containing a list of points [x,y], and the list at 1 containing fold lines [axis,coordinate]
	"""
	with open("day13puzzle1input.txt",'r') as f:
		input = f.readlines()
	sep = input.index("\n")
	dots = []
	folds = []
	for i in range(sep):
		dots.append(list(int(x) for x in input[i].strip().split(',')))
	for fold in input[sep+1:]:
		folds.append(fold.strip().split(' ')[-1].split('='))
	return [dots,folds]

def foldSheet(points,direction,lineCoord):
	"""
	Applies horizontal/vertical reflection to the given points about the given vertical/horizontal line.
	Input: a list of points [x,y], a direction of reflection line 'x' or 'y', and the invariant coordinate of the line as an integer.
	Output: a list of reflected points [x,y]
	"""
	outpoints=[]
	if direction == 'x':
		for pt in points:
			if pt[0] < lineCoord:
				outpoints.append(pt)
			else:
				outpoints.append([lineCoord - (pt[0] - lineCoord),pt[1]])
	elif direction == 'y':
		for pt in points:
			if pt[1] < lineCoord:
				outpoints.append(pt)
			else:
				outpoints.append([pt[0],lineCoord - (pt[1] - lineCoord)])
	return outpoints
	
def consolidate(inDots):
	"""
	Removes duplicate points from list.
	Input: a list of points [x,y]
	Output: a list of points [x,y]
	"""
	outDots = []
	dotTracker = []
	for pt in inDots:
		temp = f"{pt[0]},{pt[1]}"
		if temp not in dotTracker:
			dotTracker.append(temp)
			outDots.append(pt)
	return outDots
	
def displayDots(dots):
	"""
	Displays the list of dots to the console visually.
	Input: a list of points [x,y].
	"""
	xlen = max(list(x[0] for x in dots))
	ylen = max(list(x[1] for x in dots))
	display = []
	for i in range(ylen+1):
		temp = []
		for j in range(xlen+1):
			temp.append('.')
		display.append(temp)
	for pt in dots:
		display[pt[1]][pt[0]] = '#'
	for line in display:
		print(line)
		
	

def main():
	###First, read the input from file.
	input = getInput()
	dots = input[0]
	folds = input[1]
	###Next, apply each fold to the dots, remove duplicate dots, and output the number of remaining dots to the console.
	for fold in folds:
		dots = consolidate(foldSheet(dots,fold[0],int(fold[1])))
		print(len(dots))
	###Finally, display the final dots to the console.
	displayDots(dots)
	
if __name__ == "__main__":
	main()