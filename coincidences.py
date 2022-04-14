from scheduleMatrix import *

class coincidence:

    def __init__(self, grid: scheduleMatrix):

        self.__schedules = grid
        self.__coincidences = self.obtainCoincidences()

# This method validates if there is a coincidence in the schedule between
# two employees taking in account their entrance or departure of the office
    def validateHours(self, listOfNames: list, hours: list, ent: int, dep: int, name: str, idx: int, tup: tuple, data: dict):
        if ent == hours[idx][0] and tup != (0,0):
            if f'{name} - {listOfNames[idx]}' not in data:
                data[f'{name} - {listOfNames[idx]}'] = 1
            else:
                data[f'{name} - {listOfNames[idx]}'] += 1
        elif ent != hours[idx][0] and tup != (0,0):
            if ent > hours[idx][0]:
                if (hours[idx][1] >= ent or hours[idx][1] >= dep) and f'{name} - {listOfNames[idx]}' not in data :
                    data[f'{name} - {listOfNames[idx]}'] = 1
                else:
                    data[f'{name} - {listOfNames[idx]}'] += 1
        return

# This method generates a dictionary with all coincidences and the recurrence for each one
    def obtainCoincidences(self):
        data = {}
        names = self.__schedules.getNames()
        for day in self.__schedules.getDays():
            listOfNames = names.copy()
            hours = self.__schedules.obtainColumnByDay(day)
            ent, dep = hours.pop(0)
            name = listOfNames.pop(0)
            while len(hours) > 0:
                for idx,tup in enumerate(hours):
                    self.validateHours(listOfNames,hours,ent,dep,name,idx,tup,data)
                ent, dep = hours.pop(0)
                name = listOfNames.pop(0)
            listOfNames = names.copy()
        return data

# Returns the data allocated in the attribute __coincidences
    def getCoincidences(self):
        data = self.__coincidences
        print('  Names         Recurrences')
        print('|--------------------------|')
        for k,v in data.items():
            print(f' {k}:    {v} \n')
