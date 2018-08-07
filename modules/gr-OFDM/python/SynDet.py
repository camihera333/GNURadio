# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: SynDet
# Author: Maria Camila Herrera Ramos
# Generated: Fri Aug  3 00:43:40 2018
##################################################


from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes


class SynDet(gr.hier_block2):

    def __init__(self, fft_tam=64):
        gr.hier_block2.__init__(
            self, "SynDet",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signaturev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_char*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.fft_tam = fft_tam

        ##################################################
        # Blocks
        ##################################################
        self.digital_ofdm_sync_sc_cfb_0 = digital.ofdm_sync_sc_cfb(fft_tam, fft_tam/4, False)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, fft_tam+fft_tam/4)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(-2.0/fft_tam)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self, 0))
        self.connect((self.digital_ofdm_sync_sc_cfb_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.digital_ofdm_sync_sc_cfb_0, 1), (self, 1))
        self.connect((self, 0), (self.blocks_delay_0, 0))
        self.connect((self, 0), (self.digital_ofdm_sync_sc_cfb_0, 0))

    def get_fft_tam(self):
        return self.fft_tam

    def set_fft_tam(self, fft_tam):
        self.fft_tam = fft_tam
        self.blocks_delay_0.set_dly(self.fft_tam+self.fft_tam/4)
        self.analog_frequency_modulator_fc_0.set_sensitivity(-2.0/self.fft_tam)
