#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



fig=plt.figure()                                                                                                                              


ax1 = fig.add_subplot(2,2,1)                                                                                                                  

ax2 = fig.add_subplot(2,2,2)                                                                                                                  

ax3 = fig.add_subplot(2,2,3)                                                                                                                  

plt.plot(np.random.randn(50).cumsum(), 'k--')                                                                                                 

_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)                                                                            

ax2.scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))                                                                              

plt.show()                                                                   
