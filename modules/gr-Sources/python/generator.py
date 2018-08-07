# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: generator
# Generated: Thu Aug  2 17:47:55 2018
##################################################


from gnuradio import gr
from gnuradio.filter import firdes
import Generators


class generator(gr.hier_block2):

    def __init__(self, Vector=[1,0,0,0,0,0,0,0]):
        gr.hier_block2.__init__(
            self, "generator",
            gr.io_signature(0, 0, 0),
            gr.io_signature(1, 1, gr.sizeof_float*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.Vector = Vector

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.Generators_sourceVector_0 = Generators.sourceVector((Vector))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Generators_sourceVector_0, 0), (self, 0))

    def get_Vector(self):
        return self.Vector

    def set_Vector(self, Vector):
        self.Vector = Vector
        self.Generators_sourceVector_0.set_invector(self.Vector)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
