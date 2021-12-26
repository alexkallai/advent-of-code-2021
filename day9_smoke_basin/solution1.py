#!/usr/bin/python

import os, sys, copy

def main():
    log = False
    print("The received argument: {}".format(sys.argv[1]))
    #read in the data
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    heightMap = []
    #read the lines into a list
    for index, line in enumerate(lines):
        heightMap.append( list(line.replace("\n", "")) )
        for i, member in enumerate(heightMap[index]): heightMap[index][i] = int(heightMap[index][i])

    riskLevelSum = 0
    for xIndex, row in enumerate(heightMap):
        for yIndex, inspectedNumber in enumerate(row):
            if ( #eliminate the possibility of indexin out of range with inline if
                (inspectedNumber < (heightMap[xIndex+1][yIndex]) if xIndex<99 else 100) and
                (inspectedNumber < (heightMap[xIndex-1][yIndex]) if xIndex>0 else 100) and
                (inspectedNumber < (heightMap[xIndex][yIndex+1]) if yIndex<99 else 100) and
                (inspectedNumber < (heightMap[xIndex][yIndex-1]) if yIndex>0 else 100) 
                ): 
                print("Found a local low point!")
                riskLevelSum += 1+heightMap[xIndex][yIndex]
                pass #that is a local low point
    print("The risk level sum is:", riskLevelSum)


if __name__ == "__main__":
    main()