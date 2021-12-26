#!/usr/bin/python

from PIL import Image
import numpy as np
import os, sys, copy, time, gc

def main():
    log = False
    print("The received argument: {}".format(sys.argv[1]))
    #read in the data
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    fishes = []
    #read the lines into a list
    fishes.append(lines[0].split(","))
    fishes = fishes[0]
    for index, fish in enumerate(fishes): 
        fishes[index] = int(fish)
    print("Fishes: ",fishes)
    
    addedFishList = []
    #81 because range is not inclusive    
    for day in range(257):
        gc.collect(2)
        print("Day:",day)
        startTime = time.time()
        #helper list
        for index, fish in enumerate(fishes):
            if index == 0:
                fishes.extend(addedFishList)
                addedFishList.clear()
            if fish == 0:
                    fishes[index] = 6
                    addedFishList.append(8) #so the list does not change during iteration
            else:
                    fishes[index] -= 1
        print("Cycle time: ", time.time()-startTime )
        print("The actual number of fishes is: ", len(fishes))

    print("The total number of fishes at the final day is: ", len(fishes))

if __name__ == "__main__":
    main()