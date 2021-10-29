
# Take photos from dslr (jpeg fine + raw) and create (jpeg fine + raw + jpeg low)
# File must be named with .JPG extension to be downsized. Will not run a second time on files named _LOW.JPG
# Call using cmd from working directory 'dslrPhotoDownsizer.py -dir C:\...\...\ -red "[10-90]"'

from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser(description='Create low resolution jpeg')

parser.add_argument("-dir", "--directory", help="Specifies the directory containing the photo files", default='.')
parser.add_argument("-red", "--reduction", help="How much to reduce the file (percent).", default='50')
args = parser.parse_args()

workingDir = args.directory if args.directory[-1:]=="\\" else args.directory+"\\"
reductionAmt = 1-((int(args.reduction) if int(args.reduction)>10 and int(args.reduction)<90 else 50)*0.01)

for fileName in os.listdir(workingDir):
    try:
        if fileName[-4:]==".JPG" and fileName[-8:]!="_LOW.JPG":
            fullLocation = workingDir+fileName
            oldImg = Image.open(fullLocation)
            newImg = oldImg.resize((int(oldImg.size[0]*reductionAmt), int(oldImg.size[1]*reductionAmt)), Image.ANTIALIAS)
            newImg.save(fullLocation.replace(".JPG","_LOW.JPG"), optimize=True, quality=95)
            print(str(fullLocation.replace(".JPG","_LOW.JPG")))
    except:
        pass