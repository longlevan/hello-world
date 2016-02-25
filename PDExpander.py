from __future__ import division # Make integer 3/2 give 1.5 in python 2.x
from CoolProp.CoolProp import PropsSI
from math import tan, atan, pi, sin, log
import numpy as np
import time
import warnings

warnings.simplefilter("ignore",RuntimeWarning)
from random import randint, random




class PDExpanderClass():
    def __init__(self,**kwargs):
        # load up the parameters passed in
        # using the dictionary
        self.__dict__.update(kwargs)
    def Update(self,**kwargs):
        # Update the parameters passed in
        # using the dictionary
        self.__dict__.update(kwargs)

    def OutputList(self):
        """
            Return a list of parameters for this components for further output

            It is a list of tuples, and each tuple is formed of items with indices:
                [0] Description of value
                [1] Units of value
                [2] The value itself
        """
        return [
            ('ff_exp','-',self.phi),
            ('eta_exp_ad','-',self.eta_s),
            ('mdot_exp','kg/s',self.m_dot),
            ('power_exp','W',self.W_dot),
            ('torque_exp','N-m',self.tau),
            ('P_exp_su','kPa',self.P_su),
            ('T_exp_ex','C',self.T_ex),
            ('P_exp_ex','kPa',self.P_ex),
            ('v_ratio_exp','-',self.r_v)
        ]

    def Calculate(self):
        # We can provide either supply temperature or supply enthalpy to fix the inlet state of the expander
        if 'h' in self.inputs: # The preferred input is enthalpy
            self.v_su = 1/PropsSI('D','H',self.h_su,'P',self.P_su*1000,self.Ref) # Expander inlet state properties
        elif 'T' in self.inputs:
            self.v_su = 1/PropsSI('D','T',self.T_su+273.15,'P',self.P_su*1000,self.Ref) # Expander inlet state properties
        else:
            raise ValueError('Supply temperature or enthalpy must be specified for this expander object before the Calculate method can execute.')

        rho_su = 1/self.v_su

        "Filling factor"
        self.r_p = self.P_su/self.P_ex

        # compute the filling factor
        p_star = (self.P_su-1000)/1000
        r_star_p = (self.r_p-self.params.rp_ref)/self.params.rp_ref
        rho_star = (rho_su-1000)/1000
        self.phi = self.params.k_1+self.params.k_2*log(self.N/self.params.N_FF_ref)+self.params.k_3*r_star_p+self.params.k_4*p_star+self.params.k_5*rho_star
        # Compute the mass flow rate from filling factor

