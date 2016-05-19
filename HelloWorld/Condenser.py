__author__ = 'Louis Le'
import CoolProp.CoolProp as CP
import CoolProp.Plots as CPP
from CoolProp import AbstractState
from CoolProp.CoolProp import PhaseSI,PropsSI, get_global_param_string
from CoolProp.HumidAirProp import HAPropsSI
import matplotlib.pyplot as plt
import numpy as np

import pint
from pint import UnitRegistry
ureg = UnitRegistry()
#**********************************************************************
# Example 9.3 @ Heat Exchangers: Selection, Rating, and Thermal Design, Third Edition. 2012.
# Design a liquid-liquid heat exchanger
print('********Hot fluid************')
fluid = 'Water'
m_dot_h = 50
T_H_in = (32+273.15)
T_H_out = (25+273.15)
print('*********Cold fluid***********')
m_dot_c = 150
T_C_in = (20+273.15)
print('************Single shell and tube pass heat exchanger************')
D_o = 19e-3
D_i = 16e-3
A_tube_in = np.pi*D_i**2/4
# tubes are laid out on 1 in. square pitch
Pitch_t = 25.4e-3
B_spacing = 0.5
L_max = 8
k_tube = 42.3
R_tot = 0.000176
# Note: surface over design should not exceed 30 percent
A_overdesign = 0.3
u_tube_max = 2

# To solve the problem, first estimate the number of tubes, cold water flow inside tube
rho_C = PropsSI('D','P',101325,'T',T_C_in,fluid)
mu_C = PropsSI('V','P',101325,'T',T_C_in,fluid)
cp_C = PropsSI('C','P',101325,'T',T_C_in,fluid)
k_C = PropsSI('L','P',101325,'T',T_C_in,fluid)
N_t=np.ceil(m_dot_c/(rho_C*u_tube_max*A_tube_in))


# the flow area through the tubes is
A_tubes = A_tube_in*N_t
# Now estimate the shell diameter
CL = 1.0
CTP = 0.93
PR = Pitch_t/D_o
D_shell = np.sqrt(N_t*CL*PR**2*D_o**2/(0.785*CTP))
# the shell diameter should be rounded off as 580 mm
D_shell = 580e-3
print('********First estimation****************')
print('Shell inside diameter :  ',D_shell,'(m)')
print('Number of tubes:         ',N_t,'(tubes)')
print('Tube outside diameter:   ',D_o,'(m)')
print('Tube inside diameter:    ',D_i,'(m)')
print('Baffle spacing:          ',B_spacing,'(m)')
# shell-side heat transfer coefficient
# Kern method
# Estimate the crossflow area at the shell diameter
N_TC = D_shell/Pitch_t
A_shell = (D_shell-N_TC*D_o)*B_spacing
print(A_shell)
# The equivalent diameter can be calculated
D_e = 4*(Pitch_t**2-np.pi*D_o**2/4)/np.pi/D_o
# Calculate the Re
mu_h = PropsSI('V','P',101325,'T',(T_H_in+T_H_out)/2,fluid)
k_h = PropsSI('L','P',101325,'T',(T_H_in+T_H_out)/2,fluid)
cp_h = PropsSI('C','P',101325,'T',(T_H_in+T_H_out)/2,fluid)
Pr = cp_h*mu_h/k_h
Re = m_dot_h/A_shell*D_e/mu_h
print(Re)
# Assuming constant properties, the heat transfer coefficient can be estimated
h_o = 0.36*k_h*Re**0.55*Pr**(1/3)/D_e
print(h_o)
# the tube-side heat transfer coefficient, hi, can be calculated from the petukhov-kirillov correlation
Re_b = rho_C*u_tube_max*D_i/mu_C
Pr_b = cp_C*mu_C/k_C
f_b = (1.58*np.log(Re_b)-3.28)**(-2)
Nu_b = (f_b/2)*Re_b*Pr_b/(1.07+12.7*(f_b/2)**0.5*(Pr_b**(2/3)-1))
print(Nu_b)
h_i = Nu_b*k_C/D_i
print(h_i)
# the overall heat transfer coeffcient for the clean surface is
U_c = (1/h_o+D_o/h_i/D_i+D_o/2*np.log(D_o/D_i)/k_tube)**(-1)
print(U_c)
# and for the fouled surface is
U_f = (1/U_c+R_tot)**(-1)
print(U_f)
T_C_out = m_dot_h*cp_h*(T_H_in-T_H_out)/(m_dot_c*cp_C)+T_C_in
print(T_C_out)
DT_1 = T_H_in-T_C_out
DT_2 = T_H_out-T_C_in
LMTD = (DT_1-DT_2)/np.log(DT_1/DT_2)
print(LMTD)
Q_dot = m_dot_h*cp_h*(T_H_in-T_H_out)
A_f = Q_dot/U_f/LMTD
A_c = Q_dot/U_c/LMTD
# the over surface design is
OS = A_f/A_c
# which is the clean vs fouling safety factor. the over surface design should not be more than about 30 percent. Assuming 20 percent surface
# over design, the cleaning scheduling must be arranged according by
U_f = 1.2*U_c

# the corresponding total resistance cand be calculated as follow
R_tot = 1/U_f-1/U_c
# For 20 percent over surface design, the surface area of the exchanger becomes
A_f = 1.2*A_c
print(A_f,A_c,Q_dot,U_f)
# the length of the heat exchanger is calculated as follows
L = A_f/N_t/np.pi/D_o
L = 5
print(L)
# which is rounded to L = 5 m
# the shell diameter can be recalculate
D_shell = np.sqrt(N_t*CL*PR**2*D_o**2/(0.785*CTP))
print(D_shell)


"""
Some lines from CMIDataProcessing project
Zone3to10_Density = []

for i in range(len(Data1_TT_1301)):
    Zone3to10_Density.append(PropsSI('D','P',1e5,'T',Data1_TT_1301['TT_0301.OUT ValueY'][i],'Air'))

Zone3to10_Density = DataFrame(Zone3to10_Density)
print(Zone3to10_Density)

Zone1to2_Density = []
for i in range(len(Data1_TT_0101)):
    Zone1to2_Density.append(PropsSI('D','P',1e5,'T',Data1_TT_0101['TT_0101.OUT ValueY'][i],'Air'))

Zone1to2_Density = DataFrame(Zone1to2_Density)

plt.plot(Zone1to2_Density)
plt.show()
"""



