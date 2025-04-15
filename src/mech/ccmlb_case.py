#!/usr/bin/env python3

from numba import njit
from fuzzyometry import bodies as bd
from fuzzyometry import combinations as cmb
from xyzcad import render


@njit
def fz_top(x, y, z):
    body = bd.fz_cuboid((x,y,z-7), (174.8,85.8,6.),1.5)
    nose = bd.fz_cuboid(((x-2)%21.42 -10.21,y-43,z-5.5), (8.,4.,1.),1.0)
    noselim = cmb.fz_and_chamfer(0.5, nose, -x-85, x-85)
    #lc = bd.fz_cuboid((x,y-2,z+6), (180.,76.,20.),1.5)
    mc = bd.fz_cuboid((x,y,z+2), (171.,82.,20.),1.5)
    fw = bd.fz_cuboid((x-10,y+42,z+3), (120.,2.,22.),1)
    btn1 = bd.fz_cuboid((x-51,y+44,z+8), (8.,3.,8.),1)
    btn2 = bd.fz_cuboid((x+33,y+44,z+8), (8.,3.,8.),1)
    pcbhld = bd.fz_cuboid((x+5.,y,z+1.25), (3.,50.,18.5),1.)
    solid = cmb.fz_or_chamfer(0.5, body, noselim, fw, btn1, btn2)
    return cmb.fz_or_chamfer(0.5,cmb.fz_and_chamfer(0.5, solid, -mc), pcbhld)

@njit
def case_top(x, y, z):
    if  fz_top(x, y, z) > 0:
        return False
    return True



@njit
def case_bottom(x, y, z):
    return True

res = 0.2
render.renderAndSave(case_top, "gen/mech/case_cmmlb_top.stl", res)
#render.renderAndSave(case_bottom, "case_cmmlb_bottom.stl", res)


