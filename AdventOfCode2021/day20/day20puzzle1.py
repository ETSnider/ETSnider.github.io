"""
Advent of Code 2021
Day 20 Challenge Part 1

Task:
   You have received an immage from your scanners, but it is noisy. You must enhance it using the provided image enhancement algorithm.
For each pixel, consider also the pixels around it. They form a 3x3 array of light pixels (#) and dark pixels (.).
Convert this into a string from top left to bottom right, and convert dark pixels to 0s, and light pixels to 1s.
This resultant 9 bit number corresponds to that numbered pixel in the image enhancement algorithm.
The given image is only a small piece of the full infinite image: consider all outside pixels to be dark.

Given the the input algorithm and image, apply the algorithm twice, and count the number of lit pixels.
"""

def getInput():
    """
    Reads the input image and algorithm from file.
    Output: a string of length 512, and an image (2d array of characters)
    """
    with open("day20input.txt",'r') as f:
        lines = f.readlines()
    alg = lines[0].strip()
    image = list(line.strip() for line in lines[2:])
    return alg, image
    
def applyAlg(image,alg):
    """
    Applies the enhancement algorithm to the image.
    Input: a m*n image, and a string of length 512
    Output: a (m-1)*(n-1) image
    """
    outImage = []
    for i in range(1,len(image)-1):
        outImage.append([])
        for j in range(1,len(image[0])-1):
            chunk = [image[i-1][j-1:j+2],image[i][j-1:j+2],image[i+1][j-1:j+2]]
            chunkNum = enhanceChunk(chunk)
            #print(chunkNum)
            outImage[i-1].append(alg[chunkNum])
    return outImage

def enhanceChunk(chunk):
    """
    Finds the 9bit number corresponding to the input chunk.
    Input: a 3x3 image chunk
    Output: an integer in range(512)
    """
    pixelString = sum(chunk,[])
    pixelDict = {'.':'0','#':'1'}
    numString = "".join(list(pixelDict[c] for c in pixelString))
    #print(numString)
    return int(numString,2)
    
def padImage(image,i):
    """
    Takes an image, and pads it.
    Input: a m*n image
    Output: a (m+2)*(n+2) image
    """
    pixelList = ['.','#']
    xlen = len(image[0])
    ylen = len(image)
    outImage = [[pixelList[i]]*(xlen+2)]
    for lineNum in range(ylen):
        outImage.append([pixelList[i]])
        for c in image[lineNum]:
            outImage[lineNum+1].append(c)
        outImage[lineNum+1].append(pixelList[i])
    outImage.append([pixelList[i]]*(xlen+2))
    return outImage
    
def countLit(image):
    """
    Counts the number of lit pixels in an image.
    Input: a 2d array of characters.
    Output: an integer.
    """
    count = 0
    for line in image:
        for c in line:
            if c == '#':
                count += 1
    return count

def main():
    ###First, read the image and algorithm from file
    alg, image = getInput()
    print(len(image),len(image[0]))
    ###Next, apply the image enhancement algorithm the requisite number of times
    ###After 2 interations, count the number of lit pixels, and output that numbers to the console.
    numApplications = 2
    #print(image)
    for _ in range(3):
        image = padImage(image,0)
    for i in range(numApplications):
        #print(image)
        image = padImage(image,i%2)
        image = applyAlg(image,alg)
    litPix = countLit(image)
    print(litPix)  
        

    
    
if __name__ == "__main__":
    main()