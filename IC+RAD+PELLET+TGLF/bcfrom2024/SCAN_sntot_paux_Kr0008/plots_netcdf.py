from netCDF4 import Dataset
from sys import argv
import matplotlib.pyplot as plt

ffile = argv[1]
rootgrp = Dataset(ffile)

rho = rootgrp['rho'][:]
ne = rootgrp['ne'][-1,:]
ni = rootgrp['ni'][-1,:]
te = rootgrp['te'][-1,:]
ti = rootgrp['ti'][-1,:]

fig, ((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9)) =plt.subplots(3,3,figsize =(8,6),dpi = 150)
lw = 2
c1 = 'b'
c2 = 'deepskyblue'
c3 = 'green'
c4 = 'lime'

ax1.plot(rho,ne,color = c1,linewidth = lw)
ax1.plot(rho,ni,color = c2,linewidth = lw,linestyle = 'dashed')
ax4.plot(rho_main,ni_main,color = c1,linewidth = lw)
ax4.plot(rho_ips,ni_ips,color = c2,linewidth = lw,linestyle = 'dashed')
ax1.set_ylabel('e dens [10$^{19}$/m$^3$]')
ax4.set_ylabel('i dens [10$^{19}$/m$^3$]')

ax2.plot(rho_main,Te_main,color = c1,linewidth = lw)
ax2.plot(rho_ips,Te_ips,color = c2,linewidth = lw,linestyle = 'dashed')
ax5.plot(rho_main,Ti_main,color = c1,linewidth = lw)
ax5.plot(rho_ips,Ti_ips,color = c2,linewidth = lw,linestyle = 'dashed')
ax2.set_ylabel('e temp [keV]')
ax5.set_ylabel('i temp [keV]')

ax3.plot(rho_main,rot_main,color = c1,linewidth = lw)
ax3.plot(rho_ips,rot_ips,color = c2,linewidth = lw,linestyle = 'dashed')
ax3.set_ylabel('rot [krad/s]')

#ax6.plot(OMFIT['MANTA']['RHOVN'],betan_MANTA,color = c1,linewidth = lw)
#ax6.plot(OMFIT['withheat_eq']['RHOVN'],betan_ips,color = c2,linewidth = lw,linestyle = 'dashed')
#ax6.set_ylabel('betan')

ax6.plot(rho_main,jtot_main,color = c1,linewidth = lw)
ax6.plot(rho_ips,jtot_ips,color = c2,linewidth = lw,linestyle = 'dashed')
ax6.set_ylabel('jtot')

ax7.plot(rho_main,q_main,color = c1,linewidth = lw)
ax7.plot(rho_ips,q_ips,color = c2,linewidth = lw,linestyle = 'dashed')
ax7.set_ylabel('q')

ax8.plot(rho_main,jbs_main,color = c1,linewidth = lw)
ax8.plot(rho_ips,jbs_ips,color = c2,linewidth = lw,linestyle = 'dashed')
ax8.set_ylabel('j_bs')

ax9.plot(rho_main,pe_rf1,color = c1,linewidth = lw)
ax9.plot(rho_ips,pe_rf,color = c2,linewidth = lw,linestyle = 'dashed')
ax9.plot(rho_main,pi_rf,color = c3,linewidth = lw)
ax9.plot(rho_ips,pi_rf,color = c4,linewidth = lw,linestyle = 'dashed')
ax9.set_ylabel('q_aux [MW/m$^3$]')
fig.tight_layout()

