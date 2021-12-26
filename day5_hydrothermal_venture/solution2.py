#!/usr/bin/python

from PIL import Image
import numpy as np
import os, sys, copy

def main():
    print("The received argument: {}".format(sys.argv[1]))
    #read in the data
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    data = []
    #read the lines into a list
    for coordinatePairIndex, coordinatePair in enumerate(lines):
        data.append( coordinatePair.replace("\n","").split(" -> ") )
    
    for coordinatePairIndex, coordinatePair in enumerate(data):
        coordinatePair[0] = coordinatePair[0].split(",")
        coordinatePair[1] = coordinatePair[1].split(",")

        coordinatePair[0][0] = int(coordinatePair[0][0])
        coordinatePair[0][1] = int(coordinatePair[0][1])
        coordinatePair[1][0] = int(coordinatePair[1][0])
        coordinatePair[1][1] = int(coordinatePair[1][1])

    w, h = 1000, 1000
    imgData = np.zeros((h, w, 3), dtype=np.uint8)
    
    incrementValue = 20 
    for rowIndex, row in enumerate(data):
        #check if the lines are vertical or horizontal
        if row[0][0] == row[1][0]: #x coordinates are equal
            print("Case1: ", row)
            for y in range( row[0][1], 
                           row[1][1]+1 if (row[0][1] < row[1][1]) else row[1][1]-1, 
                           1 if (row[0][1] < row[1][1]) else -1 ):
                #print("y: ", y)
                imgData[ row[0][0] ][ y ][1] = imgData[ row[0][0] ][ y ][1] + incrementValue 

        if row[0][1] == row[1][1]: #y coordinates are equal
            print("Case2: ", row)
            for x in range( row[0][0], 
                            row[1][0]+1 if (row[0][0] < row[1][0]) else row[1][0]-1, 
                            1 if (row[0][0] < row[1][0]) else -1 ):
                #print("x: ", x)
                imgData[ x ][ row[0][1] ][1] = imgData[ x ][ row[0][1] ][1] + incrementValue
        #in case it's 45 degrees (checked, all are 45)
        if row[0][0] != row[1][0] and row[0][1] != row[1][1]: 
            print("Drawing 45 degree line from x1-{} y1-{} and x2-{} y2-{}".format(row[0][0], row[0][1], row[1][0], row[1][1],  ) )
            diffX1X2 = abs(row[0][1] - row[1][1]) 
            print("Difference: ",diffX1X2)
            xCoordMultiplier = -1 if (row[0][0] - row[1][0]) > 0 else 1
            yCoordMultiplier = -1 if (row[0][1] - row[1][1]) > 0 else 1

            for actualDiff in range(diffX1X2+1):
                print("Actual diff:", actualDiff)
                print("The actual incremented coordinate: ", row[0][0] + (actualDiff)*xCoordMultiplier, row[0][1] + (actualDiff)*yCoordMultiplier)
                imgData[ row[0][0] + (actualDiff)*xCoordMultiplier ][ row[0][1] + (actualDiff)*yCoordMultiplier ][1] +=  incrementValue
    input()

    numberOfOverlaps = 0
    for xindex, row in enumerate(imgData):
        for yindex, column in enumerate(row):
            if column[1] > incrementValue: 
                #print("column[1]: {} - {} -- {} ".format(xindex, yindex, column[1]))
                numberOfOverlaps += 1
    print("The number of overlaps: ", numberOfOverlaps)

    img = Image.fromarray(imgData, 'RGB')
    img.save('solution1.png')
    img.show()

if __name__ == "__main__":
    main()