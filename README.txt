"""
ASME ORC 2015
3rd International Seminar on ORC systems
12-14 October 2015, Brussels, Belgium

Example of detailed ORC with regenerator model with subcooling and charge based solvers. The linesets are included
for the charge estimation, but not to evaluate pressure drops between main cycle components.
Minor adjustments can be done inside Cycle.py to account for lineset pressure drops

Ref: D. Ziviani et al. "ORCSIM: A generalized Organic Rankine Cycle Simulation Tool"

"""

To run the simulation code:

Preliminary: Install conda (http://conda.pydata.org/docs/) or equivalent Python

1) Git pull the "ORC--Example" folder from https://github.com/TSTK
2) Install Coolprop for Python: http://coolprop.sourceforge.net/coolprop/wrappers/Python/index.html#python
3) Run the file Cycle_solve.py


Description of the files included:
