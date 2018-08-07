# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Channels
# Generated: Fri Aug  3 00:47:25 2018
##################################################


from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import Transmission_Channels


class Channels(gr.hier_block2):

    def __init__(self, k=4.0, tchannel=1, voltage=0):
        gr.hier_block2.__init__(
            self, "Channels",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.k = k
        self.tchannel = tchannel
        self.voltage = voltage

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.channel_0_0 = Transmission_Channels.channel(
            k=k,
            tchannel=tchannel,
            voltage=voltage,
        )
        self.channel_0 = Transmission_Channels.channel(
            k=k,
            tchannel=tchannel,
            voltage=voltage,
        )
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_float_0, 0), (self.channel_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.channel_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self, 0))
        self.connect((self.channel_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.channel_0_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self, 0), (self.blocks_complex_to_float_0, 0))

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k
        self.channel_0_0.set_k(self.k)
        self.channel_0.set_k(self.k)

    def get_tchannel(self):
        return self.tchannel

    def set_tchannel(self, tchannel):
        self.tchannel = tchannel
        self.channel_0_0.set_tchannel(self.tchannel)
        self.channel_0.set_tchannel(self.tchannel)

    def get_voltage(self):
        return self.voltage

    def set_voltage(self, voltage):
        self.voltage = voltage
        self.channel_0_0.set_voltage(self.voltage)
        self.channel_0.set_voltage(self.voltage)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
