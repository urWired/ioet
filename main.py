#! /usr/bin/env python3
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

    listData = readData(txtFile)
   # print(listData)

    dataDict = dataToDict(listData)

    grid = scheduleMatrix(dataDict)
    coin = coincidences(grid)

    print(coin.obtainRelations())
    #print(coin.getRelations())



if '__main__' == __name__:
    main()
