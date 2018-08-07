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
import math
from gnuradio import gr


class SNR(gr.sync_block):
    """
    docstring for block SNR
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="SNR",
            in_sig=[numpy.float32, numpy.float32],
            out_sig=[numpy.float32])

    def work(self, input_items, output_items):
        in0 = input_items[0]
        in1 = input_items[1]
        out = output_items[0]
        pot2=0
        pot1=0
        for i in range(len(in0)):
            pot1=pot1+(in0[i]**2)
        for i in range(len(in1)):
            pot2=pot2+(in1[i]**2)
        pot1=(pot1)/len(in0)
        pot2=(pot2)/len(in1)
        if pot2==0.0:
            pot2=0.000000000001
        snrveces=pot1/pot2
        snr=10*math.log10(snrveces)
        out[:]=snr
        return len(output_items[0])
