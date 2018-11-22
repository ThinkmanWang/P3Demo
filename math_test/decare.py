# -*- coding: UTF-8 -*-

import sys
import os

import numpy as np
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
a = 1
t = np.linspace(0 , 2 * np.pi, 1024)
X = a*(2*np.cos(t)-np.cos(2*t))
Y = a*(2*np.sin(t)-np.sin(2*t))
plt.plot(Y, X,color='r')
plt.show()
