#!/usr/bin/python

import os, sys, copy

def main():
    log = False
    print("The received argument: {}".format(sys.argv[1]))
    #read in the data
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    segmentNoteLines = []
    #read the lines into a list
    for index, line in enumerate(lines):
        segmentNoteLines.append([ line.replace("\n", "").split(" | ")[0].split(),
                                 line.replace("\n", "").split(" | ")[1].split() ])
    numberOfKeywords = 0
    for index, segmentNoteLine in enumerate(segmentNoteLines):
        print(segmentNoteLine)
        for num in range(4):
            if  (len(segmentNoteLine[1][num]) == 2 or
                len(segmentNoteLine[1][num]) == 3 or
                len(segmentNoteLine[1][num]) == 4 or
                len(segmentNoteLine[1][num]) == 7):
                numberOfKeywords += 1
    print("The solution is:", numberOfKeywords)

if __name__ == "__main__":
    main()