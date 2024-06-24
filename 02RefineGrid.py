from t2grids import *
from t2data import *
from t2incons import *
from t2listing import *

#read model grid
geo=mulgrid('Geometry.dat')

#refine the grid where given a list of co-ordinates:
#columns to refine:
columns_refine=np.loadtxt('pols.dat',delimiter=',')
print (columns_refine)
#need to find cols in polygon
skinny_columns=geo.columns_in_polygon(columns_refine)
print (skinny_columns)
geo.refine(skinny_columns)
#write geometry file
geo.write('Geometry_02.dat')
#geo.export_surfer('g_.bna')
