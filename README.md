# 2017ChipBets

Your have 2 bags containing 200 chips each.

There are red and white chips distributed between the two bags:

    White dominant bag: 160 white chips and 40 red chips
    Red dominant bag:   120   red chips and 80 white chips
    
You have a bank account of $1000.

The object is to guess which bag chips are being selected from and to bet
up to 100% of your bank on the guess. E.g. you guess bag "wd" and bet $50.
If you are correct, you get $50; if you are wrong, you lose $50.

You will get 100 bets. At the beginning of each session, a bag
is selected at random. You can buy chips from that bag for $1
each using your bank account.  Chips are purchased 1 at a time and
you can switch from buying chips to betting at any time.

Chips are not replaced in the bags at any time.

Highest bank account at the end of 100 bets wins.

Your strategy must be coded in the file "strategy.py" with the function
"bet_strategy" with the signature:

def bet_strategy(session, bank, chip_color, session_history, **kwargs)
    
    session is an int [0, 99] enumerating your bets
    bank is your current bank balance
    chip_color is the color of a chip if your last move was a "buy" ["w","r"]
    session_history is the list of all of your moves during the current session

Your function returns the tuple defining a chip buy or a bet:

    move_choice="bet" or "buy
    bet = [1, bank]
    bet_bag_dominant color = "wd" or "rd"

I have provided the simulation code that will be used to evaluate your
strategy at the end of the competition in "sim.py". You can change anything
here you like, but there probabaly isn't any need.

If you plan to do a parameter search, use the kwargs.  See meta.py for an
example of how this is easily done.

The example code shows a strategy of random selection base on buying a
single chip before betting. Run this example to see how it works, then
do something better!

Good luck!


