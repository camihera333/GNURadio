#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
import math
from gnuradio import gr
import numpy as np
from random import randint
class frecSynthesizer(gr.sync_block):
    """
    docstring for block tabfrec_py_nf
    """
    def __init__(self, fc,fd,bps,tam_info):
        gr.sync_block.__init__(self,
            name="frecSynthesizer",
            in_sig=None,
            out_sig=[numpy.float32])
        self.set_output_multiple(8192)
        self.bps=bps
        self.fc=fc
        self.fd=fd
        self.tam_info=tam_info
        self.frec=2**self.bps
        self.tampfrec=8192/self.frec
        self.ban=0
    def set_bps(self,bps):
        self.bps=bps
        self.frec=2**self.bps
        self.tampfrec=8192/self.frec
        self.ban=0
    def set_fc(self,fc):
        self.fc=fc
        self.ban=0
    def set_fd(self,fd):
        self.fd=fd
        self.ban=0
    def set_tam_info(self,tam_info):
        self.tam_info=tam_info
        self.ban=0
    def cos(self,arg):
        sal=[]
        for i in range(len(arg)):
            sal.append(10*math.cos(arg[i]))
        return sal
    def bitodec(self,a):
        b=[]
        for i in range(len(a)):
            b.append(str(int(a[i])))
        c=""
        c=c.join(b)
        c=int(c,2)
        return c
    def walsh(self,z):
        if (z==1):
            aux=0
        elif (z==2):
            aux=1
        elif(z==4):
            aux=2
        elif (z==8):
            aux=3
        elif (z==16):
            aux=4

        w1=[1]
        w2=[[1,1],[1,-1]]
        w2=np.matrix(w2)
        w3=np.concatenate((np.concatenate((w2,w2)).transpose(),np.concatenate((w2,-w2)).transpose()))
        w4=np.concatenate((np.concatenate((w3,w3)).transpose(),np.concatenate((w3,-w3)).transpose()))
        w5=np.concatenate((np.concatenate((w4,w4)).transpose(),np.concatenate((w4,-w4)).transpose()))
        w=[w1,w2,w3,w4,w5]
        fi=randint(1,z-1)
        c=w[aux][fi,:]
        return(c)
    def walshtotal(self,totaltam):
        if totaltam==16:
            z=8
            codpn1=list(self.walsh(z))
            codpn2=list(self.walsh(z))
            codpn=np.concatenate((codpn1,codpn2),axis=2)
            codpn=codpn[0][0]
        elif totaltam==24:
            z=16
            codpn1=list(self.walsh(z))
            z=8
            codpn2=list(self.walsh(z))
            codpn=np.concatenate((codpn1,codpn2),axis=2)
            codpn=codpn[0][0]
        elif totaltam==32:
            z=16
            codpn1=list(self.walsh(z))
            codpn2=list(self.walsh(z))
            codpn=np.concatenate((codpn1,codpn2),axis=2)
            codpn=codpn[0][0]
        elif totaltam==48:
            z=16
            codpn1=list(self.walsh(z))
            codpn2=list(self.walsh(z))
            codpn3=list(self.walsh(z))
            codpn=np.concatenate((codpn1,codpn2,codpn3),axis=2)
            codpn=codpn[0][0]
        elif totaltam==64:
            z=16
            codpn1=list(self.walsh(z))
            codpn2=list(self.walsh(z))
            codpn3=list(self.walsh(z))
            codpn4=list(self.walsh(z))
            codpn=np.concatenate((codpn1,codpn2,codpn3,codpn4),axis=2)
            codpn=codpn[0][0]
        return(codpn)
    def work(self, input_items, output_items):
        out = output_items[0]
        # <+signal processing here+>
        if self.ban==0:
            ts=1/32000
            fs=32000
            self.totaltam=self.bps*self.tam_info
            codpn=self.walshtotal(self.totaltam)
            codpn=(codpn+1)/2
            fi=[]
            for i in range(1,self.frec+1):
                fi.append(self.fc+((2*i)-1-self.frec)*self.fd)
            fi=numpy.array(fi)
            tf=8192*float(1.0/fs)
            tpf=tf/self.tam_info
            t=numpy.linspace(0,tpf,8192/self.tam_info)
            signale=[]
            for j in range(self.tam_info):
                bina=codpn[j*self.bps:(j*self.bps)+self.bps]
                val=self.bitodec(bina)
                fpn=fi[val]
                portadora=self.cos(2*math.pi*fpn*t)
                signale.append(portadora)
            self.signale=signale
            self.ban=1
        i=0
        var=int(8192/self.tam_info)
        for c in range(0,8192,var):
            out[c:c+var]=numpy.array(self.signale[i])
            i=i+1
        return len(output_items[0])
