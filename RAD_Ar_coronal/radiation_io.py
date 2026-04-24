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
    tiny = np.finfo(np.float64).tiny

    def __init__(self, dir_data='.'):
        self.dir_data = dir_data

    def log10_with_floor(self, x):
        """Return log10(x), floored to the smallest representable float to avoid -inf."""
        return np.log10(np.maximum(x, self.tiny))

    def read(self, impurity_name):
        ncfile = os.path.join(self.dir_data, f'{impurity_name}.nc')
        data = netCDF4.Dataset(ncfile, 'r', format='NETCDF4')

        data_Lz = data.variables['coronal_Lz'][:, :]
        #dim_ne_tau = data.variables['dim_ne_tau'][:]
        dim_ne = data.variables['dim_electron_density'][:]
        dim_te = data.variables['dim_electron_temp'][:]

        self.coeff_is_zero = np.all(data_Lz == 0.0)

        # Interpolate in log-space: take log10 of axes and values
        self.Lz = RegularGridInterpolator(
            (
                self.log10_with_floor(dim_te),
                self.log10_with_floor(dim_ne),
                #self.log10_with_floor(dim_ne_tau),
            ),
            self.log10_with_floor(data_Lz),
            bounds_error=True,
        )

    def __call__(self, te, ne, ne_tau=0.5e17, allow_extrap=False):
        # Query point in log-space
        log_point = (
            self.log10_with_floor(te),
            self.log10_with_floor(ne),
            #self.log10_with_floor(ne_tau),
        )

        if allow_extrap:
            result = self.Lz(log_point, method='linear')
        else:
            result = self.Lz(log_point)  # bounds_error=True by default

        # Exponentiate back to linear space, unless all coefficients were zero
        if self.coeff_is_zero:
            return result
        else:
            return np.power(10, result)
