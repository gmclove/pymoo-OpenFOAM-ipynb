#### import the simple module from the paraview
from paraview.simple import *
import sys

gen = int(sys.argv[1])
ind = int(sys.argv[2])
L_diff = float(sys.argv[3])

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

## Load the case
case_foam = OpenFOAMReader( FileName='./cases/gen%i/ind%i/g%ii%i.OpenFOAM' %(gen, ind, gen, ind))

# get active source.
case = GetActiveSource()

###########################################################################
########   Extract Data   #################
# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=case,
    Source='High Resolution Line Source')

# Properties modified on plotOverLine1
plotOverLine1.Tolerance = 2.22044604925031e-16

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [L_diff, 0.8, 0.1] #4.67614808
plotOverLine1.Source.Point2 = [L_diff, 0.1, 0.1] #4.67614808


###########################################################################
########## Save Data  #################################3
# save data
SaveData('./cases/gen%i/ind%i/plotOverLineData.csv' %(gen, ind), proxy=plotOverLine1)
