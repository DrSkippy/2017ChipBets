""" This is where you code your stragegy.
    The stratgy shown uses the first chip drawn as the dominate
    bag indicator and bets a constant, optimized fraction of the bank
    based on this strategy."""

from sim_parameters import *

def bet_strategy(session, bank, chip_color, session_history, **kwargs):
    # you have two move choices, to bet on the bag being white-dominate, red-dominate
    # or ud for undefined
    move_choices = ["bet","buy"]
    # These are the codes for your bag bet choices.  Don't bet on "ud"!
    dominant_bag_choices = ["wd", "rd", "ud"]
    #############################################
    # simple demo strategy:
    #  1. buy a single chip
    #  2. predict based on chip color
    #  3. bet X% of bank
    #############################################
    if session_history == []:
        # We haven't done anything yet. So, buy a chip
        move_choice = "buy"
        # These options are ignored, but cannot be None
        bet = 0
        bet_bag_dominant_color = "ud"
    else:
        # Make a bet
        move_choice = "bet"
        # Based on last chip returned
        bet_bag_dominant_color = chip_color + "d"
        # of a constant fraction of the bank
        # This was for the finding the 0.38 optimization
        # see the file "meta.py" for parameter search example
        # bet = int(kwargs["bet_frac"]*bank)
        bet = int(0.38*bank)
        # Don't try to bet more than you have
        if bet <=0:
            bet = bank
    return move_choice, bet, bet_bag_dominant_color
