"""
Advent of Code 2021
Day 1 Challenge Part 2

Task: read a series of number from a file, and count the number of times a rolling average of four numbers is greater than the average of the previous four numbers.
"""
import sys

#import requests
#from bs4 import BeautifulSoup

def getList():
    """
	Read a list of numbers from a file in the same directory.
	Output: A list of integers.
	"""
    f = open('day1puzzle1input.txt','r')
    nums = f.read()
    f.close()
    nums = nums.split()
    for n in range(len(nums)):
        nums[n]=int(nums[n])
    return nums
    
def countAvgDrops(numlist):
    """
    Counts the number of times the average of three consecutive numbers is greater than an average of three consecutive numbers one step behind the frame.
    As a shortcut, ignore the shared numbers, and only consider the 1 number differences.
    Output: An integer.
    """
    count=0
    for num in range(len(numlist)-2):
        if numlist[num+2]-numlist[num-1]>0:
            count=count+1
    return count
	
def main():
    
    #testnums=[199,200,208,210,200,207,240,269,260,263]
    #print(countAvgDrops(testnums))
    ###First, read the list of numbers from a file.
    numlist = getList()
    ###Then, count the number of drops of averages, and output that count to the console.
    count = countAvgDrops(numlist)
    print(str(count))
    return 1

if __name__=="__main__":
    main()
