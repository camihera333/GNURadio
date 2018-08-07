# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: PayloadModulator
# Author: Maria Camila Herrera Ramos
# Generated: Fri Aug  3 00:17:17 2018
##################################################


from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes


class PayloadModulator(gr.hier_block2):

    def __init__(self, length_tag_key="package_size", package_size=96, payload_mod=digital.constellation_bpsk()):
        gr.hier_block2.__init__(
            self, "PayloadModulator",
            gr.io_signature(1, 1, gr.sizeof_char*1),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.length_tag_key = length_tag_key
        self.package_size = package_size
        self.payload_mod = payload_mod

        ##################################################
        # Blocks
        ##################################################
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((payload_mod.points()), 1)
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, package_size, length_tag_key)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, payload_mod.bits_per_symbol(), length_tag_key, False, gr.GR_LSB_FIRST)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key

    def get_package_size(self):
        return self.package_size

    def set_package_size(self, package_size):
        self.package_size = package_size
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len(self.package_size)
        self.blocks_stream_to_tagged_stream_0_0.set_packet_len_pmt(self.package_size)

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod
