# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: PilotSymbols
# Author: Maria Camila Herrera Ramos
# Generated: Fri Aug  3 00:28:04 2018
##################################################


from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes


class PilotSymbols(gr.hier_block2):

    def __init__(self, fft_size=64, occupied_carriers=(range(-26, -21) + range(-20, -7) + range(-6, 0) + range(1, 7) + range(8, 21) + range(22, 27),), pilot_carriers=((-21, -7, 7, 21,),), pilot_symbols=((1, 1, 1, -1,),)):
        gr.hier_block2.__init__(
            self, "PilotSymbols",
            gr.io_signaturev(2, 2, [gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1]),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*64),
        )

        ##################################################
        # Parameters
        ##################################################
        self.fft_size = fft_size
        self.occupied_carriers = occupied_carriers
        self.pilot_carriers = pilot_carriers
        self.pilot_symbols = pilot_symbols

        ##################################################
        # Variables
        ##################################################
        self.word_sync2 = word_sync2 = [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0]
        self.word_sync1 = word_sync1 = [0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.]
        self.paquete_tam = paquete_tam = 96
        self.length_tag_key = length_tag_key = "paquete_tam"

        ##################################################
        # Blocks
        ##################################################
        self.digital_ofdm_carrier_allocator_cvc_0 = digital.ofdm_carrier_allocator_cvc(fft_size, occupied_carriers, pilot_carriers, pilot_symbols, (word_sync1,word_sync2), length_tag_key)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, length_tag_key, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_ofdm_carrier_allocator_cvc_0, 0))
        self.connect((self.digital_ofdm_carrier_allocator_cvc_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self, 1), (self.blocks_tagged_stream_mux_0, 1))

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols

    def get_word_sync2(self):
        return self.word_sync2

    def set_word_sync2(self, word_sync2):
        self.word_sync2 = word_sync2

    def get_word_sync1(self):
        return self.word_sync1

    def set_word_sync1(self, word_sync1):
        self.word_sync1 = word_sync1

    def get_paquete_tam(self):
        return self.paquete_tam

    def set_paquete_tam(self, paquete_tam):
        self.paquete_tam = paquete_tam

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key
