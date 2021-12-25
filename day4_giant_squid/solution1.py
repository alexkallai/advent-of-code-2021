#!/usr/bin/python

import os, sys, copy

def main():
    print("The received argument: {}".format(sys.argv[1]))
    #read in the data
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    #the first member of the list is the list of numbers
    #later the members must be cast to int!!!
    numberList = lines[0].replace("\n","").split(",")
    print("The list of input numbers:", numberList)
    
    #fill the list of boards 
    bingoBoardList = []
    i = 2
    while i <= len(lines)-5: #<--- the subtraction could be error
        #delete the endline characters, and make list of the numbers
        bingoBoardList.append([ lines[i].replace("\n","").split(),
                                lines[i+1].replace("\n","").split(), 
                                lines[i+2].replace("\n","").split(), 
                                lines[i+3].replace("\n","").split(), 
                                lines[i+4].replace("\n","").split() ]) 
        i += 6
    
    #Convert the read bingo boards into iterable int lists
    for a, valuea in enumerate(bingoBoardList):
        for b, valueb in enumerate(valuea):
            for c, valuec in enumerate(valueb):
                    bingoBoardList[a][b][c] = int(valuec)
    print("The list of boards is: ", bingoBoardList) 

    #create a same size list for results
    #it's not possible to create simply a copy of a list!!!
    bingoResultList = copy.deepcopy(bingoBoardList)

    #Create a same size list with 0-s
    for a, valuea in enumerate(bingoResultList):
        for b, valueb in enumerate(valuea):
            for c, valuec in enumerate(valueb):
                    bingoResultList[a][b][c] = int(0)
    print("The list of results is:\n ",bingoResultList)
    
    #iterate through all given numbers
    for numberIndex, number in enumerate(numberList):
        #go through the whole list of tables
        for tableIndex, table in enumerate(bingoBoardList):
            #where there is an equal number, set the same position 1 in the result list
            #go through the table and set the result
            for rowIndex, row in enumerate(table):
                for columnIndex, column in enumerate(row):
                    if int(number) == bingoBoardList[tableIndex][rowIndex][columnIndex]:
                        bingoResultList[tableIndex][rowIndex][columnIndex] = 1
            #check if the result list has a complete row or column anywhere
            for colRow in range(0,5):
                if ( (bingoResultList[tableIndex][colRow][0] == 1 and
                      bingoResultList[tableIndex][colRow][1] == 1 and
                      bingoResultList[tableIndex][colRow][2] == 1 and
                      bingoResultList[tableIndex][colRow][3] == 1 and
                      bingoResultList[tableIndex][colRow][4] == 1 ) 
                    or
                    ( bingoResultList[tableIndex][0][colRow] == 1 and 
                      bingoResultList[tableIndex][1][colRow] == 1 and 
                      bingoResultList[tableIndex][2][colRow] == 1 and
                      bingoResultList[tableIndex][3][colRow] == 1 and
                      bingoResultList[tableIndex][4][colRow] == 1 ) ):
                    print("There is a winner table! The table number is: {}".format(tableIndex)) 
                    print("(The total number of boards is: {})".format(len(bingoBoardList)))
                    print("The bingo result table looks like this:")
                    print(bingoResultList[tableIndex])

                    
                    print("The winner number that was just called is: {}".format(number))
                    print("Adding up the sum of unmarked numbers...")
                    #iterate through the winner table
                    sum = 0
                    for rowIndex, row in enumerate(table):
                        for columnIndex, column in enumerate(row):
                            if bingoResultList[tableIndex][rowIndex][columnIndex] == 0:
                                sum += bingoBoardList[tableIndex][rowIndex][columnIndex]
                    print("The sum is: {}".format(sum))
                    result = int(number)*sum
                    print("The result of the task is: {}".format(result))
                    return
               
    print("The list of results is:\n ",bingoResultList)
if __name__ == "__main__":
    main()
