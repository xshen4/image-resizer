import PIL
from PIL import Image
import glob2

def getMinImageSize(inputDir):
    # todo but this in global var
    IMAGE_NAMES = glob2.glob(inputDir + '/*')
    minSize = None
    for imageName in IMAGE_NAMES:
        img = Image.open(imageName)
        width, height = img.size
        currSize = height if width > height else width
        if minSize == None:
            minSize = currSize
        minSize = currSize if currSize < minSize else minSize
    return minSize

def resizePhotos(size, inputDir, outputDir):
    IMAGE_NAMES = glob2.glob(inputDir + '/*')
    minSize = None
    # set up size to size + 100 ish ; redo this part
    THUMBSIZE= size+100, size+100
    idx = 1
    for imageName in IMAGE_NAMES:
        img = Image.open(imageName)
        img.thumbnail(THUMBSIZE, Image.ANTIALIAS)
        img.save(outputDir + str(idx) + '.jpg', quality=95)
        idx = idx+1

def cropPhotos(size, inputDir, outputDir):
    IMAGE_NAMES = glob2.glob(inputDir + '/*')
    cropSize= (size-100) / 2
    idx = 1
    for imageName in IMAGE_NAMES:
        img = Image.open(imageName)

        half_the_width = img.size[0] / 2
        half_the_height = img.size[1] / 2
        img2 = img.crop(
            (
                half_the_width - cropSize,
                half_the_height - cropSize,
                half_the_width + cropSize,
                half_the_height + cropSize
            )
        )
        img2.save(outputDir + str(idx) + '.jpg', quality=95)
        idx = idx+1

# get from input params
INPUT_DIR = '/Users/xiuli.j.shen/development/wogrammer-photos-test'
RESIZED_DIR = '/Users/xiuli.j.shen/development/wogrammer-photos-resized/'
CROPPED_DIR = '/Users/xiuli.j.shen/development/wogrammer-photos-cropped/'
size = getMinImageSize(INPUT_DIR)
print size
resizePhotos(size, INPUT_DIR, RESIZED_DIR)
cropPhotos(size, RESIZED_DIR, CROPPED_DIR)

# loop through all pix and get minimum size (both either height or width)
# resize based on min size + 100px if > min size + 100px
# otherwise, crop in middle for each
# save to another folder

# get min size with directory as param
# dir: string
#def getMinSize(dir):
#    for
