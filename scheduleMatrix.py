
# Data structure to store parsed file in a table format
class scheduleMatrix:

    def __init__(self, dataDict: dict):

        self.__cols = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
        self.__rows = list(dataDict)
        self.__data = dataDict
        self.__grid = self.__fillGrid()

# Returns vector of names
    def getNames(self):
        return self.__rows

# Returns vector of days
    def getDays(self):
        return self.__cols

# Fills matrix with tuples contained in dictionary.
# If a employee doesn't have records for a given day, it is set to (0,0)
    def __fillGrid(self,fill = 0):
        zeroGrid = [[fill for col in self.__cols] for row in self.__rows]
        for idxR,emp in enumerate(self.__rows):
            for idxC,day in enumerate(self.__cols):
               if self.__contains(emp,day):
                   zeroGrid[idxR][idxC] = self.__data[emp][day]
               else:
                   zeroGrid[idxR][idxC] = (0,0)
        return zeroGrid

# Validates if employee worked the given day
    def __contains(self,employee: str, day: str) -> bool:
        if self.__data[employee].get(day):
            return True
        else:
            return False

# Returns a vector of hours corresponding to a given day for every employee
    def obtainColumnByDay(self, day: str):
        colIdx = self.__cols.index(day)
        hours = []
        for idx,row in enumerate(self.__grid):
            hours.append(self.__grid[idx][colIdx])
        return hours

    def __printGrid(self):
        for row in self.__grid:
            print(row)
            print('\n')

    def printGrid(self):
        self.__printGrid()
