#!/usr/bin/env python3
""" Example file for meta searches of the parameter space.
    Use this one as an example and do whatever you want!

    This file searchs the bet_frac (fraction of the bank to bet)
    for optimization."""

from sim import *
for i in range(60):
    bet_frac = 0.05 + i*(.002)
    print("{}, {}".format(bet_frac, get_bank(bet_frac=bet_frac)))
