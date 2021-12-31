"""
Advent of Code 2021
Day 22 Challenge Part 1

Task:
A reactor consists of a 3-dimensional grid of cubes, which may each be on or off. At the startof the reboot process, they are all off.
There are a series of steps to boot the reactor, each specifying a cuboid and whether to turn the cubes on or off.

Find the number of cubes that are on after all the steps.
"""

def getInput():
    with open("day22input.txt",'r') as f:
        input = f.readlines()
    data = []
    for line in input:
        line=line.strip().split()
        op = line[0]
        line = line[1].split(',')
        x = [int(c) for c in line[0].split('=')[1].split('..')]
        y = [int(c) for c in line[1].split('=')[1].split('..')]
        z = [int(c) for c in line[2].split('=')[1].split('..')]
        data.append([op,x[:],y[:],z[:]])
    return data

class Cuboid:
    def __init__(self,area):
        self.xrange = area[0]
        self.yrange = area[1]
        self.zrange = area[2]
        self.volume = getVolume(self.xrange,self.yrange,self.zrange)
        
    def __repr__(self):
        return str([self.xrange,self.yrange,self.zrange])
    
    def findIntersectionVolume(self,other):
        def findInterSection1D(self,range,otherRange):
            intersection = [x for x in range if x in otherRange]
            if len(intersection)>1:
                return [min(intersection),max(intersection)] 
            elif len(intersection) == 1:
                return [min(intersection),max(intersection)]
            else:
                return None
        #print(other)
        x = findInterSection1D(self,self.xrange,other.xrange)
        y = findInterSection1D(self,self.yrange,other.yrange)
        z = findInterSection1D(self,self.zrange,other.zrange)
        if x!=None and y!=None and z!=None:
            return getVolume(x,y,z)

def getVolume(xrange,yrange,zrange):
    return (xrange[1]-xrange[0])*(yrange[1]-yrange[0])*(zrange[1]-zrange[0])

def operationHandler(instruction,onCore,offCore):
    if instruction[0] == 'on':
        onHandler(instruction[1:],onCore)
    elif instruction[0] == 'off':
        offHandler(instruction[1:],offCore)
    else:
        raise Exception(f"Invalid instruction: {instruction[0]}")
    
def onHandler(data,onCore):
    onCore.append(Cuboid(data))
    
def offHandler(data,offCore):
    offCore.append(Cuboid(data))
    
def findVolume(onCore,offCore):
    volume = 0
    while len(onCore)>0 or len(onCore)>0:
        while len(onCore)>0:
            cube = onCore.pop(0)
            if len(onCore)>0:
                for other in onCore:
                    ranges = cube.findIntersectionVolume(other)
                    if ranges != None:
                        offCore.append(Cuboid(ranges))
            volume += cube.volume
        
        while len(offCore)>0:
            cube = offCore.pop(0)
            if len(offCore)>0:
                for other in offCore:
                    ranges = cube.findIntersectionVolume(other)
                    if ranges != None:
                        onCore.append(Cuboid(ranges))
            volume -= cube.volume
    
    return volume
    
def main():
    data = getInput()
    onCore = []
    offCore = []
    
    for instruction in data:
        operationHandler(instruction,onCore,offCore)
    
    volume = findVolume(onCore,offCore)
    print(volume)
    
if __name__ == "__main__":
    main()