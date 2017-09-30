import matplotlib.pyplot as plt
plt.rcdefaults()

import numpy as np
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

def example():
    fig, ax = plt.subplots()
    # create 3x3 grid to plot the artists
    grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T
    print(grid)
    patches = []

    circle = mpatches.Circle(grid[0], 0.1, ec="none")
    patches.append(circle)

    colors = np.linspace(0, 1, len(patches))
    collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
    collection.set_array(np.array(colors))
    ax.add_collection(collection)

    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    plt.axis('equal')
    plt.axis('off')

    plt.show()


def with_subplot_grid():
    fig, axes = plt.subplots(3, 3)

    for i, row in enumerate(axes):
        for j, ax in enumerate(row):
            # ax.axis('equal')
            # ax.axis('off')
            # ax.set_visible(False)
            ax.add_artist(plt.Circle((0.5, 0.5), 0.2, color='r'))

    for row in range(0, 3):
        for col in range(0, 3):
            # axes[row, col].axis('equal')
            axes[row, col].axis('off')

    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    with_subplot_grid()
    # example()