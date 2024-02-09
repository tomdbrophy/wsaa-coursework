# Program that prints the data for all trains in Ireland to the console.

import requests
import csv
from xml.dom.minidom import parseString

url = 'https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML'
page = requests.get(url)
doc = parseString(page.content)

#print(doc.toprettyxml())

#with open('trainxml.xml','w') as xmlfp:
#    doc.writexml(xmlfp)

retrieveTags = ['TrainStatus',
                'TrainLatitude',
                'TrainLongitude',
                'TrainCode',
                'TrainDate',
                'PublicMessage',
                'Direction'
                ]

objTrainPositionsNodes = doc.getElementsByTagName('objTrainPositions')
'''
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName('TrainCode').item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    print(traincode)
'''
with open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for objTrainPositionsNode in objTrainPositionsNodes:
        latitudenode = objTrainPositionsNode.getElementsByTagName('TrainLatitude').item(0)
        latitude = latitudenode.firstChild.nodeValue.strip()
        dataList=[]
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)