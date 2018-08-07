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

class fskbpskDemodulator(gr.sync_block):
    """
    docstring for block fskbpskDemodulator
    """
    def __init__(self, taminfo):
        gr.sync_block.__init__(self,
            name="fskbpskDemodulator",
            in_sig=[np.float32],
            out_sig=[np.float32])
        self.f=1000
        self.taminfo=taminfo
        self.set_output_multiple(8192)

    def set_taminfo(self,taminfo):
        self.taminfo=taminfo
    def sen(self,arg):
        sal=list()
        for i in range(len(arg)):
            sal.append(math.sin(arg[i]))
        sal=np.array(sal)
        return(sal)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        t=np.linspace(0.0,8192*(1.0/32000),8192)
        y1=self.sen(2*math.pi*self.f*t)
        sal1=y1*in0
        bitsal=list()
        bit=list()
        mb=8192/self.taminfo
        for i in range(self.taminfo):
            sel=sal1[i*mb:(i*mb)+mb]
            bit.append(np.trapz(sel))
        bit=np.array(bit)
        valo=np.array([-8.39314869e+00,-2.55954471e+04])
        v=valo.sum()/self.taminfo
        for i in range(self.taminfo):
            if bit[i]>(v):
                bitsal.append(1)
            else:
                bitsal.append(-1)
        bitsal=np.array(bitsal)
        out[:] = bitsal.repeat(8192/self.taminfo)
        return len(output_items[0])
