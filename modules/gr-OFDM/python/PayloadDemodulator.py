# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: PayloadDemodulator
# Author: Maria Camila Herrera Ramos
# Generated: Fri Aug  3 00:58:13 2018
##################################################


from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes


class PayloadDemodulator(gr.hier_block2):

    def __init__(self, fft_tam=64, length_tag_key="paquete_tam", occupied_carriers=(range(-26, -21) + range(-20, -7) + range(-6, 0) + range(1, 7) + range(8, 21) + range(22, 27),), paquete_tam=96, payload_mod=digital.constellation_bpsk(), pilot_carriers=((-21, -7, 7, 21,),), pilot_symbols=((1, 1, 1, -1,),)):
        gr.hier_block2.__init__(
            self, "PayloadDemodulator",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*64),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.fft_tam = fft_tam
        self.length_tag_key = length_tag_key
        self.occupied_carriers = occupied_carriers
        self.paquete_tam = paquete_tam
        self.payload_mod = payload_mod
        self.pilot_carriers = pilot_carriers
        self.pilot_symbols = pilot_symbols

        ##################################################
        # Variables
        ##################################################
        self.payload_equalizer = payload_equalizer = digital.ofdm_equalizer_simpledfe(fft_tam, payload_mod.base(), occupied_carriers, pilot_carriers, pilot_symbols, 1)
        self.packet_length_tag_key = packet_length_tag_key = "paquete_tam"

        ##################################################
        # Blocks
        ##################################################
        self.digital_ofdm_serializer_vcc_payload = digital.ofdm_serializer_vcc(fft_tam, occupied_carriers, length_tag_key, packet_length_tag_key, 1, '', True)
        self.digital_ofdm_frame_equalizer_vcvc_1 = digital.ofdm_frame_equalizer_vcvc(payload_equalizer.base(), fft_tam/4, length_tag_key, True, 0)
        self.digital_constellation_decoder_cb_1 = digital.constellation_decoder_cb(payload_mod.base())
        self.blocks_uchar_to_float_0_0 = blocks.uchar_to_float()
        self.blocks_repack_bits_bb_0_1 = blocks.repack_bits_bb(payload_mod.bits_per_symbol(), 8, packet_length_tag_key, True, gr.GR_LSB_FIRST)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.blocks_uchar_to_float_0_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0, 0), (self, 0))
        self.connect((self.digital_constellation_decoder_cb_1, 0), (self.blocks_repack_bits_bb_0_1, 0))
        self.connect((self.digital_ofdm_frame_equalizer_vcvc_1, 0), (self.digital_ofdm_serializer_vcc_payload, 0))
        self.connect((self.digital_ofdm_serializer_vcc_payload, 0), (self.digital_constellation_decoder_cb_1, 0))
        self.connect((self, 0), (self.digital_ofdm_frame_equalizer_vcvc_1, 0))

    def get_fft_tam(self):
        return self.fft_tam

    def set_fft_tam(self, fft_tam):
        self.fft_tam = fft_tam
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_tam, payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_tam, payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))

    def get_paquete_tam(self):
        return self.paquete_tam

    def set_paquete_tam(self, paquete_tam):
        self.paquete_tam = paquete_tam

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_tam, payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_tam, payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 1))

    def get_payload_equalizer(self):
        return self.payload_equalizer

    def set_payload_equalizer(self, payload_equalizer):
        self.payload_equalizer = payload_equalizer

    def get_packet_length_tag_key(self):
        return self.packet_length_tag_key

    def set_packet_length_tag_key(self, packet_length_tag_key):
        self.packet_length_tag_key = packet_length_tag_key
