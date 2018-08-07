# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: walsh_hadamard
# Generated: Thu Aug  2 18:13:46 2018
##################################################


from gnuradio import gr
from gnuradio.filter import firdes
import Generators


class walsh_hadamard(gr.hier_block2):

    def __init__(self, Chips=4):
        gr.hier_block2.__init__(
            self, "walsh_hadamard",
            gr.io_signature(0, 0, 0),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Chips = Chips

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.Generators_walsh_hadamand_0 = Generators.walsh_hadamand(Chips)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Generators_walsh_hadamand_0, 0), (self, 0))

    def get_Chips(self):
        return self.Chips

    def set_Chips(self, Chips):
        self.Chips = Chips
        self.Generators_walsh_hadamand_0.set_z(self.Chips)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
