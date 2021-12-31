"""
Advent of Code 2021
Day 19 Challenge Part 1

Task:
Your probe has released scanners and beacons.
A scanner can detect beacons up to 1000 units away in any of the X,Y,Z directions.
However, scanners cannot detect other scanners, or their own rotational direction.
Each scanner reports a list of the xyz coordinates of detected beacons relative to them, following their own xyz conventions.
You can reconstruct a 3d map of the region by finding pairs of scanners that have at least 12 overlapping beacons.
Given the list of each scanner's detected beacons, reconstruct the map, and find the number of unique beacons.

Consider scanner 0 to be at 0,0,0

Could not complete, I have left some completed functions for records.
"""
import numpy as np
from itertools import permutations

def rotationTransforms():
    out = []
    for x in [-1,1]:
        for y in [-1,1]:
            for z in [-1,1]:
                for p in permutations([[x,0,0],[0,y,0],[0,0,z]]):
                    matrix = np.array(p)
                    if np.linalg.det(matrix)==1:
                        out.append(matrix)
    return out

def checkMatch(rotations,scan0,scan1):
    for rot in rotations:
        rotScan1 = [rot.dot(beacon) for beacon in scan1]

    
def getInput():
	with open('day19puzzle1input.txt','r') as f:
		lines = f.read()
    lines = lines.split("\n\n")
    scanners = []
    for line in lines:
        scanners.append(np.array(list(int(x) for x in line.strip().split(','))))
	return scanners

def manhattenDistance(point1,point2):   
    return sum(abs(e1-e1) for e1,e2 in zip(point1,point2)
    
def relatives(scan,point):
    neighbours = []
    for pt in [x for x in scan if x[:] != point[:]]:
        neighbours.append(manhattenDistance(pt,point))
    return neighbours.sort()
           
def main():
	scanners = getInput()
	print(scanners)
	
if __name__ == "__main__":
	main()


		