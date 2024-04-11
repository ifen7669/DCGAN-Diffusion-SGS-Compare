from PIL import Image
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def calculations(image_folder, resolution):
    
    results = np.empty((len(os.listdir(image_folder)), resolution, resolution))
    
    for i, name in enumerate(os.listdir(image_folder)):
        path = os.path.join(image_folder, name)
        image = Image.open(path).convert('L')
        image_normalized = np.array(image, dtype=np.float32) / 255.0
        
        
        results[i] = image_normalized

    return results

def plot_colormap(X, Y, Color, colorbar_title, title):

    fig = plt.figure(figsize = (6,5))
    ax = plt.gca()
    im = ax.scatter(X, Y, c=Color, marker='.', s=5, cmap='gist_earth')
    plt.title(title)
    plt.xlabel('X [m]'); plt.ylabel('Y [m]')
    plt.locator_params(nbins=5)
    plt.axis('scaled')

    # make colorbar
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.1)
    cbar = plt.colorbar(im, ticks=np.linspace(np.min(Color), np.max(Color), 11), cax=cax)
    cbar.set_label(colorbar_title, rotation=270, labelpad=15)
   