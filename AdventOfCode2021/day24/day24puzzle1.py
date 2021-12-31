"""
Advent of Code 2021
Day 24 Challenge Part 1

Task:
You must build a new ALU.
It has input variables w,x,y,z, all starting with the value 0.
It also supports 6 constructions:
    inp a : read an input value and write it to variable all
    add a b: add a and b, then store in a
    mul a b: multiply a and b, then store in a
    div a b: a//b, store in a
    mod a b: a%b, store to a
    eql a b: 1 if a==b, 0 otherwise, store in a
In these, a will always be a variable, and b may be a variable or an integer
Once you have built it, it will continue its previous operation: validate the model number.
The model number is a 14-digit number consisting of only the digits 1-9. 0 cannot appear.
This number is evaluated through 14 inp instructions, each containing a single digit, from most to least significant.
Verification also has other restrictions, which must be discovered.
Find the largest 14 digit number accepted by the verification.
"""

def getInput():
    with open("day24input.txt",'r') as f:
        lines = f.readlines()
    instructions = [line.strip().split() for line in lines]
    return instructions
    
def interpret(line,wVar,xVar,yVar,zVar,inputList):
    varDict = {'w': wVar,'x':xVar,'y':yVar,'z':zVar}
    opDict = {'inp':getDigit,'add':addNums,'mul':mulNums,'div':divNums,'mod':modNums,'eql':checkEqual}
    
    op = line[0]
    aVar = varDict[line[1]]
    if len(line)==2:
        aVar[0] = getDigit(inputList)
        return wVar,xVar,yVar,zVar
    if line[2] in varDict:
        bVar = varDict[line[2]]
    else:
        bVar = [int(line[2])]
    aVar[0] = opDict[op](aVar,bVar)
    return wVar,xVar,yVar,zVar
    
def getDigit(inputList):
    return int(inputList.pop(0))

def addNums(a,b):
    #print(a,b)
    return a[0]+b[0]
    
def mulNums(a,b):
    return a[0]*b[0]
    
def divNums(a,b):
    return a[0]//b[0]
    
def modNums(a,b):
    return a[0]%b[0]
    
def checkEqual(a,b):
    return 1 if a[0]==b[0] else 0
    
def main():
    commands = getInput()
    
    for num in (_ for _ in range(int('9'*14),0,-1) if '0' not in str(_)):
        inputList = list(str(num))
        #print(inputList)
        wVar,xVar,yVar,zVar = [0],[0],[0],[0]
        for cmd in commands:
            interpret(cmd,wVar,xVar,yVar,zVar,inputList)
        if zVar[0] == 0:
            print(str(num))
            break

if __name__ == "__main__":
    main()