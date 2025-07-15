import numpy as np
import matplotlib.pyplot as plt
from scipy.special import exp1 as W
plt.plot()
s =int(1,3,7,9,15,24,30,15,8,4,0)
plt.plot(times, s)
plt.ylabel('Drawdown, in meters')
plt.xlabel('Time, in days')
plt.show()
