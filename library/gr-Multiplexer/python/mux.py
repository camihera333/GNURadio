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

class mux(gr.sync_block):
    """
    docstring for block mux
    """
    def __init__(self, sel):
        gr.sync_block.__init__(self,
            name="mux",
            in_sig=[numpy.float32,numpy.float32,numpy.float32],
            out_sig=[numpy.float32])
        self.sel=sel


    def set_sel(self,sel):
        self.sel=sel
    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        in2 = input_items[2]
        out = output_items[0]
        # <+signal processing here+>

        if self.sel==1:
            out[:]=in0
        elif self.sel==2:
            out[:]=in1
        elif self.sel==3:
            out[:]=in2
        else:
            print('ERROR:Opción de canal no válida (1=Gaussian, 2=Rician, 3=Rayleigh)')
        return len(output_items[0])
