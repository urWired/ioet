# File containing all functions used to read and parse input text file
# Read data and returns a list of strings
def readData(txtFile):

    with open(txtFile, 'r', encoding = 'utf-8') as txt:
        return [linea.strip() for linea in txt]


def dataToDict(listOfStr: list) -> dict:

    data = {}
    for line in listOfStr:
        name = line.split('=')[0]
        listOfDays = line.split('=')[1].split(',')

        if len(listOfDays) > 1:
            for d in listOfDays:
                day = d[0:2]
                time = d[2:]
                tupleTime = strToTime(time)

                if name not in data:
                    data[name] = {day:tupleTime}
                else:
                    data[name][day] = tupleTime
        else:
            day = listOfDays[0:2]
            time = listOfDays[2:]

            if name not in data:
                data[name] = {day:tupleTime}
            else:
                data[name][day] = tupleTime
    return data


def strToTime(time: str) -> tuple:

    entranceTime,departureTime = time.split('-')
    entranceTime = int(entranceTime.split(':')[0])
    departureTime = int(departureTime.split(':')[0])
    return (entranceTime,departureTime)
