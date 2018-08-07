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

class interpolatorVector(gr.sync_block):
    """
    docstring for block interpolatorVector
    """
    def __init__(self, tam_info):
        gr.sync_block.__init__(self,
            name="interpolatorVector",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
        self.set_output_multiple(8192)
        self.tam_info=tam_info
    def set_tam_info(self,tam_info):
        self.tam_info=tam_info
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        cam=in0[0:self.tam_info]
        # <+signal processing here+>
        out[:] = cam.repeat(8192/self.tam_info)
        return len(output_items[0])
