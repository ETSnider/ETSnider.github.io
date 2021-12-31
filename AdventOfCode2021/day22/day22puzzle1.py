"""
Advent of Code 2021
Day 22 Challenge Part 1

Task:
A reactor consists of a 3-dimensional grid of cubes, which may each be on or off. At the startof the reboot process, they are all off.
There are a series of steps to boot the reactor, each specifying a cuboid and whether to turn the cubes on or off.
The initialization procedure only uses points from [-50,50]^3
Find all the cubes that are on after all the steps.
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

def operationHandler(opList,core):
    if opList[0] == 'on':
        return turnOn(opList[1:],core)
    elif opList[0] == 'off':
        return turnOff(opList[1:],core)
    else:
        raise Exception(f'Improper operation: {opList[0]}')
        
def turnOn(region,core):
    x,y,z = region
    if x[1]<-50 or x[0]>50 or y[1]<-50 or y[0]>50 or z[1]<-50 or z[0]>50:
        return
    for i in range(x[0],x[1]+1):
        for j in range(y[0],y[1]+1):
            for k in range(z[0],z[1]+1):
                if i in range(-50,51) and j in range(-50,51) and k in range(-50,51):
                    core[i+50][j+50][k+50] = 1

def turnOff(region,core):
    x,y,z = region
    if x[1]<-50 or x[0]>50 or y[1]<-50 or y[0]>50 or z[1]<-50 or z[0]>50:
        return
    for i in range(x[0],x[1]+1):
        for j in range(y[0],y[1]+1):
            for k in range(z[0],z[1]+1):
                if i in range(-50,51) and j in range(-50,51) and k in range(-50,51):
                    core[i+50][j+50][k+50] = 0

def countOn(core):
    return sum([sum([sum(edge) for edge in flat]) for flat in core])
    
def buildCore():
    core = []
    for i in range(101):
        flat = []
        for j in range(101):
            flat.append([0]*101)
        core.append(flat[:])
    return core
    
def main():
    data = getInput()
    core = buildCore()
    
    for instruction in data:
        operationHandler(instruction,core)
    
    activeCount = countOn(core)
    print(activeCount)
    
if __name__ == "__main__":
    main()