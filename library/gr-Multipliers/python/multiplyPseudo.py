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

class multiplyPseudo(gr.sync_block):
    """
    docstring for block multiplyPseudo
    """
    def __init__(self, chips,tam_info):
        gr.sync_block.__init__(self,
            name="multiplyPseudo",
            in_sig=[numpy.float32,numpy.float32],
            out_sig=[numpy.float32])
        self.chips=chips
        self.tam_info=tam_info
        self.musbit=8192/(self.chips*self.tam_info)
        self.set_output_multiple(8192)
    def set_tam_info(self,tam_info):
        self.tam_info=tam_info
        self.musbit=8192/(self.chips*self.tam_info)
    def set_chips(self,chips):
        self.chips=chips
        self.musbit=8192/(self.chips*self.tam_info)

    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]
        fu=in0[::8192/self.tam_info]
        pn=in1[::8192/self.chips]
        sen=[]
        for i in range(self.tam_info):
            for j in range(self.chips):
                sen.append(fu[i]*pn[j])
        sen=numpy.array(sen)
        out[:] = sen.repeat(self.musbit)
        # <+signal processing here+>
        return len(output_items[0])
