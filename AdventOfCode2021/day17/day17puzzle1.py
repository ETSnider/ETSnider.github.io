"""
Advent of Code 2021
Day 17 Challenge

Task:
You are firing a probe to check an oceanic trench. The probe can be fired with any integer of x and y velocity.
X is positive in the forward direction, Y is positive upwards.
The probe starts at 0,0
Each step, the following occurs in this order:
	The X position changes by the X velocity
	The Y position increases by the Y velocity
	The X velocity changes 1 toward 0.
	The Y velocity decreases by 1
The probe must be within the target area after any step.
Part 1: What is the highest Y position the probe can reach while still entering the target area?
Part 2: How many initial velocities get the probe into the target area?
"""
import re
def getInput():
	with open("day17puzzle1input.txt",'r') as f:
		line = f.read()
	xrange = [int(x) for x in re.search(r"x=(\d+\.\.\d+),",line).group(1).split('..')]
	print(xrange)
	print(line)
	yrange = [int(y) for y in line.split()[-1].split('=')[-1].split('..')]
	print(yrange)
	return [xrange[:],yrange[:]]
	
def checkInTarget(targetRange,point):
	if min(targetRange[0]) <= point[0] <= max(targetRange[0]) and min(targetRange[1]) <= point[1] <= max(targetRange[1]):
		return True
	return False
	
def checkInBounds(targetRange,point):
	if point[0] > max(targetRange[0]) or point[1] < min(targetRange[1]):
		return False
	return True

def checkFall(targetRange,point,velocity):
	if velocity[0]==0 and point[0] < min(targetRange[0]):
		return True
	return False
	
def step(position,velocity):
	position[0] += velocity[0]
	position[1] += velocity[1]
	velocity[0] = velocity[0]-1 if velocity[0]>0 else 0
	velocity[1] -= 1
	
def checkPath(startVelocity, targetRange):
	position = [0,0]
	velocity = startVelocity[:]
	maxY = 0
	while(checkInBounds(targetRange,position) and not checkFall(targetRange,position,velocity)):
		step(position,velocity)
		#print([position,velocity])
		if position[1]>maxY:
			maxY = position[1]
		if checkInTarget(targetRange,position):
			return maxY
	return "long" if position[0]>max(targetRange[0]) else "short"
	
def checkVelocities(targetRange):
	maxY = 0
	goodVelocities = []
	##Check each forward velocity that doesnt send the probe past the target area in one step
	for xVel in range(max(targetRange[0])+1):
		##Check each vertical velocity greater than zero until the path passes the target area in x (checkPath returns "long")
		##if the maxY for this x velocity is less than the maxY for the previous x velocity, stop early
		prevMaxY = 0
		for yVel in range(min(targetRange[1]),1+max(targetRange[0])):
			print(xVel,yVel)
			currMaxY = 0
			pathResult = checkPath([xVel,yVel],targetRange)
			#print(pathResult)
			if pathResult == "long":
				break
			elif isinstance(pathResult, int):
				goodVelocities.append([xVel,yVel])
				currMaxY = max(pathResult, currMaxY)
				maxY = max(pathResult, maxY)
		if currMaxY < prevMaxY:
			break
		prevMaxY = currMaxY
	return maxY, goodVelocities
	
def main():
	targetRange = getInput()
	maxY, goodVel = checkVelocities(targetRange)
	print(maxY)
	print(len(goodVel))

if __name__ == "__main__":
	main()
