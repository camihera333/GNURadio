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

class qambpskDemodulator(gr.sync_block):
    """
    docstring for block qambpskDemodulator
    """
    def __init__(self, mod,tambit,chips):
        gr.sync_block.__init__(self,
            name="qambpskDemodulator",
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

    def dectobin(self,val):
        bi=np.zeros(4)
        for i in range(4):
            res=val%2
            val=val//2
            bi[3-i]=res
        return bi

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        ts=1.0/32000.0
        tf=ts*8192
        t=np.linspace(0.0,tf,8192)
        f=1000
        y1=self.sen(2*math.pi*f*t)
        y2=self.cos(2*math.pi*f*t)
        sal1=y1*in0
        sal2=y2*in0
        tamb=self.tambit*self.chips
        mb=int(8192/tamb)
        out1 = output_items[1]
        out2 = output_items[2]
        if self.mod==1:
            nsim=int(tamb/4)
            msim=int(8192/nsim)
            raz=tamb/8
            vmax=6000/raz
            vmin=2000/raz
            umb=(vmax+vmin)/2
            simx=list()
            simy=list()
            z=np.linspace(0,15,16)
            x=np.array([-3,-3,-3,-3,-1,-1,-1,-1,3,3,3,3,1,1,1,1])
            y=np.array([3,1,-3,-1,3,1,-3,-1,3,1,-3,-1,3,1,-3,-1])
            interpo = interpolate.interp2d(x,y,z)
            for i in range(nsim):
                sel1=sal1[i*msim:(i*msim)+msim]
                sel2=sal2[i*msim:(i*msim)+msim]
                sx=np.trapz(sel2)
                sy=np.trapz(sel1)
                if sx>0:
                    if sx>umb:
                        simx.append(3)
                    else:
                        simx.append(1)
                else:
                    if sx<-umb:
                        simx.append(-3)
                    else:
                        simx.append(-1)
                if sy>0:
                    if sy>umb:
                        simy.append(3)
                    else:
                        simy.append(1)
                else:
                    if sy<-umb:
                        simy.append(-3)
                    else:
                        simy.append(-1)
            simx=np.array(simx)
            simy=np.array(simy)
            valx=simx
            valy=simy
            bina=[]
            for i in range(nsim):
                vald=interpo(valx[i],valy[i])
                bb=self.dectobin(vald)
                bina=np.concatenate([bina,bb])
            bina=(bina*2)-1
            out[:] = bina.repeat(mb)
            out1[:]=simx.repeat(msim)
            out2[:]=simy.repeat(msim)
        else:
            bitsal=list()
            bit=list()
            for i in range(tamb):
                sel=sal1[i*mb:(i*mb)+mb]
                bit.append(np.trapz(sel))
            bit=np.array(bit)
            for i in range(tamb):
                if bit[i]>(-1/2):
                    bitsal.append(1)
                else:
                    bitsal.append(-1)
            bitsal=np.array(bitsal)
            out[:] =bitsal.repeat(8192/tamb)
            out1[:]=bitsal.repeat(8192/tamb)
            out2[:]=np.zeros((8192,), dtype=int)
        return len(output_items[0])
