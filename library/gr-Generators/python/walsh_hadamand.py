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
from random import randint
from gnuradio import gr

class walsh_hadamand(gr.sync_block):
    """
    docstring for block walsh_hadamand_py_nf
    """
    def __init__(self, chips):
        gr.sync_block.__init__(self,
            name="walsh_hadamand",
            in_sig=None,
            out_sig=[np.float32])
        self.z=chips
        self.set_output_multiple(4096*2)
        self.ban=0

    def set_z(self,chips):
        self.z=chips
        self.ban=0
    def work(self, input_items, output_items):
        out = output_items[0]

        if (self.ban==0):
            if (self.z==1):
                aux=0
            elif (self.z==2):
                aux=1
            elif(self.z==4):
                aux=2
            elif (self.z==8):
                aux=3
            elif (self.z==16):
                aux=4

            w1=[1]
            w2=[[1,1],[1,-1]]
            w2=np.matrix(w2)
            w3=np.concatenate((np.concatenate((w2,w2)).transpose(),np.concatenate((w2,-w2)).transpose()))
            w4=np.concatenate((np.concatenate((w3,w3)).transpose(),np.concatenate((w3,-w3)).transpose()))
            w5=np.concatenate((np.concatenate((w4,w4)).transpose(),np.concatenate((w4,-w4)).transpose()))
            w=[w1,w2,w3,w4,w5]
            fi=randint(1,self.z-1)
            self.c=w[aux][fi,:]
            self.ban=1
        out[:] = self.c.repeat(8192/self.z)
        #print(len(out))

        return len(output_items[0])
