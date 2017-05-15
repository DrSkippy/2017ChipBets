""" 
    SUBMIT THIS FILE AS YOUR ENTRY!
    
    This is where you code your strategy. You can add any imports and 
    additional functions you need. When you submit your answer, it must
    contain the fuction below.
"""    
from sim_parameters import *
import random

def bet_strategy(session, bank, chip_color, session_history, **kwargs):
    
    # Based on original bag setup
    p_r = (n_wd_r + n_rd_r)/(n_wd_w + n_wd_r + n_rd_w + n_rd_r)
    p_w = (n_wd_w + n_rd_w)/(n_wd_w + n_wd_r + n_rd_w + n_rd_r)
    
    # use logging like this
    logging.debug("p(r) = {} p(w) = {}".format(p_r, p_w))
    
    # There are two move choices:
    #     (1) to bet on the bag being white-dominate, red-dominate
    #         (ud for undefined)
    #     (2) buy a chip draw and see its color
    move_choices = ["bet","buy"]
    
    # These are the codes for your bag bet choices.  Don't bet on "ud"!
    dominant_bag_choices = ["wd", "rd", "ud"]

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
        if random.random() > p_w:
            bet_bag_dominant_color = "rd"
        else:
            bet_bag_dominant_color = "wd"

        # see file meta.py for parameter search example 
        # bet = int(kwargs["bet_frac"]*bank)
        bet = int(0.118*bank)
        
        # Don't try to bet more than you have
        if bet <=0:
            bet = bank
    
    return move_choice, bet, bet_bag_dominant_color
