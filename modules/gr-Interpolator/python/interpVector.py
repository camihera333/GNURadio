# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: interpVector
# Generated: Thu Aug  2 18:21:25 2018
##################################################


from gnuradio import gr
from gnuradio.filter import firdes
import Interpolators


class interpVector(gr.hier_block2):

    def __init__(self, data=8):
        gr.hier_block2.__init__(
            self, "interpVector",
            gr.io_signature(1, 1, gr.sizeof_float*1),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.data = data

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.Interpolators_interpolatorVector_0 = Interpolators.interpolatorVector(data)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Interpolators_interpolatorVector_0, 0), (self, 0))
        self.connect((self, 0), (self.Interpolators_interpolatorVector_0, 0))

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
        self.Interpolators_interpolatorVector_0.set_tam_info(self.data) 
    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
