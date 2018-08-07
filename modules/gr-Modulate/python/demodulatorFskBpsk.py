# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: demodulatorFskBpsk
# Generated: Thu Aug  2 19:15:09 2018
##################################################


from gnuradio import gr
from gnuradio.filter import firdes
import Modulator


class demodulatorFskBpsk(gr.hier_block2):

    def __init__(self, data=8):
        gr.hier_block2.__init__(
            self, "demodulatorFskBpsk",
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
        self.Modulator_fskbpskDemodulator_0 = Modulator.fskbpskDemodulator(data)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Modulator_fskbpskDemodulator_0, 0), (self, 0))
        self.connect((self, 0), (self.Modulator_fskbpskDemodulator_0, 0))

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
        self.Modulator_fskbpskDemodulator_0.set_taminfo(self.data)
    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
