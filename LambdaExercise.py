import csv
from functools import reduce
import statistics

filename = r'C:\Users\nickk\Downloads\DetroitCallsForService.csv'
with open(filename, 'r') as csv_file:
    
    fullDict = [{k:v for k, v in row.items()} for row in csv.DictReader(csv_file, skipinitialspace=True)]
print(len(fullDict))
cleanList = list(filter(lambda oneDict: False if(oneDict['zip_code'] == '0' or oneDict['neighborhood'] == '') else True, fullDict))

for i in range(0,len(cleanList)):
    if(cleanList[i]['dispatchtime'] == ''):
        cleanList[i]['dispatchtime'] = 0
    else:
        cleanList[i]['dispatchtime'] = float(cleanList[i]['dispatchtime'])
    if(cleanList[i]['totalresponsetime'] == ''):
        cleanList[i]['totalresponsetime'] = 0
    else:
        cleanList[i]['totalresponsetime'] = float(cleanList[i]['totalresponsetime'])
    if(cleanList[i]['totaltime'] == ''):
        cleanList[i]['totaltime'] = 0
    else:
        cleanList[i]['totaltime'] = float(cleanList[i]['totaltime'])

dispatchtimeList = list(map(lambda x: x['dispatchtime'], cleanList))
responsetimeList = list(map(lambda x: x['totalresponsetime'], cleanList))
totaltimeList = list(map(lambda x: x['totaltime'], cleanList))

print(f"{round(statistics.mean(dispatchtimeList),2)} is the average dispatch time.")
print(f"{round(statistics.mean(responsetimeList),2)} is the average response time.")
print(f"{round(statistics.mean(totaltimeList),2)} is the average total time.")

dispatchtimeTot = reduce(lambda num1, num2: num1+num2, dispatchtimeList, 0)
avgDispatchTime = dispatchtimeTot/len(dispatchtimeList)
print(avgDispatchTime)

responsetimeTot = reduce(lambda num1, num2: num1+num2, responsetimeList, 0)
avgresponseTime = responsetimeTot/len(responsetimeList)
print(avgresponseTime)

totaltimeTot = reduce(lambda num1, num2: num1+num2, totaltimeList, 0)
avgtotalTime = totaltimeTot/len(totaltimeList)
print(avgtotalTime)