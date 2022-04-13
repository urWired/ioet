class scheduleMatrix:

    def __init__(self, dataDict: dict):

        self.__cols = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
        self.__rows = list(dataDict)
        self.__data = dataDict
        self.__grid = self.__fillGrid()

    def getNames(self):
        return self.__rows

    def getDays(self):
        return self.__cols

    def __fillGrid(self,fill = 0):

        zeroGrid = [[fill for col in self.__cols] for row in self.__rows]

        for idxR,emp in enumerate(self.__rows):
            for idxC,day in enumerate(self.__cols):
               if self.__contains(emp,day):
                   zeroGrid[idxR][idxC] = self.__data[emp][day]
               else:
                   zeroGrid[idxR][idxC] = (0,0)
        return zeroGrid


    def __printGrid(self):

        for row in self.__grid:
            print(row)
            print('\n')

    def printGrid(self):

        self.__printGrid()


    def __contains(self,employee: str, day: str) -> bool:

        if self.__data[employee].get(day):
            return True
        else:
            return False

    def obtainColumnByDay(self, day: str):

        colIdx = self.__cols.index(day)
        hours = []
        for idx,row in enumerate(self.__grid):
            hours.append(self.__grid[idx][colIdx])
        return hours
