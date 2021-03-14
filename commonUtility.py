import os
import json

with open(os.path.join(os.getcwd(),'CamarillaConfig.json'), "r") as readfile: 
    data = json.load(readfile)

webURL = data["URL"]
googleSheetURL = data["GoogleSheetURL"]
googleSheetName = data["GoogleSheetName"]
outputXLFilename = data["OutputXLFilename"]
symbols = data["Symbols"]
