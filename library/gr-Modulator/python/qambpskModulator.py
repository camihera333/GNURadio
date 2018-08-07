#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy as np
from gnuradio import gr
import math
from scipy import interpolate

class qambpskModulator(gr.sync_block):
    """
    docstring for block qambpskModulator
    """
    def __init__(self, mod,tambit,chips):
        gr.sync_block.__init__(self,
            name="qambpskModulator",
            in_sig=[np.float32],
            out_sig=[np.float32,np.float32,np.float32])
        self.tambit=tambit
        self.chips=chips
        self.mod=mod
        self.set_output_multiple(8192)

    def set_chips(self,chips):
        self.chips=chips
    def set_tambit(self,tambit):
        self.tambit=tambit
    def set_mod(self,mod):
        self.mod=mod
    def bitodec(self,a):
        b=[]
        for i in range(len(a)):
            b.append(str(int(a[i])))
        c=""
        c=c.join(b)
        c=int(c,2)
        return c

    def sen(self,arg):
        sal=[]
        for i in range(len(arg)):
            sal.append(math.sin(arg[i]))
        return sal

    def cos(self,arg):
        sal=list()
        for i in range(len(arg)):
            sal.append(math.cos(arg[i]))
        sal=np.array(sal)
        return(sal)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]

        ts=1.0/32000.0
        tf=ts*8192
        t=np.linspace(0.0,tf,8192)
        f=1000
        out1 = output_items[1]
        out2 = output_items[2]
        if self.mod==1:

            z=np.linspace(0,15,16)
            x=np.array([-3,-3,-3,-3,-1,-1,-1,-1,3,3,3,3,1,1,1,1])
            y=np.array([3,1,-3,-1,3,1,-3,-1,3,1,-3,-1,3,1,-3,-1])
            interpox = interpolate.interp1d(z, x)
            interpoy = interpolate.interp1d(z, y)
            tamb=self.tambit*self.chips
            mb=int(8192/tamb)
            bits=(in0[::mb]+1)/2
            nsim=int(tamb/4)
            valx=list()
            valy=list()
            for i in range(nsim):
                grup=bits[i*4:(i*4)+4]
                decval=self.bitodec(grup)
                valx.append(interpox(decval))
                valy.append(interpoy(decval))
            valx=np.array(valx)
            valy=np.array(valy)
            valx=valx.repeat(8192/nsim)
            valy=valy.repeat(8192/nsim)
            out1[:]=valx
            out2[:]=valy
            out[:]=(valx*self.cos(2*math.pi*f*t))+(valy*self.sen(2*math.pi*f*t))

        else:
            c=self.sen(2*math.pi*f*t)
            mod=[]
            for n in range(0,8192):
    			mod.append(c[n]*in0[n])
            out[:] = mod
            out1[:] = in0
            out2[:] = np.zeros((8192,), dtype=int)
        return len(output_items[0])
