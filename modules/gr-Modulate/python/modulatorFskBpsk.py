# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: modulatorFskBpsk
# Generated: Thu Aug  2 19:12:30 2018
##################################################


from gnuradio import gr
from gnuradio.filter import firdes
import Modulator


class modulatorFskBpsk(gr.hier_block2):

    def __init__(self, M=1):
        gr.hier_block2.__init__(
            self, "modulatorFskBpsk",
            gr.io_signature(1, 1, gr.sizeof_float*1),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.M = M

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.Modulator_fskbpskModulator_0 = Modulator.fskbpskModulator(M)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Modulator_fskbpskModulator_0, 0), (self, 0))
        self.connect((self, 0), (self.Modulator_fskbpskModulator_0, 0))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.Modulator_fskbpskModulator_0.set_mod(self.M)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
