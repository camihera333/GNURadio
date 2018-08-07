# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: synthesizerFreq
# Generated: Thu Aug  2 18:17:48 2018
##################################################


from gnuradio import gr
from gnuradio.filter import firdes
import Generators


class synthesizerFreq(gr.hier_block2):

    def __init__(self, Bits=2, Delta=1000, Carrier=10000,Data_Size=8):
        gr.hier_block2.__init__(
            self, "synthesizerFreq",
            gr.io_signature(0, 0, 0),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Bits = Bits
        self.Delta = Delta
        self.Carrier = Carrier
        self.Data_Size=Data_Size
        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.Generators_frecSynthesizer_0 = Generators.frecSynthesizer(Carrier, Delta, Bits,Data_Size)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Generators_frecSynthesizer_0, 0), (self, 0))

    def get_Bits(self):
        return self.Bits

    def set_Bits(self, Bits):
        self.Bits = Bits
        self.Generators_frecSynthesizer_0.set_bps(self.Bits)

    def get_Data_Size(self):
        return self.Data_size

    def set_Data_Size(self, Data_Size):
        self.Data_Size = Data_Size
        self.Generators_frecSynthesizer_0.set_tam_info(self.Data_Size)
    def get_Delta(self):
        return self.Delta

    def set_Delta(self, Delta):
        self.Delta = Delta
        self.Generators_frecSynthesizer_0.set_fd(self.Delta)

    def get_Carrier(self):
        return self.Carrier

    def set_Carrier(self, Carrier):
        self.Carrier = Carrier
        self.Generators_frecSynthesizer_0.set_fc(self.Carrier)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
