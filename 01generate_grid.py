from t2grids import *
from t2data import *
from t2incons import *
from t2listing import *

################################################################################
#IMPORTANT! check PyTOUGH manual for what all these things mean
################################################################################
# number in [] is block width or thickness, number after * is how many 
x=[2000]*10
y=[2000]*10
z=[1000]*10
origin=[0.0,0.0,0.0]
################################################################################
atmos_type=0
convention=0
#angle=30
#permeability_dir=-45
#PUT IN YOUR OWN CO-ORDS & shift if you need to
#centre=[10000,10000]
#shift=[-4500.0,-1400.0,0.0]
geo=mulgrid().rectangular(x,y,z,convention,atmos_type,origin)
#rotate grid if necessary - need value for angle & centre
#geo.rotate(angle,centre)
#geo.permeability_angle=permeability_dir
#translate grid
#geo.translate(shift)
#ADD WELLS - FILE REQ'D#########################################################
#open file & loop thru lines, read &:::::::::::::::::::::::::::::::::::::::::::: 
#
#f=open('well-coords.dat')
#for line in f.readlines():
#  values=line.split(',')
#  print values
#  name=values[0]
#  top=[float(values[1]),float(values[2]),float(values[3])]
#  bot=[float(values[4]),float(values[5]),float(values[6])]
#  w=well(name,[top,bot])
#  geo.add_well(w)
#f.close()
################################################################################
#WRITE GEOMETRY FILE
geo.write('Geometry.dat')
#geo.export_surfer('mulgraph_gridfilename.bna')


