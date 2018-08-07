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
import numpy
from gnuradio import gr
import math
from scipy import interpolate

class fskbpskModulator(gr.sync_block):
    """
    docstring for block fskbpskModulator
    """
    def __init__(self,mod):
        gr.sync_block.__init__(self,
            name="fskbpskModulator",
            in_sig=[np.float32],
            out_sig=[np.float32])
        self.mod=mod
        self.f0=1000
        self.f1=2000
        self.set_output_multiple(8192)

    def set_mod(self,mod):
        self.mod=mod
    def sen(self,arg):
        sal=[]
        for i in range(len(arg)):
            sal.append(math.sin(arg[i]))
        return sal

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        ts=1.0/32000.0
        tf=ts*8192
        t=numpy.linspace(0.0,tf,8192)
        if self.mod==1:
            mod=[]
            for n in range(8192):
                if in0[n]==-1:
                    c=math.sin(2*math.pi*self.f0*t[n])
                    mod.append(c*in0[n])
                elif in0[n]==1:
                    c=math.sin(2*math.pi*self.f1*t[n])
                    mod.append(c*in0[n])
            # <+signal processing here+>
            out[:] = mod
        else:
            f=1000
            c=self.sen(2*math.pi*f*t)
            mod=[]
            for n in range(0,8192):
    			mod.append(c[n]*in0[n])
            out[:] = mod
        # <+signal processing here+>
        return len(output_items[0])
