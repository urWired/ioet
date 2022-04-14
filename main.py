#! /usr/bin/env python

import sys
from processingData import *
from scheduleMatrix import *
from coincidences import *

def main():

    if len(sys.argv) < 2:

        print('Usage: python main.py [file path]')
        sys.exit()

    # Obtain file
    txtFile = sys.argv[1]

    # Generate list of strings
    listData = readData(txtFile)

    # Generate dictionary with data
    dataDict = dataToDict(listData)

    # Generate matrix data structure
    grid = scheduleMatrix(dataDict)

    # Create coincidences based on grid structure
    # Creates an Object coincidence that stores a dictionary with results
    coincidences = coincidence(grid)

    # Print results
    coincidences.getCoincidences()


if '__main__' == __name__:
    main()
