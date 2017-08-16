"""
The diet problem

The goal of the Diet problem is to select foods that satisfy daily nutritional requirements at minimum cost.
This problem can be formulated as a linear program, for which constraints limit the number of calories and the amount
of vitamins, minerals, fats, sodium and cholesterol in the diet.

Problem statement
The Diet problem can be formulared mathematically as a linear programming problem using the following model
"""
from pyomo.environ import *
infinity = float('inf')
model=AbstractModel()

# Foods
model.F = set()
# Nutrients
model.N = set()

