import matplotlib
import matplotlib.pyplot as plt

from skimage import color
from skimage import io
from skimage.filters import threshold_mean

class Maze:
    class Node:
        def __init__(self, position):
            self.Position = position
            self.Neighbours = [None, None, None, None]

    def __init__(self, im, start, finish):
        self.image = color.rgb2gray(io.imread(im))
        thresh = threshold_mean(self.image)
        self.binary = self.image > thresh
        self.start = start
        self.finish = finish

        fig, axes = plt.subplots(ncols=2, figsize=(8, 3))
        ax = axes.ravel()

        ax[0].imshow(image, cmap=plt.cm.gray)
        ax[0].set_title('Original image')

        ax[1].imshow(binary, cmap=plt.cm.gray)
        ax[1].set_title('Result')
        plt.show()

if __name__ == '__main__':
    Maze = Maze('maze3.jpg')
