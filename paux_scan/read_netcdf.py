from netCDF4 import Dataset
from sys import argv
import matplotlib.pyplot as plt
ffile = argv[1]
rootgrp = Dataset(ffile)
plt.plot(rootgrp['rho'][:],rootgrp[argv[2]][-1,:])
plt.show()

