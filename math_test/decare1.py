# -*- coding: UTF-8 -*-

import sys
import os

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

T = np.linspace(0 , 2 * np.pi, 1024)
plt.axes(polar = True)
plt.plot(T, 1. - np.sin(T),color="r")
plt.show()
