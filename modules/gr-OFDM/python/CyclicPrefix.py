# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Cyclicprefix
# Author: Maria Camila Herrera Ramos
# Generated: Fri Aug  3 00:38:19 2018
##################################################


from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes


class CyclicPrefix(gr.hier_block2):

    def __init__(self, fft_size=64, paquete_tam=96, rolloff=0, samp_rate=100000):
        gr.hier_block2.__init__(
            self, "Cyclicprefix",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*64),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.fft_size = fft_size
        self.paquete_tam = paquete_tam
        self.rolloff = rolloff
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.length_tag_key = length_tag_key = "paquete_tam"

        ##################################################
        # Blocks
        ##################################################
        self.digital_ofdm_cyclic_prefixer_0 = digital.ofdm_cyclic_prefixer(fft_size, fft_size+fft_size/4, rolloff, length_tag_key)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.05, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self, 0))
        self.connect((self.digital_ofdm_cyclic_prefixer_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self, 0), (self.digital_ofdm_cyclic_prefixer_0, 0))

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_paquete_tam(self):
        return self.paquete_tam

    def set_paquete_tam(self, paquete_tam):
        self.paquete_tam = paquete_tam

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key
