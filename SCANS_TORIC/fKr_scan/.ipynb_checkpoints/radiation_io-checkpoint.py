"""
 -----------------------------------------------------------------------
 utils for genray IO
 -----------------------------------------------------------------------
"""
import os
import numpy as np
from scipy.interpolate import RegularGridInterpolator
import netCDF4


class radiation_io():
    def __init__(self, dir_data='.'):
        self.dir_data = dir_data
        pass
    
    def read(self, impurity_name):
        #-- read genray output
        ncfile = os.path.join(self.dir_data, f'{impurity_name}.nc')
        data = netCDF4.Dataset(ncfile, 'r', format='NETCDF4')
        data_Lz = data.variables['coronal_Lz'][:, :, :]
        dim_ne_tau = data.variables['dim_ne_tau'][:]
        dim_ne = data.variables['dim_electron_density'][:]
        dim_te = data.variables['dim_electron_temp'][:]
        print(dim_ne_tau)
        print(dim_ne[0], dim_ne[-1])
        print(dim_te[0], dim_te[-1])

        self.ne_bound = 1.01 * dim_ne[0], 0.99 * dim_ne[-1]
        self.te_bound = 1.01 * dim_te[0], 0.99 * dim_te[-1]
        self.Lz = RegularGridInterpolator((np.log10(dim_te), np.log10(dim_ne), np.log10(dim_ne_tau)), np.log10(data_Lz))
        self.Lz = 10**self.Lz
    
    def __call__(self, te, ne, nte_tau=0.5e17):
        _te =  np.where(te >= self.te_bound[1], self.te_bound[1], te)
        _te =  np.where(te <= self.te_bound[0], self.te_bound[0], _te)
        _ne =  np.where(ne >= self.ne_bound[1], self.ne_bound[1], ne)
        _ne =  np.where(ne <= self.ne_bound[0], self.ne_bound[0], _ne)
        # print(_te)
        # print(_ne)
        return self.Lz((_te, _ne, nte_tau))
