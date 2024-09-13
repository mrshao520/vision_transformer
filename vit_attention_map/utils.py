import torch
from torch import nn, optim
import torch.nn.functional as F

import torchvision
from torchvision.transforms import Compose, Resize, CenterCrop, Normalize, ToTensor

from timm.models import create_model

import PIL
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests

from tqdm.auto import tqdm
import os
import warnings
warnings.filterwarnings("ignore")
print("Libraries Imported Successfully")


############################## image display functions ##############################
def show_img(img, cmap=None):
    img = np.asarray(img)
    plt.figure(figsize=(10, 10))
    plt.imshow(img, cmap = cmap)
    plt.axis('off')
    plt.show()
    
def show_img2(img1, img2, alpha=0.8, cmap=None):
    img1 = np.asarray(img1)
    img2 = np.asarray(img2)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(img1, cmap=cmap)
    plt.imshow(img2, alpha=alpha, cmap=cmap)
    plt.axis('off')
    plt.show()
    

############################## plotting Functions ##############################