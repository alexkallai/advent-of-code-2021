#!/usr/bin/python

import os, sys, copy

def main():
    log = False
    print("The received argument: {}".format(sys.argv[1]))
    #read in the data
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    syntaxData = []
    #read the lines into a list
    for index, line in enumerate(lines):
        syntaxData.append( list(line.replace("\n", "")) )

    bracketTranslateDict = {">":"<",
                            "}":"{",
                            ")":"(",
                            "]":"[" }
    bracketErrorValueDict = {">":25137,
                            "}":1197,
                            ")":3,
                            "]":57 }
    bracketCompletePointDict = {">":4,
                            "}":3,
                            ")":1,
                            "]":2 }

    bracketTranslateDictReverse = {   "<":">",
                                "{":"}",
                                "(":")",
                                "[":"]" }
    errorSum = 0
    completionStringPointList = []
    for lineIndex, line in enumerate(syntaxData):
        print("-----------------------------------------")
        print("---------------------LINE----------------")
        print("-----------------------------------------")
        skipLine = False
        openedBrackets = []
        for charIndex, character in enumerate(line):
            if (character == "<") or (character == "{") or (character == "(") or (character == "["):
                openedBrackets.append(character)
            if (character == ">") or (character == "}") or (character == ")") or (character == "]"):
                if openedBrackets[-1] != bracketTranslateDict[character]:
                    print("-----------------------------------------")
                    print(openedBrackets[-1],  bracketTranslateDict[character])
                    print("*********************************************************************************")
                    print("There is syntax error in line {}, with character: {}".format(lineIndex, character))
                    errorSum += bracketErrorValueDict[ character ]
                    print("errorSum was incremented to:", errorSum)
                    print("Skipping line...")
                    print("*********************************************************************************")
                    break
                else:
                    print("-----------------------------------------")
                    print("openedBrackets: ",openedBrackets)
                    print("Removing bracket from openedBrackets:", openedBrackets[-1])
                    openedBrackets.pop(-1)
                    print("openedBrackets: ",openedBrackets)
                    print("-----------------------------------------")
            complCharSum = 0
            if charIndex == len(line)-1:
                completionStringPointList.append(0)
                for complChar in reversed(openedBrackets):
                    completionStringPointList[-1] = completionStringPointList[-1] * 5 + bracketCompletePointDict[ bracketTranslateDictReverse[complChar] ]

    print(completionStringPointList)
    completionStringPointList.sort()
    print("The middle element of the completion string point list:", completionStringPointList[ int(len(completionStringPointList)/2) ] )


if __name__ == "__main__":
    main()