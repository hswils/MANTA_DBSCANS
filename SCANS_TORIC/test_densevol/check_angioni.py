from uncertainties import ufloat
from netCDF4 import Dataset
from sys import argv
import matplotlib.pyplot as plt

ffile = '/pscratch/sd/h/hswils/github_repos/MANTA_DBSCANS/basecase/SCAN/work/fastran_tr_fastran_7/fastran.nc'
rootgrp = Dataset(ffile)

nebar = rootgrp['nebar'][-1]
ni = rootgrp['ni'][-1,:]

te = rootgrp['te'][-1,:]
teavg = rootgrp['tea'][-1]
ti = rootgrp['ti'][-1,:]
tiavg = rootgrp['tia'][-1]

prfe = rootgrp['pe_rf'][-1,:]
prfe_int = rootgrp['prfe'][-1]
prfi = rootgrp['pi_rf'][-1,:]
prfi_int = rootgrp['prfi'][-1]

betan = rootgrp['betan_loc'][-1,:]
betan_num = rootgrp['betan'][-1]

ipol = rootgrp['ipol'][-1,:]

pfuse = rootgrp['pe_fus'][-1,:]


Rmaj = rootgrp['r0'][-1] 
Bt = rootgrp['b0'][-1]
Ip = rootgrp['ip'][-1]
aminor = rootgrp['a0'][-1]
Gamma_NBI = 0
n_Gr = Ip/(pi*aminor**2)

#Grab profiles
rho_tor_norm = rootgrp['rho'][:]
ne_prof = rootgrp['ne'][-1,:] #10^19/m^3
Te_prof = rootgrp['te'][-1,:] #keV
ni_prof_tot = rootgrp['ni'][-1,:] + rootgrp['nz0'][-1,:]
Ti_prof = rootgrp['ti'][-1,:]
p_prof = (ne_prof*Te_prof+ni_prof_tot*Ti_prof)/1602.2 # kev*10**19 (division is for from eV to Joules)

#Calculate volume integrals
#p_vol_int = volume_integral(geqdsk,rho_tor_norm,p_prof)
#vol = volume_integral(geqdsk,rho_tor_norm,np.ones(len(rho_tor_norm)))

#Calculate volume averages
ne_lin_avg = nebar
#p_vol_avg = p_vol_int/vol
Te_vol_avg = teavg

f_Gr = ne_lin_avg/n_Gr

#Calculate regression variables
nu_eff = 0.2*ne_lin_avg*Rmaj/(Te_vol_avg**2)
#beta = 4.02e-3*p_vol_avg/(Bt**2)
beta = rootgrp['betan'][-1]
#print(nu_eff)
#print(beta)

n02 = ne_prof[int(0.2*len(ne_prof))]

#Calculate Angioni peaking
npeaking = ufloat(1.347,0.014) - ufloat(0.117,0.005)*numpy.log(nu_eff) + ufloat(1.331,0.117)*Gamma_NBI - ufloat(4.030,0.810)*beta

n_peak_left = npeaking.nominal_value-npeaking.std_dev
n_peak_right = npeaking.nominal_value+npeaking.std_dev
if n02/ne_vol_avg >= n_peak_left and n02/ne_vol_avg <= n_peak_right:
    print('pass')
else:
    print('fail')
print(npeaking)
print(n02/ne_vol_avg)

