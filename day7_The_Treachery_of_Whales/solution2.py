#!/usr/bin/python

import os, sys, copy

def factorialSum(number):
    sum = 0
    for index in range(number+1):
       sum += index 
       #print("current index is:", index)
    #print("Returning factorialsum:", sum)
    return sum

def main():
    log = False
    print("The received argument: {}".format(sys.argv[1]))
    #read in the data
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    crabPositions = []
    #read the lines into a list
    crabPositions.append(lines[0].split(","))
    crabPositions = crabPositions[0]
    for index, crabPosition in enumerate(crabPositions):
        crabPositions[index] = int(crabPosition)
    crabPositions.sort()
    print(crabPositions)

    #calculate the fuel consumption
    minFuelConsumptionSoFar = 10000000000000000000000000000000
    for position in range(1900):
        fuelConsumption = 0
        print("The currently inspected position is: ", position)
        for index, crabPosition in enumerate(crabPositions):
            calculatedFuel = factorialSum(abs(position-crabPosition))
            fuelConsumption += abs(calculatedFuel) 
        if fuelConsumption < minFuelConsumptionSoFar: minFuelConsumptionSoFar = fuelConsumption
        print("The minFuelConsumption is:", minFuelConsumptionSoFar)
        
if __name__ == "__main__":
    main()