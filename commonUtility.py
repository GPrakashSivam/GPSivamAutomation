import os
import json
from datetime import datetime, timedelta

def getPrevBusinessDate():
    date = datetime.today()
    # Logical equation to find time elapsed for previous business day
    offset = max(1, (date.weekday() + 6) % 7 - 3)
    date = date - timedelta(offset)
    return date.strftime("%d%m%Y")

with open(os.path.join(os.getcwd(),'CamarillaConfig.json'), "r") as readfile: 
    data = json.load(readfile)

webURL = data["URL"]
googleSheetURL = data["GoogleSheetURL"]
googleSheetName = data["GoogleSheetName"]
senderEmailAddress = data["SenderEmailAddress"]
recipientEmailAddress = data["RecipientEmailAddress"]
exportPDFFileName = data["ExportPDFFileName"] + "_" + datetime.today().strftime("%d%m%Y") + '.pdf'
sendGrid_API_KEY = data["SENDGRID_API_KEY"]

filepath = data["Filepath"]
fileExtn = data["FileExtn"]
isAutoDate = data["IsAutoDate"]
if(isAutoDate == "True"):
    filename = data["FileName"] + "_" + getPrevBusinessDate() + fileExtn
else:
    filename = data["FileName"] + fileExtn
filenameFullPath = os.path.join(filepath,filename)
targetFile = os.path.join(os.getcwd(),filename)

isFileDownloaded = os.path.exists(filenameFullPath)
isTargetFileExists = os.path.exists(targetFile)

OutputXLFilename = data["OutputXLFilename"]
symbols = data["Symbols"]

