import os

def creatFiles(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def moveFiles(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


files = os.listdir()

creatFiles("Images")
creatFiles("Pdf files")
creatFiles("Media")
creatFiles("Others")

imgExt = [".jpg", ".png",".eps",".gif" ]
image = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]

docExt = [".DOC", ".HTML",".png",".PDF",".ODS",".PPT",".PPTX",".TXT", ".csv" ]
document = [file for file in files if os.path.splitext(file)[1].lower() in docExt]

mediaExt = [".mp3" ,".mp4", ".flv"]
media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]

others = []

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if(ext not in imgExt) and (ext not in docExt) and (ext not in mediaExt) and os.path.isfile(file):
        others.append(file)


moveFiles("Images", image)
moveFiles("Pdf files", document)
moveFiles("Media", media)
moveFiles("Others", others)