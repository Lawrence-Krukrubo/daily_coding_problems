"""
Permutations and Combinations

As you may have already noticed, finding patterns in the possible ways events can occur is very useful in helping us
count the number of desirable events in our sample space. Two of the easiest methods for doing this are with
permutations (when order matters) and combinations (when order doesn't matter).

Because the only difference between permutations and combinations is that combinations are unordered,
we can easily find the number of r-element combinations by dividing out the permutations (r!):

When we talk about combinations, we're talking about the number of subsets of size r that can be made
from a set of size n. In fact, `nCr`  is often referred to as "n choose r", because it's counting the number
of r-element combinations that can be chosen from a set of n elements. In notation, `nCr` is typically written as (n/r).


See Hacker-Rank Link below for more on Permutation and Combination

https://www.hackerrank.com/challenges/s10-mcq-5/tutorial
"""


"""
Task
You draw 2 cards from a standard 52-card deck without replacing them. What is the probability that both cards are of 
the same suit?
"""


def draw_cards():

    # there are 52 possible combinations for first card and 51 for the second...
    two_cards_comb = 52 * 51

    # Now there are 13 cards per suit per deck, therefore to get matching cards, on the
    # first pick, we pick from the entire 52 cards and on the second, we need to
    # pick from a pack of 13 to match, but we have already picked one card, so
    # we have only 12 valid options left... This gives:-
    similar_cards = 52 * 12

    # Therefore the probability as usual is valid options divided by total options...
    probability = similar_cards / two_cards_comb

    return round(probability, 4)


"""
Task
A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from the bag, at random, without replacement. 
If the first marble drawn is red, what is the probability that the second marble is blue?
"""


def marbles():
    # For first draw:
    p_red = 3/7

    # For second draw to be blue...
    # Without replacement means there are now 2 red and 4 blue marbles
    p_second_being_blue = 4 / 6

    return p_second_being_blue