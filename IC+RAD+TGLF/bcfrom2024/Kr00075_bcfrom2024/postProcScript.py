from toric_tools import *

filename = 'toric.nc'
minority_species_indx = -4

toricFile = toric_analysis(toric_name=filename, mode='ICRF')
toricFile.toricPlots(min_indx=minority_species_indx)
toricFile.close()
