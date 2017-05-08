# Weight balance visualisation for ASK-21 glider
#
# See README.md for details
#
# Plotting solution based on
# http://stackoverflow.com/questions/17576508/python-matplotlib-drawing-linear-inequality-functions
#
# Ilya Kizhvatov, ilya.kizhvatov@gmail.com

import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

###################################################################################################
# Define weight constraints

minFrontWeight = 70
maxFrontWeight = 110
minBackWeight = 0
maxBackWeight = 110
backToFrontContribCoef = 0.33

# min and max weights in the back as a function of the front seat weight from (1)
def minBackWeightFunc(f):
    return (minFrontWeight - f) / backToFrontContribCoef
def maxBackWeightFunc(f):
    return (maxFrontWeight - f) / backToFrontContribCoef

# maximum total weight as a function of the front seat weight
def maxTotalWeight(f):
    return f + np.minimum(maxBackWeight, maxBackWeightFunc(f))

# find points of intersection which will define the area of admissible weight combinations
f = Symbol('f')
x1, =  solve(minBackWeightFunc(f) - maxBackWeight)
x2, =  solve(maxBackWeightFunc(f) - maxBackWeight)
x3, =  solve(maxBackWeightFunc(f) - minBackWeight)
x4, =  solve(minBackWeightFunc(f) - minBackWeight)
y1 = minBackWeightFunc(x1)
y2 = maxBackWeightFunc(x2)
y3 = maxBackWeightFunc(x3)
y4 = minBackWeightFunc(x4)


###################################################################################################
# Plot it all
# There will be two subplots:
# - admissible weight combintaions area (bottom)
# - maximum total weight (top)

# create figure with a 5, 5*1.4142 aspect ratio
# two sublots with 1:3 height ratio
fig = plt.figure(figsize=(5, 5*1.414))
gs = gridspec.GridSpec(2, 1, height_ratios=[1,3])
axBalance = plt.subplot(gs[1])
axTotal = plt.subplot(gs[0])

fig.suptitle("ASK-21 Weight Balance", fontsize=16)

# limits for axes
xMin = 30
xMax = maxFrontWeight
yMinBalance = 0
yMaxBalance = maxFrontWeight + 10
yMinTotal = 100
yMaxTotal = 200

# plot the area
axBalance.fill([x1,x2,x3,x4],[y1,y2,y3,y4], 'green')

axBalance.set_xlim([xMin, xMax])
axBalance.set_ylim([yMinBalance, yMaxBalance])
axBalance.set_xticks(np.arange(xMin, xMax + 1, 10))
axBalance.set_xticks(np.arange(xMin, xMax + 1, 2), minor=True)
axBalance.set_yticks(np.arange(yMinBalance, yMaxBalance + 1, 10))
axBalance.set_yticks(np.arange(yMinBalance, yMaxBalance + 1, 2), minor=True)
axBalance.grid(b=True, which='both', color='0.75')
axBalance.set_facecolor((1,0.4,0.4))
axBalance.set_xlabel('Front seat, kg')
axBalance.set_ylabel('Back seat, kg')

# plot the total weight
xr = np.linspace(xMin, xMax, 100)
axTotal.plot(xr, maxTotalWeight(xr))

axTotal.set_xlim([xMin, xMax])
axTotal.set_ylim([yMinTotal, yMaxTotal])
axTotal.set_xticks(np.arange(xMin, xMax + 1, 10))
axTotal.set_xticks(np.arange(xMin, xMax + 1, 2), minor=True)
axTotal.set_yticks(np.arange(yMinTotal, yMaxTotal + 1, 20))
axTotal.set_yticks(np.arange(yMinTotal, yMaxTotal + 1, 10), minor=True)
axTotal.tick_params(axis='x', which='both', top='off', bottom='off', labelbottom='off')
axTotal.grid(b=True, which='both', color='0.65') 
axTotal.set_ylabel('Max total, kg')

plt.show()
