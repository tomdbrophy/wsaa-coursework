# Program that prints the data for all trains in Ireland to the console.

import requests
import csv
from xml.dom.minidom import parseString

url = 'https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML'
page = requests.get(url)
doc=parseString(page.content)

print(doc.toprettyxml())

#with open('trainxml.xml','w') as xmlfp:
#    doc.writexml(xmlfp)