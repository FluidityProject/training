#!/usr/bin/env python

import string
import os
import vtktools
from numpy import argsort, size
from pylab import *
import time
import argparse
import re

ion()

def main():

    # Probably a bit of overkil for a simple script, but let's add some options
    # Later we can add a -v flag and a flag to save an animation or something
    parser = argparse.ArgumentParser(
         description="""This script visualises the tracer_advection_dg example."""
                     """The only argument is the directory where the VTU files reside."""
                     )
    parser.add_argument(
            '-s', 
            '--sleep', 
             help="Pause between frame updates (in seconds). Default is 0.1",
             default=0.1
            )
    
    
    parser.add_argument(
            'directory',
            help="A directory containing the output files from the example."
            )
    args = parser.parse_args()
    directory = str(args.directory)
    sleep = float(args.sleep)

    # This grabs all the pvtus and vtus in the directory given, sorted in human-readbale order
    # which means the order is 0, 1, 2, ..., 9, 10, 11, 12 as we'd expect.
    vtus = get_vtus(directory)

    # set up the figure we're going to animate
    line = plot_tracer(vtus[8])
    #show()
    for v in vtus:
        # plot the tracer value along the x-axis
        time.sleep(sleep)
        line = plot_tracer(v, line)

#### taken from http://www.codinghorror.com/blog/archives/001018.html    #######
def sort_nicely( l ): 
    """ Sort the given list in the way that humans expect. 
    """ 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    l.sort( key=alphanum_key ) 


######################
def get_vtus(directory):
    """ For a given directory, list all PVTU/VTU files, except checkpoint & Mesh files
    """ 
    files = []
    dirList=os.listdir(directory)
    for file in dirList:
        if (string.find(file, 'checkpoint') != -1):
            continue
        elif (string.find(file, 'Mesh') != -1):
            continue
        elif (string.find(file, 'vtu') != -1):
            files.append(directory + "/" + file)
        else:
            continue

    sort_nicely(files)
    return files

def get_1d_indices(pos, z0=1.0, tolerance=1.0e-5):
    """ Return the field indices corresponding to the ordered depth values at position (x0, y0)
    """
    ind = argsort(-pos[:,0])
    indices = []
    for i in ind:
        if (z0-tolerance < pos[i][1] < z0+tolerance):
            indices.append(i)
    return indices

def plot_tracer(vtu_file, line=None):
    
    u=vtktools.vtu(vtu_file)
    pos = u.GetLocations()
    time = u.GetScalarField('Time')[0]
    t = u.GetScalarField('Tracer')
    ind = get_1d_indices(pos)
    distance = vtktools.arr([pos[i,0] for i in ind])
    tracer = vtktools.arr( [t[i] for i in ind] )

    if (line):
        line.set_ydata(tracer)  # update the data
        draw()
    else:
        line, = plot(distance,tracer,color='k')
        
    return line

    
if __name__ == "__main__":
    main()
