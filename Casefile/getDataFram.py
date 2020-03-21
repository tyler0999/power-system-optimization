#Author: itaoxiaoran
#E-mail: ta0ran@163.com
#Read more: https://github.com/itaoxiaoran/power-system-optimization

import numpy as np
import sys
import pandas as pd

def getDataFrame(path):
    ##creat bus, branch, gen, gencost index
    idxbus = ['BUS_I', 'BUS_TYPE', 'Pd', 'Qd', 'Gs', 'Bs', 'BUS_AREA', 'Vm', 'Va', 'BASE_KV', 'ZONE', 'Vmax',
              'Vmin']
    idxgen = ['GEN_BUS', 'Pg', 'Qg', 'Qmax', 'Qmin', 'Vg', 'mBase', 'status', 'Pmax', 'Pmin', 'Pc1', '	Pc2',
              'Qc1min', 'Qc1max', 'Qc2min', 'Qc2max', 'ramp_agc', 'ramp_10', 'ramp_30', 'ramp_q', 'apf']
    idxbrch = ['fbus', 'tbus', 'r', 'x', 'b', 'rateA', 'rateB', 'rateC', 'ratio', 'angle', 'status', 'angmin',
               'angmax']
    #I just provide the cost form in linear and quadratic function
    #If you want use another form, you can change the idxgencost (Only surpported by polynomial)
    idxgencost_1 = ['v2', 'startup', 'shutdown', 'n_eq_2', 'c1', 'c0']  # Generator cost function written as a linear function
    idxgencost_2 = ['v2', 'startup', 'shutdown', 'n_eq_3', 'c2', 'c1', 'c0']  # Generator cost function written as a quadratic function
    bus_ndarray = np.loadtxt(path + 'bus.dat', delimiter=',')
    gen_ndarray = np.loadtxt(path + 'gen.dat', delimiter=',')
    brch_ndarray = np.loadtxt(path + 'brch.dat', delimiter=',')
    gencost_ndarray = np.loadtxt(path + 'gencost.dat', delimiter=',')

    if gencost_ndarray.shape[1] == 6: # is linear
        idxgencost = idxgencost_1
    elif gencost_ndarray.shape[1] == 7: # is quadratic
        idxgencost = idxgencost_2
    else: # if you want use another form, you can change there.
        print('Generation cost function is not in the form of a linear or quadratic polynomial !')
        sys.exit()

    bus_df = pd.DataFrame(bus_ndarray, columns=idxbus)
    gen_df = pd.DataFrame(gen_ndarray, columns=idxgen)
    brch_df = pd.DataFrame(brch_ndarray, columns=idxbrch)
    gencost_df = pd.DataFrame(gencost_ndarray, columns=idxgencost)

    return bus_df, gen_df, brch_df, gencost_df

if __name__ == '__main__':
    # if you want to test this function
    # you can run this
    # and change the filePath, i.e. filePath='C:/case5'
    # filePath = 'X:/.../caseName/'
    filePath ='F:/本地_华电_研究生/pycase/case5/'
    bus_df, gen_df, brch_df, gencost_df = getDataFrame(path=filePath)