# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: channel
# Author: Maria Camila Herrera Ramos
# Generated: Thu Aug  2 18:09:17 2018
##################################################


from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import gr
from gnuradio.filter import firdes
import Multiplexer


class channel(gr.hier_block2):

    def __init__(self, k=4.0, tchannel=1, voltage=0):
        gr.hier_block2.__init__(
            self, "channel",
            gr.io_signature(1, 1, gr.sizeof_float*1),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.k = k
        self.tchannel = tchannel
        self.voltage = voltage

        ##################################################
        # Blocks
        ##################################################
        self.channels_fading_model_0_0 = channels.fading_model( 8, 5/32000, False, 4.0, 0 )
        self.channels_fading_model_0 = channels.fading_model( 8, 5/32000, True, k, 0 )
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, voltage, 0)
        self.Multiplexer_mux_0 = Multiplexer.mux(tchannel)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Multiplexer_mux_0, 0), (self, 0))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.Multiplexer_mux_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.Multiplexer_mux_0, 2))
        self.connect((self.blocks_complex_to_float_0_0_0, 0), (self.Multiplexer_mux_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.channels_fading_model_0_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.channels_fading_model_0, 0))
        self.connect((self.channels_fading_model_0, 0), (self.blocks_complex_to_float_0_0_0, 0))
        self.connect((self.channels_fading_model_0_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self, 0), (self.blocks_add_xx_0, 1))
        self.connect((self, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self, 0), (self.blocks_float_to_complex_0_0, 0))

    def get_k(self):
        return self.k

    def set_k(self, k):
        self.k = k
        self.channels_fading_model_0.set_K(self.k)

    def get_tchannel(self):
        return self.tchannel

    def set_tchannel(self, tchannel):
        self.tchannel = tchannel
        self.Multiplexer_mux_0.set_sel(self.tchannel)

    def get_voltage(self):
        return self.voltage

    def set_voltage(self, voltage):
        self.voltage = voltage
        self.analog_noise_source_x_0.set_amplitude(self.voltage)
