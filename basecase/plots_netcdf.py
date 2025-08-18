from netCDF4 import Dataset
from sys import argv
import matplotlib.pyplot as plt

ffile = argv[1]
rootgrp = Dataset(ffile)

rho = rootgrp['rho'][:]

ne = rootgrp['ne'][-1,:]
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
ip = rootgrp['ip'][-1]

pfuse = rootgrp['pe_fus'][-1,:]
pfuse_int = rootgrp['pfuse'][-1]
pfusi = rootgrp['pi_fus'][-1,:]
pfusi_int = rootgrp['pfusi'][-1]

q = rootgrp['q'][-1,:]

jbs = rootgrp['j_bs'][-1,:]
ibs = rootgrp['ibs'][-1]
jrf = rootgrp['j_rf'][-1,:]
irf = rootgrp['irf'][-1]
jtot = rootgrp['j_tot'][-1,:]

fluxe = rootgrp['fluxe'][-1,:]
fluxe_exp = rootgrp['fluxe_exp'][-1,:]
fluxi = rootgrp['fluxi'][-1,:]
fluxi_exp = rootgrp['fluxi_exp'][-1,:]

fig, ((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9)) =plt.subplots(3,3,figsize =(8,6),dpi = 150)
lw = 2
c1 = 'green'
c2 = 'lime'
c3 = 'magenta'
c4 = 'darkviolet'
c5 = 'dodgerblue'
c6 = 'cyan'

ax1.plot(rho,ne,color = c1,linewidth = lw,label='electron')
ax1.plot(rho,ni,color = c2,linewidth = lw,linestyle = 'dashed',label='ion')
ax2.plot(rho,te,color = c1,linewidth = lw)
ax2.plot(rho,ti,color = c2,linewidth = lw,linestyle = 'dashed')
ax1.set_ylabel('dens [10$^{19}$/m$^3$]')
ax2.set_ylabel('temp [keV]')
ax1.legend()

ax3.plot(rho,prfe,color = c1,linewidth = lw)
ax3.plot(rho,prfi,color = c2,linewidth = lw,linestyle = 'dashed')
ax4.plot(rho,betan,color = c3,linewidth = lw)
ax3.set_ylabel('qaux [MW/m$^3$]')
ax3.text(0.5,0.8,'{:.1f} MW'.format(prfe_int),color = c1, transform = ax3.transAxes)
ax3.text(0.5,0.6,'{:.1f} MW'.format(prfi_int),color = c2, transform = ax3.transAxes)
ax4.set_ylabel('betan')
ax4.text(0.5,0.8,'betan = {:.1f}'.format(betan_num),color = c3, transform = ax4.transAxes)

ax5.plot(rho,q,color = c3,linewidth = lw)
ax5.set_ylabel('q')

ax6.plot(rho,ipol,color = c3, linewidth = lw)
ax6.set_ylabel('ipol')
ax6.text(0.5,0.8,'{:.1f} MA'.format(ip),color = c3,transform = ax6.transAxes)

#ax7.plot(rho,jtot,color = c3,linewidth = lw)
ax7.plot(rho,jrf,color = c4,linewidth = lw,linestyle = 'dashed')
ax7.plot(rho,jbs,color = c5, linewidth =lw, linestyle='dashed')
ax7.text(0.5,0.8,'i_rf = {:.1f}'.format(irf),color = c4,transform = ax7.transAxes)
ax7.text(0.5,0.6,'i_bs = {:.1f}'.format(ibs),color = c5,transform = ax7.transAxes)
ax7.set_ylabel('current density')

ax8.plot(rho,pfuse,color = c1,linewidth = lw)
ax8.plot(rho,pfusi,color = c2,linewidth = lw,linestyle = 'dashed')
ax8.set_ylabel('pfus')
ax8.text(0.5,0.8,'{:.1f} MW'.format(pfuse_int),color = c1,transform = ax8.transAxes)
ax8.text(0.5,0.6,'{:.1f} MW'.format(pfusi_int),color = c2,transform = ax8.transAxes)

ax9.plot(rho,fluxe,'.',color =c1,linewidth = lw)
ax9.plot(rho,fluxe_exp,color = c1,linewidth = lw,linestyle = 'dashed')
ax9.plot(rho,fluxi,'.',color = c2,linewidth = lw)
ax9.plot(rho,fluxi_exp,color = c2,linewidth = lw,linestyle = 'dashed')
ax9.set_ylabel('flux [W/m$^3$]')

fig.tight_layout()
plt.show()
