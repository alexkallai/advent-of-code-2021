#!/usr/bin/python

from PIL import Image
import numpy as np
import os, sys, copy

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
    for day in range(81):
        if log:
            print("")
        #helper list
        for index, fish in enumerate(fishes):
            if index == 0:
                fishes.extend(addedFishList)
                addedFishList.clear()
            if log:
                print("Day:",day)
                print("Actual index:",index)
                print("Before:",fishes)
            match fish:
                case 8:
                    fishes[index] -= 1
                case 7:
                    fishes[index] -= 1
                case 6:
                    fishes[index] -= 1
                case 5:
                    fishes[index] -= 1
                case 4:
                    fishes[index] -= 1
                case 3:
                    fishes[index] -= 1
                case 2:
                    fishes[index] -= 1
                case 1:
                    fishes[index] -= 1
                case 0:
                    fishes[index] = 6
                    addedFishList.append(8) #so the list does not change during iteration
                case _:
                    pass
            if log:
                print("After: ",fishes)
                print("AddedFishList:",addedFishList)
                input()

    print("The number of fishes is: ", len(fishes))

if __name__ == "__main__":
    main()