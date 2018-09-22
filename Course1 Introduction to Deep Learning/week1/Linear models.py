# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 14:50:55 2018

@author: Administrator
"""

#1
import numpy as np
a = np.array([1, -2, 0.5])
b = np.exp(a)
softmax = b/np.sum(b)