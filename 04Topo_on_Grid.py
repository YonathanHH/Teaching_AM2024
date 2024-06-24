from t2grids import *
from t2data import *
from t2incons import *
from t2listing import *

print ('hello')
#read model grid
geo=mulgrid('Geometry_02b.dat')

##############################################################################

#this fits the surface to xyz, note can fit specific cols if req'd
topo_data=np.loadtxt('Mountain.dat', delimiter=',')
print ('hello_again')
geo.fit_surface(topo_data,1.0,1.0)
#write geometry file
geo.write('Geometry_03.dat')

#geo.export_surfer('g_.bna')
