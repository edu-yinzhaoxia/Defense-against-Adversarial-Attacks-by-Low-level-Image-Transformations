#### Flip images
import os, sys
from PIL import Image

def flipImages(pathOfPictures):
	for filename in os.listdir(pathOfPictures):
		oldName = os.path.splitext(filename)
		originalImage = Image.open(pathOfPictures + "/" + filename)
		flippedImage = originalImage.transpose(Image.FLIP_LEFT_RIGHT)
		saveFlippedImage = flippedImage.save(pathOfPictures + "/" + oldName[0] + "_f" + oldName[1])  # Save the flipped images

flipImages(sys.argv[1]) # The path of the folder where the image needs to be flipped