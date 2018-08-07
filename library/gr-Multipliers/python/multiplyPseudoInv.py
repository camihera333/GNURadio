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

import numpy
from gnuradio import gr

class multiplyPseudoInv(gr.sync_block):
    """
    docstring for block multiplyPseudoInv
    """
    def __init__(self, chips,tam_info):
        gr.sync_block.__init__(self,
            name="multiplyPseudoInv",
            in_sig=[numpy.float32,numpy.float32],
            out_sig=[numpy.float32])
        self.set_output_multiple(8192)
        self.chips=chips
        self.tam_info=tam_info
        self.mul=self.chips*self.tam_info

    def set_chips(self,chips):
        self.chips=chips
        self.mul=self.chips*self.tam_info
    def set_tam_info(self,tam_info):
        self.tam_info=tam_info
        self.mul=self.chips*self.tam_info

    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]
        # <+signal processing here+>
        fu=in0[::8192/self.mul]
        pn=in1[::8192/self.chips]
        senori=numpy.ones(self.tam_info)
        sen=[]
        for i in range(self.tam_info):
            for j in range(self.chips):
                sen.append(senori[i]*pn[j])
        sen=numpy.array(sen)
        fin=[]
        for i in range(self.mul):
            fin.append(sen[i]*fu[i])
        fin=numpy.array(fin)
        fin=fin[::self.chips]
        out[:]=fin.repeat(8192/len(fin))
        return len(output_items[0])
