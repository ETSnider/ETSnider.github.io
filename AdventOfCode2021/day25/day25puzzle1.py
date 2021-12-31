"""
Advent of Code 2021
Day 25 Challenge Part 1

Task:
There are two herds of sea cucumbers.
One herd only moves in a straight line east, and the other only moves south.
They will only move if the space in front of them is clear.
Each step, first the east ones move east, then the south ones move south.
When a sea cucumber reaches the end of the map, they will try to move to the spot on the opposite side of the map.
What is the first step on which no sea cucumbers move?
"""

def getInput():
    with open("day25input.txt",'r') as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]
    
def moveEast(grid):
    moved=False
    newGrid = [[_ for _ in line] for line in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=='>' and grid[i][(j+1)%len(grid[i])] not in ['>','v']:
                moved=True
                newGrid[i][j]='.'
                newGrid[i][(j+1)%len(grid[i])]='>'
    grid=newGrid[:][:]
    return grid
                
def moveSouth(grid):
    moved=False
    newGrid = [[_ for _ in line] for line in grid]
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if grid[i][j]=='v' and grid[(i+1)%len(grid)][j] not in ['>','v']:
                moved=True
                newGrid[i][j]='.'
                newGrid[(i+1)%len(grid)][j]='v'
    grid=newGrid[:][:]
    return grid
    
def checkDiffGrids(aGrid,bGrid):
    for i in range(len(aGrid)):
        for j in range(len(aGrid[i])):
            if aGrid[i][j]!=bGrid[i][j]:
                return True
    return False
                
def main():
    grid = getInput()
    #print(len(grid),len(grid[0]))
    moved = True
    step = 0
    while (moved):
        step += 1
        start=grid[:][:]
        grid = moveEast(grid)
        grid = moveSouth(grid)
        moved = checkDiffGrids(start,grid)
    #print(start)   
    with open("day25output.txt",'w') as f:
        lines = ["".join(line) + '\n' for line in grid]
        f.writelines(lines)
    print(step)
        
if __name__ == "__main__":
    main()