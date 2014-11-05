import Image
import numpy as na
import pylab as p
import scipy.interpolate as intp

F=Image.open('MDP.jpg').convert('L')
arr=na.flipud(p.array(F))

NX=214
NY=286
x=na.arange(214)
y=na.arange(286)


##X,Y=p.meshgrid(x,y)

I=intp.interp2d(x,y,arr)


