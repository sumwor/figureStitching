from config import figurePath

from PIL import Image

import numpy as np

from os import listdir
from os.path import isfile, join


class Picture(object):

    def __init__(self, path):
        self.path = path

    def getImages(self):
        # get all the images in the folder
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        files.sort()
        return files

    def alignImages(self, fig1, fig2):
        # align two Images at a time

        figure1 = Image.open(fig1)
        figure2 = Image.open(fig2)

        figData1 = np.asarray(figure1)
        figData2 = np.asarray(figure2)

        def getGrayScale(pixel):
            # convert RGB into gray scale
            (x,y,z) = np.shape(pixel)
            pxGray = np.zeros((x,y))
            for i in range(len(pixel)):
                for j in range(len(pixel[i])):
                    pxGray[i][j] = pixel[i][j][0]

            return pxGray

        figGray1 = getGrayScale(figData1)
        figGray2 = getGrayScale(figData2)


Pic= Picture(figurePath)
figures = Pic.getImages()
print figures

# to make array into image
# img = Image.fromarray(array, 'L')