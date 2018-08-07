# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: HeaderModulator
# Author: Maria Camila Herrera Ramos
# Generated: Fri Aug  3 00:17:20 2018
##################################################


from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes


class HeaderModulator(gr.hier_block2):

    def __init__(self, length_tag_key="package_size", mod_encabezado=digital.constellation_bpsk(), occupied_carriers=(range(-27, -21) + range(-20, -7) + range(-6, 0) + range(1, 7) + range(8, 21) + range(22, 28),), package_size=96):
        gr.hier_block2.__init__(
            self, "HeaderModulator",
            gr.io_signature(1, 1, gr.sizeof_char*1),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.length_tag_key = length_tag_key
        self.mod_encabezado = mod_encabezado
        self.occupied_carriers = occupied_carriers
        self.package_size = package_size

        ##################################################
        # Variables
        ##################################################
        self.hdr_format = hdr_format = digital.header_format_ofdm(occupied_carriers, 1, length_tag_key,)

        ##################################################
        # Blocks
        ##################################################
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, length_tag_key)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((mod_encabezado.points()), 1)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, package_size, length_tag_key)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, 1, length_tag_key, False, gr.GR_LSB_FIRST)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self, 0), (self.blocks_stream_to_tagged_stream_0, 0))

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key
        self.set_hdr_format(digital.header_format_ofdm(self.occupied_carriers, 1, self.length_tag_key,))

    def get_mod_encabezado(self):
        return self.mod_encabezado

    def set_mod_encabezado(self, mod_encabezado):
        self.mod_encabezado = mod_encabezado

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_hdr_format(digital.header_format_ofdm(self.occupied_carriers, 1, self.length_tag_key,))

    def get_package_size(self):
        return self.package_size

    def set_package_size(self, package_size):
        self.package_size = package_size
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.package_size)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.package_size)

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format
