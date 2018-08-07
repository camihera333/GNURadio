# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: modulatorQamBpsk
# Generated: Thu Aug  2 19:08:22 2018
##################################################


from gnuradio import gr
from gnuradio.filter import firdes
import Modulator


class modulatorQamBpsk(gr.hier_block2):

    def __init__(self, Chips=4, M=1, data=8):
        gr.hier_block2.__init__(
            self, "modulatorQamBpsk",
            gr.io_signature(1, 1, gr.sizeof_float*1),
            gr.io_signaturev(3, 3, [gr.sizeof_float*1, gr.sizeof_float*1, gr.sizeof_float*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Chips = Chips
        self.M = M
        self.data = data

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.Modulator_qambpskModulator_0 = Modulator.qambpskModulator(M, data, Chips)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Modulator_qambpskModulator_0, 1), (self, 0))
        self.connect((self.Modulator_qambpskModulator_0, 0), (self, 1))
        self.connect((self.Modulator_qambpskModulator_0, 2), (self, 2))
        self.connect((self, 0), (self.Modulator_qambpskModulator_0, 0))

    def get_Chips(self):
        return self.Chips

    def set_Chips(self, Chips):
        self.Chips = Chips
        self.Modulator_qambpskModulator_0.set_chips(self.Chips)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.Modulator_qambpskModulator_0.set_mod(self.M)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
        self.Modulator_qambpskModulator_0.set_tambit(self.data)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
