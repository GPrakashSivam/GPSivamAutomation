import os
import json
from datetime import datetime, timedelta

with open(os.path.join(os.getcwd(),'CamarillaConfig.json'), "r") as readfile: 
    data = json.load(readfile)

webURL = data["URL"]
googleSheetURL = data["GoogleSheetURL"]
googleSheetName = data["GoogleSheetName"]
exportPDFFileName = data["ExportPDFFileName"] + "_" + datetime.today().strftime("%d%m%Y") + '.pdf'
outputXLFilename = data["OutputXLFilename"]
symbols = data["Symbols"]
