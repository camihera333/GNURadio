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

class sourceVector(gr.sync_block):
    """
    docstring for block sourceVector_py_nf
    """
    def __init__(self, invector):
        gr.sync_block.__init__(self,
            name="sourceVector",
            in_sig=None,
            out_sig=[np.float32])
	self.set_output_multiple(4096*2)
	self.invector=np.array(invector)

    def set_invector(self,invector):
        self.invector=invector
    def work(self, input_items, output_items):
        out = output_items[0]

        # <+signal processing here+>
        out[:] = np.tile(self.invector,8192/len(self.invector))
        return len(output_items[0])
