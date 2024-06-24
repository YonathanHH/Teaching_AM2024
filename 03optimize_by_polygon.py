from t2grids import *
import numpy as np

#read large model grid
#this assumes 2 refinements - if only one then should read 2a
geo=mulgrid('Geometry_02.dat')
#nodes to optimize:
opt = np.loadtxt('pols.dat',delimiter=',')
#need to find cols in polygon
opt_nodes = geo.nodes_in_polygon(opt)
print(opt_nodes)
#going from nodes to nodenames
opt_nodes_list=[tempnode.name for tempnode in opt_nodes]
geo.optimize(opt_nodes_list, 1.0, 0.5, 0.0, False)
#write geometry file. Note the filename is just for tracking 
#until I get it right.  Then I rename to 001_grid.dat
geo.write('Geometry_02b.dat')

#np.loadtxt('03polygon_optimize.dat',delimiter=',')

