# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 01:56:59 2022

@author: xq127
"""

import numpy as np
import matplotlib.pyplot as plt

im = np.arange(256)

im = im[np.newaxis, :]

im = np.repeat(im, 150, axis=0)

# print(im.shape)

plt.imshow(im, cmap='gray')


plt.show()