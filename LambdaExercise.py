import csv

def hasZipCode(fullDict):
    for i in range(0,len(fullDict)):
        if fullDict[i]['zip_code'] == 0:
            return False
        else: return True

filename = r'C:\Users\nickk\Downloads\DetroitCallsForService.csv'
with open(filename, 'r') as csv_file:
    
    fullDict = [{k:v for k, v in row.items()} for row in csv.DictReader(csv_file, skipinitialspace=True)]
print(len(fullDict))
noZip = list(filter(lambda x:x['zip_code']!='0', fullDict))
noZipNoNeighborhood = list(filter(lambda x:x['neighborhood']!='',noZip))
print(len(noZipNoNeighborhood))

