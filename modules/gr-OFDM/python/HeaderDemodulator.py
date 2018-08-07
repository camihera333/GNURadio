# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: HeaderDemodulator
# Author: Maria Camila Herrera Ramos
# Generated: Fri Aug  3 00:53:16 2018
##################################################


from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes


class HeaderDemodulator(gr.hier_block2):

    def __init__(self, fft_tam=64, mod_encabezado=digital.constellation_bpsk(), occupied_carriers=(range(-26, -21) + range(-20, -7) + range(-6, 0) + range(1, 7) + range(8, 21) + range(22, 27),), pilot_carriers=((-21, -7, 7, 21,),), pilot_symbols=((1, 1, 1, -1,),)):
        gr.hier_block2.__init__(
            self, "HeaderDemodulator",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*64),
            gr.io_signature(1, 1, gr.sizeof_char*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.fft_tam = fft_tam
        self.mod_encabezado = mod_encabezado
        self.occupied_carriers = occupied_carriers
        self.pilot_carriers = pilot_carriers
        self.pilot_symbols = pilot_symbols

        ##################################################
        # Variables
        ##################################################
        self.paquete_tam = paquete_tam = 96
        self.palabra_sinc2 = palabra_sinc2 = [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0]
        self.palabra_sinc1 = palabra_sinc1 = [0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.]
        self.packet_length_tag_key = packet_length_tag_key = "paquete_tam"
        self.length_tag_key = length_tag_key = "paquete_tam"
        self.header_equalizer = header_equalizer = digital.ofdm_equalizer_simpledfe(fft_tam, mod_encabezado.base(), occupied_carriers, pilot_carriers, pilot_symbols)

        ##################################################
        # Blocks
        ##################################################
        self.digital_ofdm_serializer_vcc_header_0 = digital.ofdm_serializer_vcc(fft_tam, occupied_carriers, length_tag_key, '', 0, '', True)
        self.digital_ofdm_frame_equalizer_vcvc_0_0 = digital.ofdm_frame_equalizer_vcvc(header_equalizer.base(), fft_tam/4, length_tag_key, True, 1)
        self.digital_ofdm_chanest_vcvc_0_0 = digital.ofdm_chanest_vcvc((palabra_sinc1), (palabra_sinc2), 1, 0, 3, False)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(mod_encabezado.base())

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self, 0))
        self.connect((self.digital_ofdm_chanest_vcvc_0_0, 0), (self.digital_ofdm_frame_equalizer_vcvc_0_0, 0))
        self.connect((self.digital_ofdm_frame_equalizer_vcvc_0_0, 0), (self.digital_ofdm_serializer_vcc_header_0, 0))
        self.connect((self.digital_ofdm_serializer_vcc_header_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self, 0), (self.digital_ofdm_chanest_vcvc_0_0, 0))

    def get_fft_tam(self):
        return self.fft_tam

    def set_fft_tam(self, fft_tam):
        self.fft_tam = fft_tam
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_tam, mod_encabezado.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))

    def get_mod_encabezado(self):
        return self.mod_encabezado

    def set_mod_encabezado(self, mod_encabezado):
        self.mod_encabezado = mod_encabezado

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_tam, mod_encabezado.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_tam, mod_encabezado.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_tam, mod_encabezado.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols))

    def get_paquete_tam(self):
        return self.paquete_tam

    def set_paquete_tam(self, paquete_tam):
        self.paquete_tam = paquete_tam

    def get_palabra_sinc2(self):
        return self.palabra_sinc2

    def set_palabra_sinc2(self, palabra_sinc2):
        self.palabra_sinc2 = palabra_sinc2

    def get_palabra_sinc1(self):
        return self.palabra_sinc1

    def set_palabra_sinc1(self, palabra_sinc1):
        self.palabra_sinc1 = palabra_sinc1

    def get_packet_length_tag_key(self):
        return self.packet_length_tag_key

    def set_packet_length_tag_key(self, packet_length_tag_key):
        self.packet_length_tag_key = packet_length_tag_key

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key

    def get_header_equalizer(self):
        return self.header_equalizer

    def set_header_equalizer(self, header_equalizer):
        self.header_equalizer = header_equalizer
