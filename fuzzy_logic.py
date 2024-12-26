"""
This module provides the code for the fuzzy logic model.
The model takes percentage of fiber (fibre), liquid limit (liquid_limit) and
Optimum moisture content (omc) as input and California Bearing
ratio (cbr) as output.
"""

import numpy as np
import os
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from matplotlib import pyplot as plt

# linguistic variables
fibre = ctrl.Antecedent(np.arange(0, 1.75, 0.25), "F")
liquid_limit = ctrl.Antecedent(np.arange(46.2, 82.6,), "LL")
omc = ctrl.Antecedent(np.arange(22, 36.2), "OMC")
cbr = ctrl.Consequent(np.arange(15.9, 26.6), "CBR")

# membership functions
fibre['F1'] = fuzz.trimf(fibre.universe, [-0.25, 0, 0.25])
fibre['F2'] = fuzz.trimf(fibre.universe, [0, 0.25, 0.5])
fibre['F3'] = fuzz.trimf(fibre.universe, [0.25, 0.5, 0.75])
fibre['F4'] = fuzz.trimf(fibre.universe, [0.5, 0.75, 1])
fibre['F5'] = fuzz.trimf(fibre.universe, [0.75, 1, 1.25])
fibre['F6'] = fuzz.trimf(fibre.universe, [1, 1.25, 1.5])
fibre['F7'] = fuzz.trimf(fibre.universe, [1.25, 1.5, 1.75])


liquid_limit['LL1'] = fuzz.trimf(liquid_limit.universe, [40.11, 46.2, 52.29])
liquid_limit['LL2'] = fuzz.trimf(liquid_limit.universe, [46.2, 52.29, 58.31])
liquid_limit['LL3'] = fuzz.trimf(liquid_limit.universe, [52.29, 58.31, 64.4])
liquid_limit['LL4'] = fuzz.trimf(liquid_limit.universe, [58.31, 64.4, 70.49])
liquid_limit['LL5'] = fuzz.trimf(liquid_limit.universe, [65.46, 71.55, 77.57])
liquid_limit['LL6'] = fuzz.trimf(liquid_limit.universe, [70.49, 76.51, 82.6])
liquid_limit['LL7'] = fuzz.trimf(liquid_limit.universe, [76.51, 82.6, 88.69])


omc['OMC1'] = fuzz.trimf(omc.universe, [19.64, 22, 24.36])
omc['OMC2'] = fuzz.trimf(omc.universe, [22, 24.36, 26.74])
omc['OMC3'] = fuzz.trimf(omc.universe, [24.36, 26.74, 29.1])
omc['OMC4'] = fuzz.trimf(omc.universe, [26.74, 29.1, 31.46])
omc['OMC5'] = fuzz.trimf(omc.universe, [29.1, 31.46, 33.84])
omc['OMC6'] = fuzz.trimf(omc.universe, [31.46, 33.84, 36.2])
omc['OMC7'] = fuzz.trimf(omc.universe, [33.84, 36.2, 38.56])


cbr['CBR1'] = fuzz.trimf(cbr.universe, [14.12, 15.9, 17.68])
cbr['CBR2'] = fuzz.trimf(cbr.universe, [15.9, 17.68, 19.47])
cbr['CBR3'] = fuzz.trimf(cbr.universe, [17.68, 19.47, 21.25])
cbr['CBR4'] = fuzz.trimf(cbr.universe, [19.47, 21.25, 23.03])
cbr['CBR5'] = fuzz.trimf(cbr.universe, [21.25, 23.03, 24.82])
cbr['CBR6'] = fuzz.trimf(cbr.universe, [23.03, 24.82, 26.6])
cbr['CBR7'] = fuzz.trimf(cbr.universe, [24.82, 26.6, 28.38])


# fuzzy rules
rule1 = ctrl.Rule(fibre['F1'] & liquid_limit['LL1'] & omc['OMC1'], cbr['CBR7'])
rule2 = ctrl.Rule(fibre['F1'] & liquid_limit['LL1'] & omc['OMC2'], cbr['CBR7'])
rule3 = ctrl.Rule(fibre['F1'] & liquid_limit['LL1'] & omc['OMC3'], cbr['CBR7'])
rule4 = ctrl.Rule(fibre['F1'] & liquid_limit['LL1'] & omc['OMC4'], cbr['CBR6'])
rule5 = ctrl.Rule(fibre['F1'] & liquid_limit['LL1'] & omc['OMC5'], cbr['CBR6'])
rule6 = ctrl.Rule(fibre['F1'] & liquid_limit['LL1'] & omc['OMC6'], cbr['CBR5'])
rule7 = ctrl.Rule(fibre['F1'] & liquid_limit['LL1'] & omc['OMC7'], cbr['CBR5'])
rule8 = ctrl.Rule(fibre['F1'] & liquid_limit['LL2'] & omc['OMC1'], cbr['CBR6'])
rule9 = ctrl.Rule(fibre['F1'] & liquid_limit['LL2'] & omc['OMC2'], cbr['CBR6'])
rule10 = ctrl.Rule(fibre['F1'] & liquid_limit['LL2'] & omc['OMC3'], cbr['CBR5'])
rule11 = ctrl.Rule(fibre['F1'] & liquid_limit['LL2'] & omc['OMC4'], cbr['CBR5'])
rule12 = ctrl.Rule(fibre['F1'] & liquid_limit['LL2'] & omc['OMC5'], cbr['CBR4'])
rule13 = ctrl.Rule(fibre['F1'] & liquid_limit['LL2'] & omc['OMC6'], cbr['CBR4'])
rule14 = ctrl.Rule(fibre['F1'] & liquid_limit['LL2'] & omc['OMC7'], cbr['CBR3'])
rule15 = ctrl.Rule(fibre['F1'] & liquid_limit['LL3'] & omc['OMC1'], cbr['CBR5'])
rule16 = ctrl.Rule(fibre['F1'] & liquid_limit['LL3'] & omc['OMC2'], cbr['CBR5'])
rule17 = ctrl.Rule(fibre['F1'] & liquid_limit['LL3'] & omc['OMC3'], cbr['CBR4'])
rule18 = ctrl.Rule(fibre['F1'] & liquid_limit['LL3'] & omc['OMC4'], cbr['CBR4'])
rule19 = ctrl.Rule(fibre['F1'] & liquid_limit['LL3'] & omc['OMC5'], cbr['CBR3'])
rule20 = ctrl.Rule(fibre['F1'] & liquid_limit['LL3'] & omc['OMC6'], cbr['CBR3'])
rule21 = ctrl.Rule(fibre['F1'] & liquid_limit['LL3'] & omc['OMC7'], cbr['CBR2'])
rule22 = ctrl.Rule(fibre['F1'] & liquid_limit['LL4'] & omc['OMC1'], cbr['CBR4'])
rule23 = ctrl.Rule(fibre['F1'] & liquid_limit['LL4'] & omc['OMC2'], cbr['CBR4'])
rule24 = ctrl.Rule(fibre['F1'] & liquid_limit['LL4'] & omc['OMC3'], cbr['CBR3'])
rule25 = ctrl.Rule(fibre['F1'] & liquid_limit['LL5'] & omc['OMC1'], cbr['CBR3'])
rule26 = ctrl.Rule(fibre['F1'] & liquid_limit['LL5'] & omc['OMC2'], cbr['CBR3'])
rule27 = ctrl.Rule(fibre['F1'] & liquid_limit['LL5'] & omc['OMC3'], cbr['CBR3'])
rule28 = ctrl.Rule(fibre['F1'] & liquid_limit['LL5'] & omc['OMC4'], cbr['CBR2'])
rule29 = ctrl.Rule(fibre['F1'] & liquid_limit['LL5'] & omc['OMC5'], cbr['CBR2'])
rule30 = ctrl.Rule(fibre['F1'] & liquid_limit['LL5'] & omc['OMC6'], cbr['CBR2'])
rule31 = ctrl.Rule(fibre['F1'] & liquid_limit['LL5'] & omc['OMC7'], cbr['CBR1'])
rule32 = ctrl.Rule(fibre['F1'] & liquid_limit['LL6'] & omc['OMC1'], cbr['CBR2'])
rule33 = ctrl.Rule(fibre['F1'] & liquid_limit['LL6'] & omc['OMC2'], cbr['CBR2'])
rule34 = ctrl.Rule(fibre['F1'] & liquid_limit['LL6'] & omc['OMC3'], cbr['CBR2'])
rule35 = ctrl.Rule(fibre['F1'] & liquid_limit['LL6'] & omc['OMC4'], cbr['CBR2'])
rule36 = ctrl.Rule(fibre['F1'] & liquid_limit['LL6'] & omc['OMC5'], cbr['CBR1'])
rule37 = ctrl.Rule(fibre['F1'] & liquid_limit['LL6'] & omc['OMC6'], cbr['CBR1'])
rule38 = ctrl.Rule(fibre['F1'] & liquid_limit['LL6'] & omc['OMC7'], cbr['CBR1'])
rule39 = ctrl.Rule(fibre['F2'] & liquid_limit['LL1'] & omc['OMC1'], cbr['CBR7'])
rule40 = ctrl.Rule(fibre['F2'] & liquid_limit['LL1'] & omc['OMC2'], cbr['CBR7'])
rule41 = ctrl.Rule(fibre['F2'] & liquid_limit['LL1'] & omc['OMC3'], cbr['CBR6'])
rule42 = ctrl.Rule(fibre['F2'] & liquid_limit['LL1'] & omc['OMC4'], cbr['CBR6'])
rule43 = ctrl.Rule(fibre['F2'] & liquid_limit['LL1'] & omc['OMC5'], cbr['CBR5'])
rule44 = ctrl.Rule(fibre['F2'] & liquid_limit['LL1'] & omc['OMC6'], cbr['CBR5'])
rule45 = ctrl.Rule(fibre['F2'] & liquid_limit['LL1'] & omc['OMC7'], cbr['CBR4'])
rule46 = ctrl.Rule(fibre['F2'] & liquid_limit['LL2'] & omc['OMC1'], cbr['CBR6'])
rule47 = ctrl.Rule(fibre['F2'] & liquid_limit['LL2'] & omc['OMC2'], cbr['CBR6'])
rule48 = ctrl.Rule(fibre['F2'] & liquid_limit['LL2'] & omc['OMC3'], cbr['CBR5'])
rule49 = ctrl.Rule(fibre['F2'] & liquid_limit['LL2'] & omc['OMC4'], cbr['CBR5'])
rule50 = ctrl.Rule(fibre['F2'] & liquid_limit['LL2'] & omc['OMC5'], cbr['CBR4'])
rule51 = ctrl.Rule(fibre['F2'] & liquid_limit['LL2'] & omc['OMC6'], cbr['CBR4'])
rule52 = ctrl.Rule(fibre['F2'] & liquid_limit['LL2'] & omc['OMC7'], cbr['CBR3'])
rule53 = ctrl.Rule(fibre['F2'] & liquid_limit['LL3'] & omc['OMC1'], cbr['CBR6'])
rule54 = ctrl.Rule(fibre['F2'] & liquid_limit['LL3'] & omc['OMC2'], cbr['CBR6'])
rule55 = ctrl.Rule(fibre['F2'] & liquid_limit['LL3'] & omc['OMC3'], cbr['CBR6'])
rule56 = ctrl.Rule(fibre['F2'] & liquid_limit['LL3'] & omc['OMC4'], cbr['CBR5'])
rule57 = ctrl.Rule(fibre['F2'] & liquid_limit['LL3'] & omc['OMC5'], cbr['CBR5'])
rule58 = ctrl.Rule(fibre['F2'] & liquid_limit['LL3'] & omc['OMC6'], cbr['CBR4'])
rule59 = ctrl.Rule(fibre['F2'] & liquid_limit['LL3'] & omc['OMC7'], cbr['CBR4'])
rule60 = ctrl.Rule(fibre['F2'] & liquid_limit['LL4'] & omc['OMC1'], cbr['CBR6'])
rule61 = ctrl.Rule(fibre['F2'] & liquid_limit['LL4'] & omc['OMC2'], cbr['CBR6'])
rule62 = ctrl.Rule(fibre['F2'] & liquid_limit['LL4'] & omc['OMC3'], cbr['CBR5'])
rule63 = ctrl.Rule(fibre['F2'] & liquid_limit['LL4'] & omc['OMC4'], cbr['CBR5'])
rule64 = ctrl.Rule(fibre['F2'] & liquid_limit['LL4'] & omc['OMC5'], cbr['CBR4'])
rule65 = ctrl.Rule(fibre['F2'] & liquid_limit['LL4'] & omc['OMC6'], cbr['CBR4'])
rule66 = ctrl.Rule(fibre['F2'] & liquid_limit['LL4'] & omc['OMC7'], cbr['CBR3'])
rule67 = ctrl.Rule(fibre['F2'] & liquid_limit['LL5'] & omc['OMC1'], cbr['CBR5'])
rule68 = ctrl.Rule(fibre['F2'] & liquid_limit['LL5'] & omc['OMC2'], cbr['CBR5'])
rule69 = ctrl.Rule(fibre['F2'] & liquid_limit['LL5'] & omc['OMC3'], cbr['CBR4'])
rule70 = ctrl.Rule(fibre['F2'] & liquid_limit['LL5'] & omc['OMC4'], cbr['CBR4'])
rule71 = ctrl.Rule(fibre['F2'] & liquid_limit['LL5'] & omc['OMC5'], cbr['CBR3'])
rule72 = ctrl.Rule(fibre['F2'] & liquid_limit['LL5'] & omc['OMC6'], cbr['CBR3'])
rule73 = ctrl.Rule(fibre['F2'] & liquid_limit['LL5'] & omc['OMC7'], cbr['CBR3'])
rule74 = ctrl.Rule(fibre['F2'] & liquid_limit['LL6'] & omc['OMC1'], cbr['CBR4'])
rule75 = ctrl.Rule(fibre['F2'] & liquid_limit['LL6'] & omc['OMC2'], cbr['CBR4'])
rule76 = ctrl.Rule(fibre['F2'] & liquid_limit['LL6'] & omc['OMC3'], cbr['CBR3'])
rule77 = ctrl.Rule(fibre['F2'] & liquid_limit['LL6'] & omc['OMC4'], cbr['CBR3'])
rule78 = ctrl.Rule(fibre['F2'] & liquid_limit['LL6'] & omc['OMC5'], cbr['CBR4'])
rule79 = ctrl.Rule(fibre['F2'] & liquid_limit['LL6'] & omc['OMC6'], cbr['CBR4'])
rule80 = ctrl.Rule(fibre['F2'] & liquid_limit['LL6'] & omc['OMC7'], cbr['CBR4'])
rule81 = ctrl.Rule(fibre['F2'] & liquid_limit['LL7'] & omc['OMC1'], cbr['CBR3'])
rule82 = ctrl.Rule(fibre['F2'] & liquid_limit['LL7'] & omc['OMC2'], cbr['CBR3'])
rule83 = ctrl.Rule(fibre['F2'] & liquid_limit['LL7'] & omc['OMC3'], cbr['CBR3'])
rule84 = ctrl.Rule(fibre['F2'] & liquid_limit['LL7'] & omc['OMC4'], cbr['CBR2'])
rule85 = ctrl.Rule(fibre['F2'] & liquid_limit['LL7'] & omc['OMC5'], cbr['CBR2'])
rule86 = ctrl.Rule(fibre['F2'] & liquid_limit['LL7'] & omc['OMC6'], cbr['CBR1'])
rule87 = ctrl.Rule(fibre['F2'] & liquid_limit['LL7'] & omc['OMC6'], cbr['CBR1'])
rule88 = ctrl.Rule(fibre['F3'] & liquid_limit['LL1'] & omc['OMC1'], cbr['CBR6'])
rule89 = ctrl.Rule(fibre['F3'] & liquid_limit['LL1'] & omc['OMC2'], cbr['CBR6'])
rule90 = ctrl.Rule(fibre['F3'] & liquid_limit['LL1'] & omc['OMC3'], cbr['CBR5'])
rule91 = ctrl.Rule(fibre['F3'] & liquid_limit['LL1'] & omc['OMC4'], cbr['CBR5'])
rule92 = ctrl.Rule(fibre['F3'] & liquid_limit['LL1'] & omc['OMC5'], cbr['CBR4'])
rule93 = ctrl.Rule(fibre['F3'] & liquid_limit['LL1'] & omc['OMC6'], cbr['CBR4'])
rule94 = ctrl.Rule(fibre['F3'] & liquid_limit['LL1'] & omc['OMC7'], cbr['CBR3'])
rule95 = ctrl.Rule(fibre['F3'] & liquid_limit['LL2'] & omc['OMC1'], cbr['CBR6'])
rule96 = ctrl.Rule(fibre['F3'] & liquid_limit['LL2'] & omc['OMC2'], cbr['CBR6'])
rule97 = ctrl.Rule(fibre['F3'] & liquid_limit['LL2'] & omc['OMC3'], cbr['CBR5'])
rule98 = ctrl.Rule(fibre['F3'] & liquid_limit['LL2'] & omc['OMC4'], cbr['CBR5'])
rule99 = ctrl.Rule(fibre['F3'] & liquid_limit['LL2'] & omc['OMC5'], cbr['CBR5'])
rule100 = ctrl.Rule(fibre['F3'] & liquid_limit['LL2'] & omc['OMC6'], cbr['CBR4'])
rule101 = ctrl.Rule(fibre['F3'] & liquid_limit['LL2'] & omc['OMC7'], cbr['CBR4'])
rule102 = ctrl.Rule(fibre['F3'] & liquid_limit['LL3'] & omc['OMC1'], cbr['CBR5'])
rule103 = ctrl.Rule(fibre['F3'] & liquid_limit['LL3'] & omc['OMC2'], cbr['CBR5'])
rule104 = ctrl.Rule(fibre['F3'] & liquid_limit['LL3'] & omc['OMC3'], cbr['CBR4'])
rule105 = ctrl.Rule(fibre['F3'] & liquid_limit['LL3'] & omc['OMC4'], cbr['CBR4'])
rule106 = ctrl.Rule(fibre['F3'] & liquid_limit['LL3'] & omc['OMC5'], cbr['CBR4'])
rule107 = ctrl.Rule(fibre['F3'] & liquid_limit['LL3'] & omc['OMC6'], cbr['CBR3'])
rule108 = ctrl.Rule(fibre['F3'] & liquid_limit['LL3'] & omc['OMC7'], cbr['CBR3'])
rule109 = ctrl.Rule(fibre['F3'] & liquid_limit['LL4'] & omc['OMC1'], cbr['CBR5'])
rule110 = ctrl.Rule(fibre['F3'] & liquid_limit['LL4'] & omc['OMC2'], cbr['CBR5'])
rule111 = ctrl.Rule(fibre['F3'] & liquid_limit['LL4'] & omc['OMC3'], cbr['CBR5'])
rule112 = ctrl.Rule(fibre['F3'] & liquid_limit['LL4'] & omc['OMC4'], cbr['CBR4'])
rule113 = ctrl.Rule(fibre['F3'] & liquid_limit['LL4'] & omc['OMC5'], cbr['CBR4'])
rule114 = ctrl.Rule(fibre['F3'] & liquid_limit['LL4'] & omc['OMC6'], cbr['CBR4'])
rule115 = ctrl.Rule(fibre['F3'] & liquid_limit['LL4'] & omc['OMC7'], cbr['CBR3'])
rule116 = ctrl.Rule(fibre['F3'] & liquid_limit['LL5'] & omc['OMC1'], cbr['CBR4'])
rule117 = ctrl.Rule(fibre['F3'] & liquid_limit['LL5'] & omc['OMC2'], cbr['CBR4'])
rule118 = ctrl.Rule(fibre['F3'] & liquid_limit['LL5'] & omc['OMC3'], cbr['CBR4'])
rule119 = ctrl.Rule(fibre['F3'] & liquid_limit['LL5'] & omc['OMC4'], cbr['CBR3'])
rule120 = ctrl.Rule(fibre['F3'] & liquid_limit['LL5'] & omc['OMC5'], cbr['CBR3'])
rule121 = ctrl.Rule(fibre['F3'] & liquid_limit['LL5'] & omc['OMC6'], cbr['CBR2'])
rule122 = ctrl.Rule(fibre['F3'] & liquid_limit['LL5'] & omc['OMC7'], cbr['CBR2'])
rule123 = ctrl.Rule(fibre['F3'] & liquid_limit['LL6'] & omc['OMC1'], cbr['CBR4'])
rule124 = ctrl.Rule(fibre['F3'] & liquid_limit['LL6'] & omc['OMC2'], cbr['CBR4'])
rule125 = ctrl.Rule(fibre['F3'] & liquid_limit['LL6'] & omc['OMC3'], cbr['CBR4'])
rule126 = ctrl.Rule(fibre['F3'] & liquid_limit['LL6'] & omc['OMC4'], cbr['CBR3'])
rule127 = ctrl.Rule(fibre['F3'] & liquid_limit['LL6'] & omc['OMC5'], cbr['CBR3'])
rule128 = ctrl.Rule(fibre['F3'] & liquid_limit['LL6'] & omc['OMC6'], cbr['CBR2'])
rule129 = ctrl.Rule(fibre['F3'] & liquid_limit['LL6'] & omc['OMC7'], cbr['CBR2'])
rule130 = ctrl.Rule(fibre['F3'] & liquid_limit['LL7'] & omc['OMC1'], cbr['CBR4'])
rule131 = ctrl.Rule(fibre['F3'] & liquid_limit['LL7'] & omc['OMC2'], cbr['CBR4'])
rule132 = ctrl.Rule(fibre['F3'] & liquid_limit['LL7'] & omc['OMC3'], cbr['CBR3'])
rule133 = ctrl.Rule(fibre['F3'] & liquid_limit['LL7'] & omc['OMC4'], cbr['CBR3'])
rule134 = ctrl.Rule(fibre['F3'] & liquid_limit['LL7'] & omc['OMC5'], cbr['CBR2'])
rule135 = ctrl.Rule(fibre['F3'] & liquid_limit['LL7'] & omc['OMC6'], cbr['CBR2'])
rule136 = ctrl.Rule(fibre['F3'] & liquid_limit['LL7'] & omc['OMC7'], cbr['CBR1'])
rule137 = ctrl.Rule(fibre['F4'] & liquid_limit['LL1'] & omc['OMC1'], cbr['CBR7'])
rule138 = ctrl.Rule(fibre['F4'] & liquid_limit['LL1'] & omc['OMC2'], cbr['CBR6'])
rule139 = ctrl.Rule(fibre['F4'] & liquid_limit['LL1'] & omc['OMC3'], cbr['CBR6'])
rule140 = ctrl.Rule(fibre['F4'] & liquid_limit['LL1'] & omc['OMC4'], cbr['CBR5'])
rule141 = ctrl.Rule(fibre['F4'] & liquid_limit['LL1'] & omc['OMC5'], cbr['CBR5'])
rule142 = ctrl.Rule(fibre['F4'] & liquid_limit['LL1'] & omc['OMC6'], cbr['CBR4'])
rule143 = ctrl.Rule(fibre['F4'] & liquid_limit['LL1'] & omc['OMC7'], cbr['CBR4'])
rule144 = ctrl.Rule(fibre['F4'] & liquid_limit['LL2'] & omc['OMC1'], cbr['CBR7'])
rule145 = ctrl.Rule(fibre['F4'] & liquid_limit['LL2'] & omc['OMC2'], cbr['CBR6'])
rule146 = ctrl.Rule(fibre['F4'] & liquid_limit['LL2'] & omc['OMC3'], cbr['CBR6'])
rule147 = ctrl.Rule(fibre['F4'] & liquid_limit['LL2'] & omc['OMC4'], cbr['CBR5'])
rule148 = ctrl.Rule(fibre['F4'] & liquid_limit['LL2'] & omc['OMC5'], cbr['CBR5'])
rule149 = ctrl.Rule(fibre['F4'] & liquid_limit['LL2'] & omc['OMC6'], cbr['CBR4'])
rule150 = ctrl.Rule(fibre['F4'] & liquid_limit['LL2'] & omc['OMC7'], cbr['CBR4'])
rule151 = ctrl.Rule(fibre['F4'] & liquid_limit['LL3'] & omc['OMC1'], cbr['CBR6'])
rule152 = ctrl.Rule(fibre['F4'] & liquid_limit['LL3'] & omc['OMC2'], cbr['CBR5'])
rule153 = ctrl.Rule(fibre['F4'] & liquid_limit['LL3'] & omc['OMC3'], cbr['CBR5'])
rule154 = ctrl.Rule(fibre['F4'] & liquid_limit['LL3'] & omc['OMC4'], cbr['CBR4'])
rule155 = ctrl.Rule(fibre['F4'] & liquid_limit['LL3'] & omc['OMC5'], cbr['CBR4'])
rule156 = ctrl.Rule(fibre['F4'] & liquid_limit['LL3'] & omc['OMC6'], cbr['CBR3'])
rule157 = ctrl.Rule(fibre['F4'] & liquid_limit['LL3'] & omc['OMC7'], cbr['CBR2'])
rule158 = ctrl.Rule(fibre['F4'] & liquid_limit['LL4'] & omc['OMC1'], cbr['CBR6'])
rule159 = ctrl.Rule(fibre['F4'] & liquid_limit['LL4'] & omc['OMC2'], cbr['CBR5'])
rule160 = ctrl.Rule(fibre['F4'] & liquid_limit['LL4'] & omc['OMC3'], cbr['CBR5'])
rule161 = ctrl.Rule(fibre['F4'] & liquid_limit['LL4'] & omc['OMC4'], cbr['CBR4'])
rule162 = ctrl.Rule(fibre['F4'] & liquid_limit['LL4'] & omc['OMC5'], cbr['CBR4'])
rule163 = ctrl.Rule(fibre['F4'] & liquid_limit['LL4'] & omc['OMC6'], cbr['CBR3'])
rule164 = ctrl.Rule(fibre['F4'] & liquid_limit['LL4'] & omc['OMC7'], cbr['CBR2'])
rule165 = ctrl.Rule(fibre['F4'] & liquid_limit['LL5'] & omc['OMC1'], cbr['CBR5'])
rule166 = ctrl.Rule(fibre['F4'] & liquid_limit['LL5'] & omc['OMC2'], cbr['CBR4'])
rule167 = ctrl.Rule(fibre['F4'] & liquid_limit['LL5'] & omc['OMC3'], cbr['CBR4'])
rule168 = ctrl.Rule(fibre['F4'] & liquid_limit['LL5'] & omc['OMC4'], cbr['CBR3'])
rule169 = ctrl.Rule(fibre['F4'] & liquid_limit['LL5'] & omc['OMC5'], cbr['CBR3'])
rule170 = ctrl.Rule(fibre['F4'] & liquid_limit['LL5'] & omc['OMC6'], cbr['CBR2'])
rule171 = ctrl.Rule(fibre['F4'] & liquid_limit['LL5'] & omc['OMC7'], cbr['CBR2'])
rule172 = ctrl.Rule(fibre['F4'] & liquid_limit['LL6'] & omc['OMC1'], cbr['CBR3'])
rule173 = ctrl.Rule(fibre['F4'] & liquid_limit['LL6'] & omc['OMC2'], cbr['CBR3'])
rule174 = ctrl.Rule(fibre['F4'] & liquid_limit['LL6'] & omc['OMC3'], cbr['CBR2'])
rule175 = ctrl.Rule(fibre['F4'] & liquid_limit['LL6'] & omc['OMC4'], cbr['CBR2'])
rule176 = ctrl.Rule(fibre['F4'] & liquid_limit['LL6'] & omc['OMC5'], cbr['CBR1'])
rule177 = ctrl.Rule(fibre['F4'] & liquid_limit['LL6'] & omc['OMC6'], cbr['CBR1'])
rule178 = ctrl.Rule(fibre['F4'] & liquid_limit['LL6'] & omc['OMC7'], cbr['CBR1'])
rule179 = ctrl.Rule(fibre['F4'] & liquid_limit['LL7'] & omc['OMC1'], cbr['CBR3'])
rule180 = ctrl.Rule(fibre['F4'] & liquid_limit['LL7'] & omc['OMC2'], cbr['CBR2'])
rule181 = ctrl.Rule(fibre['F4'] & liquid_limit['LL7'] & omc['OMC3'], cbr['CBR2'])
rule182 = ctrl.Rule(fibre['F4'] & liquid_limit['LL7'] & omc['OMC4'], cbr['CBR2'])
rule183 = ctrl.Rule(fibre['F4'] & liquid_limit['LL7'] & omc['OMC5'], cbr['CBR1'])
rule184 = ctrl.Rule(fibre['F4'] & liquid_limit['LL7'] & omc['OMC6'], cbr['CBR1'])
rule185 = ctrl.Rule(fibre['F4'] & liquid_limit['LL7'] & omc['OMC7'], cbr['CBR1'])
rule186 = ctrl.Rule(fibre['F5'] & liquid_limit['LL4'] & omc['OMC1'], cbr['CBR3'])
rule187 = ctrl.Rule(fibre['F5'] & liquid_limit['LL4'] & omc['OMC2'], cbr['CBR3'])
rule188 = ctrl.Rule(fibre['F5'] & liquid_limit['LL4'] & omc['OMC3'], cbr['CBR2'])
rule189 = ctrl.Rule(fibre['F5'] & liquid_limit['LL4'] & omc['OMC4'], cbr['CBR2'])
rule190 = ctrl.Rule(fibre['F5'] & liquid_limit['LL4'] & omc['OMC5'], cbr['CBR1'])
rule191 = ctrl.Rule(fibre['F5'] & liquid_limit['LL4'] & omc['OMC6'], cbr['CBR1'])
rule192 = ctrl.Rule(fibre['F5'] & liquid_limit['LL4'] & omc['OMC7'], cbr['CBR1'])
rule193 = ctrl.Rule(fibre['F5'] & liquid_limit['LL5'] & omc['OMC1'], cbr['CBR1'])
rule194 = ctrl.Rule(fibre['F5'] & liquid_limit['LL5'] & omc['OMC1'], cbr['CBR2'])
rule195 = ctrl.Rule(fibre['F5'] & liquid_limit['LL5'] & omc['OMC2'], cbr['CBR2'])
rule196 = ctrl.Rule(fibre['F5'] & liquid_limit['LL5'] & omc['OMC3'], cbr['CBR1'])
rule197 = ctrl.Rule(fibre['F5'] & liquid_limit['LL5'] & omc['OMC4'], cbr['CBR1'])
rule198 = ctrl.Rule(fibre['F5'] & liquid_limit['LL6'] & omc['OMC1'], cbr['CBR1'])
rule199 = ctrl.Rule(fibre['F5'] & liquid_limit['LL6'] & omc['OMC2'], cbr['CBR1'])
rule200 = ctrl.Rule(fibre['F5'] & liquid_limit['LL6'] & omc['OMC3'], cbr['CBR1'])
rule201 = ctrl.Rule(fibre['F5'] & liquid_limit['LL6'] & omc['OMC4'], cbr['CBR1'])
rule202 = ctrl.Rule(fibre['F5'] & liquid_limit['LL6'] & omc['OMC5'], cbr['CBR1'])
rule203 = ctrl.Rule(fibre['F5'] & liquid_limit['LL6'] & omc['OMC6'], cbr['CBR1'])
rule204 = ctrl.Rule(fibre['F5'] & liquid_limit['LL6'] & omc['OMC7'], cbr['CBR1'])
rule205 = ctrl.Rule(fibre['F5'] & liquid_limit['LL7'] & omc['OMC1'], cbr['CBR2'])
rule206 = ctrl.Rule(fibre['F5'] & liquid_limit['LL7'] & omc['OMC2'], cbr['CBR1'])
rule207 = ctrl.Rule(fibre['F5'] & liquid_limit['LL7'] & omc['OMC3'], cbr['CBR1'])
rule208 = ctrl.Rule(fibre['F5'] & liquid_limit['LL7'] & omc['OMC4'], cbr['CBR1'])
rule209 = ctrl.Rule(fibre['F5'] & liquid_limit['LL7'] & omc['OMC5'], cbr['CBR1'])
rule210 = ctrl.Rule(fibre['F5'] & liquid_limit['LL7'] & omc['OMC6'], cbr['CBR1'])
rule211 = ctrl.Rule(fibre['F5'] & liquid_limit['LL7'] & omc['OMC7'], cbr['CBR1'])
rule211 = ctrl.Rule(fibre['F6'] & liquid_limit['LL1'] & omc['OMC1'], cbr['CBR6'])
rule213 = ctrl.Rule(fibre['F6'] & liquid_limit['LL1'] & omc['OMC2'], cbr['CBR5'])
rule214 = ctrl.Rule(fibre['F6'] & liquid_limit['LL1'] & omc['OMC3'], cbr['CBR5'])
rule215 = ctrl.Rule(fibre['F6'] & liquid_limit['LL1'] & omc['OMC4'], cbr['CBR4'])
rule216 = ctrl.Rule(fibre['F6'] & liquid_limit['LL1'] & omc['OMC5'], cbr['CBR4'])
rule217 = ctrl.Rule(fibre['F6'] & liquid_limit['LL1'] & omc['OMC6'], cbr['CBR3'])
rule218 = ctrl.Rule(fibre['F6'] & liquid_limit['LL1'] & omc['OMC7'], cbr['CBR3'])
rule219 = ctrl.Rule(fibre['F6'] & liquid_limit['LL2'] & omc['OMC1'], cbr['CBR4'])
rule220 = ctrl.Rule(fibre['F6'] & liquid_limit['LL2'] & omc['OMC2'], cbr['CBR3'])
rule221 = ctrl.Rule(fibre['F6'] & liquid_limit['LL2'] & omc['OMC3'], cbr['CBR3'])
rule222 = ctrl.Rule(fibre['F6'] & liquid_limit['LL2'] & omc['OMC4'], cbr['CBR2'])
rule223 = ctrl.Rule(fibre['F6'] & liquid_limit['LL2'] & omc['OMC5'], cbr['CBR2'])
rule224 = ctrl.Rule(fibre['F6'] & liquid_limit['LL2'] & omc['OMC6'], cbr['CBR2'])
rule225 = ctrl.Rule(fibre['F6'] & liquid_limit['LL2'] & omc['OMC7'], cbr['CBR2'])
rule226 = ctrl.Rule(fibre['F6'] & liquid_limit['LL3'] & omc['OMC1'], cbr['CBR2'])
rule227 = ctrl.Rule(fibre['F6'] & liquid_limit['LL3'] & omc['OMC2'], cbr['CBR2'])
rule228 = ctrl.Rule(fibre['F6'] & liquid_limit['LL3'] & omc['OMC3'], cbr['CBR2'])
rule229 = ctrl.Rule(fibre['F6'] & liquid_limit['LL3'] & omc['OMC4'], cbr['CBR1'])
rule230 = ctrl.Rule(fibre['F6'] & liquid_limit['LL3'] & omc['OMC5'], cbr['CBR1'])
rule231 = ctrl.Rule(fibre['F7'] & liquid_limit['LL5'] & omc['OMC1'], cbr['CBR1'])
rule232 = ctrl.Rule(fibre['F7'] & liquid_limit['LL5'] & omc['OMC2'], cbr['CBR1'])
rule233 = ctrl.Rule(fibre['F7'] & liquid_limit['LL5'] & omc['OMC3'], cbr['CBR1'])
rule234 = ctrl.Rule(fibre['F7'] & liquid_limit['LL5'] & omc['OMC4'], cbr['CBR1'])
rule235 = ctrl.Rule(fibre['F7'] & liquid_limit['LL5'] & omc['OMC5'], cbr['CBR1'])
rule235 = ctrl.Rule(fibre['F7'] & liquid_limit['LL5'] & omc['OMC6'], cbr['CBR1'])
rule237 = ctrl.Rule(fibre['F7'] & liquid_limit['LL5'] & omc['OMC7'], cbr['CBR1'])
rule238 = ctrl.Rule(fibre['F7'] & liquid_limit['LL6'] & omc['OMC1'], cbr['CBR1'])
rule239 = ctrl.Rule(fibre['F7'] & liquid_limit['LL6'] & omc['OMC2'], cbr['CBR1'])
rule240 = ctrl.Rule(fibre['F7'] & liquid_limit['LL6'] & omc['OMC3'], cbr['CBR1'])
rule241 = ctrl.Rule(fibre['F7'] & liquid_limit['LL6'] & omc['OMC4'], cbr['CBR1'])
rule242 = ctrl.Rule(fibre['F7'] & liquid_limit['LL6'] & omc['OMC5'], cbr['CBR1'])
rule243 = ctrl.Rule(fibre['F7'] & liquid_limit['LL6'] & omc['OMC6'], cbr['CBR1'])
rule244 = ctrl.Rule(fibre['F7'] & liquid_limit['LL6'] & omc['OMC6'], cbr['CBR1'])

# control system
prediction_control = ctrl.ControlSystem([
  rule1, rule2, rule3, rule4, rule5,  rule6, rule7, rule8, rule9,
  rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17,
  rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25,
  rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33,
  rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41,
  rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49,
  rule50, rule51, rule52, rule53, rule54, rule55, rule56, rule57,
  rule58, rule59, rule60, rule61, rule62, rule63, rule64, rule65,
  rule66, rule67, rule68, rule69, rule70, rule71, rule72, rule73,
  rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81,
  rule82, rule83, rule84, rule85, rule86, rule87, rule88, rule89,
  rule90, rule91, rule92, rule93, rule94, rule95, rule96, rule97,
  rule98, rule99, rule100, rule101, rule102, rule103, rule104,
  rule105, rule106, rule107, rule108, rule109, rule110, rule111,
  rule112, rule113, rule114, rule115, rule116, rule117, rule118,
  rule119, rule120, rule121, rule122, rule123, rule124, rule125,
  rule126, rule127, rule128, rule129, rule130, rule131, rule244,
  rule132, rule133, rule134, rule135, rule136, rule137, rule138, rule139,
  rule140, rule141, rule142, rule143, rule144, rule145, rule146, rule147,
  rule148, rule149, rule150, rule151, rule152, rule153, rule154, rule155,
  rule156, rule157, rule158, rule159, rule160, rule161, rule162, rule163,
  rule164, rule165, rule166, rule167, rule168, rule169, rule170, rule171,
  rule172, rule173, rule174, rule175, rule176, rule177, rule178, rule179,
  rule180, rule181, rule182, rule183, rule184, rule185, rule186, rule187,
  rule188, rule189, rule190, rule191, rule192, rule193, rule194, rule195,
  rule196, rule197, rule198, rule199, rule200, rule201, rule202, rule203,
  rule204, rule205, rule206, rule207, rule208, rule209, rule210, rule211,
  rule211, rule213, rule214, rule215, rule216, rule217, rule218, rule219,
  rule220, rule221, rule222, rule223, rule224, rule225, rule226, rule227,
  rule228, rule229, rule230, rule231, rule232, rule233, rule234, rule235,
  rule235, rule237, rule238, rule239, rule240, rule241, rule242, rule243,
])

prediction_simulation = ctrl.ControlSystemSimulation(prediction_control)


def predict(fibre: float | int, liquid_limit: float | int, omc: float | int):
    """
    Calculates the resulting cbr for given inputs
    """
    prediction_simulation.input["F"] = fibre
    prediction_simulation.input["LL"] = liquid_limit
    prediction_simulation.input["OMC"] = omc

    prediction_simulation.compute()
    return prediction_simulation.output["CBR"]


def view_charts():
    """
    Visualizes the fuzzy logic system
    """
    os.makedirs('reports', exist_ok=True)
    fibre.view()
    plt.savefig('./reports/F_view.png')
    plt.close()

    liquid_limit.view()
    plt.savefig('./reports/LL_view.png')
    plt.close()

    omc.view()
    plt.savefig('./reports/OMC_view.png')
    plt.close()

    cbr.view()
    plt.savefig('./reports/CBR_view.png')
    plt.close()

    # prediction_control.view()
    # plt.savefig('./reports/prediction_control_view.png')
    # plt.close()
