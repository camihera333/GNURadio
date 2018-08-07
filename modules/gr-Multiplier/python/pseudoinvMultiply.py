# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: pseudoinvMultiply
# Generated: Thu Aug  2 19:21:56 2018
##################################################


from gnuradio import gr
from gnuradio.filter import firdes
import Multipliers


class pseudoinvMultiply(gr.hier_block2):

    def __init__(self, Chips=4, data=8):
        gr.hier_block2.__init__(
            self, "pseudoinvMultiply",
            gr.io_signaturev(2, 2, [gr.sizeof_float*1, gr.sizeof_float*1]),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Chips = Chips
        self.data = data

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.Multipliers_multiplyPseudoInv_0 = Multipliers.multiplyPseudoInv(Chips, data)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Multipliers_multiplyPseudoInv_0, 0), (self, 0))
        self.connect((self, 0), (self.Multipliers_multiplyPseudoInv_0, 0))
        self.connect((self, 1), (self.Multipliers_multiplyPseudoInv_0, 1))

    def get_Chips(self):
        return self.Chips

    def set_Chips(self, Chips):
        self.Chips = Chips
        self.Multipliers_multiplyPseudoInv_0.set_chips(self.Chips)
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
        self.Multipliers_multiplyPseudoInv_0.set_tam_info(self.data)
    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
