from scheduleMatrix import *

class coincidences:

    def __init__(self, grid: scheduleMatrix):

        self.__schedules = grid
        self.__relations = self.obtainRelations()


    def obtainRelations(self):

        data = {}
        names = self.__schedules.getNames()
        for day in self.__schedules.getDays():
            listOfNames = names.copy()
            hours = self.__schedules.obtainColumnByDay(day)
            ent, dep = hours.pop(0)
            name = listOfNames.pop(0)
            while len(hours) > 0:
                for idx,tup in enumerate(hours):
                    if ent == hours[idx][0] and tup != (0,0):
                        if f'{name} - {listOfNames[idx]}' not in data:
                            data[f'{name} - {listOfNames[idx]}'] = 1
                        else:
                            data[f'{name} - {listOfNames[idx]}'] += 1
                    if ent != hours[idx][0] and tup != (0,0):
                        if ent > hours[idx][0]:
                            if hours[idx][1] >= ent and f'{name} - {listOfNames[idx]}' not in data :
                                data[f'{name} - {listOfNames[idx]}'] = 1
                            else:
                                data[f'{name} - {listOfNames[idx]}'] += 1

                ent, dep = hours.pop(0)
                name = listOfNames.pop(0)
            listOfNames = names.copy()
        return data


    def getRelations(self):
        return self.__relations
