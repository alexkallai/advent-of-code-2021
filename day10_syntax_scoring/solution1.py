#!/usr/bin/python

import os, sys, copy

def wasThereSyntaxError(bracketDict):
    for key in bracketDict:
        if bracketDict[key] < 0:
            print(bracketDict)
            print("There is syntax error in line {}, with character: {}".format(lineIndex, key))
            errorSum += bracketErrorValueDict[ character ]
            print("bracketErrorValueDict [character]: ",bracketErrorValueDict[ character ])
            break
    

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

    errorSum = 0
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

            #input()

    print("The sum of errors in the whole file:", errorSum)


if __name__ == "__main__":
    main()