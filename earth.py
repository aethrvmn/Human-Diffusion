from PIL import Image
from tqdm import tqdm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Earth:

    def __init__(self):
        pass

    def black_and_white(self, filename, outputname, imgname, threshold = 5):

        self.img = Image.open(filename)
        self.arr = np.array(self.img.getdata())
        self.newPixels = []

        threshold = 15

        for pixel in tqdm(self.arr):
            # if it looks like black, convert it to black
            if pixel[0] <= threshold:
                newPixel = (0, 0, 0)
            # if it looks like white, convert it to white
            else:
                newPixel = (255, 255, 255)
            self.newPixels.append(newPixel)

        pd.DataFrame(self.newPixels).to_csv(outputname, index = None, header = ['R', 'G', 'B'])

        newImg = Image.new(self.img.mode, self.img.size)
        newImg.putdata(self.newPixels)
        newImg.save(imgname)

        return self

    def generate_image(self, filename, threshold = 200, value = 1):

        img_array=plt.imread(filename)

        self.height = img_array.shape[0]
        self.width = img_array.shape[1]

        self.map = np.zeros(shape = (self.height, self.width))

        for i in tqdm(np.arange(len(img_array))):
            for j in np.arange(len(img_array[0])):
                if img_array[i][j][0] > 200:
                    self.map[i][j] = 1

        return self

    def plot(self, imgname, clrtmplt = 'ocean', xsize = 20, ysize = 20):
        plt.figure(figsize=(xsize, ysize))
        plt.imshow(self.map, cmap = clrtmplt)
        plt.ylabel('Latitude')
        plt.xlabel('Longtitude')
        plt.xticks([])
        plt.yticks([])
        plt.savefig(f"Images/{imgname}")
        plt.show()
