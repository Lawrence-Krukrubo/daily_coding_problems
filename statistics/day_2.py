"""
Task
In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.
"""


def toss_2_coins():
    # Possible outcome of first die
    p_a = [1, 2, 3, 4, 5, 6]
    # Possible outcome of second die
    p_b = [1, 2, 3, 4, 5, 6]

    # Total sample space (p_a * p_b)
    S = [(i, j) for i in p_a for j in p_b]

    # Total number of elements is S
    total = len(S)

    # Count number of elements in S have no more than 9 combined items
    not_more_than_9 = len([i for i in S if sum(i) <= 9])

    # To find Probability of sum of two dice being at most 9
    probability = not_more_than_9 / total

    return round(probability, 4)


"""
Task
In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die 
will be different and the two dice have a sum of 6.
"""


def toss_2_more_coins():
    # Possible outcome of first die
    p_a = [1, 2, 3, 4, 5, 6]
    # Possible outcome of second die
    p_b = [1, 2, 3, 4, 5, 6]

    # Total sample space (p_a * p_b)
    S = [(i, j) for i in p_a for j in p_b]

    # Total number of elements is S
    total = len(S)

    # Count number of elements in S that have a combined score of 6,
    # Also ensure that items in each tuple of elements are different.
    diff_equate_6 = len([i for i in S if sum(i) == 6 and i[0] != i[1]])

    # To find Probability of sum of two dice being at most 9
    probability = diff_equate_6 / total

    return round(probability, 4)


"""
Compound Event Probability
Task

There are 3 urns labeled X, Y, and Z.
Urn X contains 4 red balls and 3 black balls.
Urn Y contains 5 red balls and 4 black balls.
Urn Z contains 4 red balls and 4 black balls.

One ball is drawn from each of the 3 urns. 
What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?
"""


def compound_prob():

    X = {'Red': 4, 'Black': 3}
    Y = {'Red': 5, 'Black': 4}
    Z = {'Red': 4, 'Black': 4}

    # One ball is drawn from each of X, Y Z, let's calc P of drawing
    # One Red ball or One Black ball from each Urn

    # For X:
    p_red_given_x = X['Red'] / sum(X.values())
    p_black_given_x = X['Black'] / sum(X.values())

    # For y
    p_red_given_y = Y['Red'] / sum(Y.values())
    p_black_given_y = Y['Black'] / sum(Y.values())

    # For Z
    p_red_given_z = Z['Red'] / sum(Z.values())
    p_black_given_z = Z['Black'] / sum(Z.values())

    # Therefore we need to find the probability of 2 red and 1 black in any combination
    # P(X[red]*Y[red]*Z[black]) + P(X[red]*Y[black]*Z[red]) + P(X[black]*Y[red]*Z[red])

    p_one = p_red_given_x * p_red_given_y * p_black_given_z
    p_two = p_red_given_x * p_black_given_y * p_red_given_z
    p_three = p_black_given_x * p_red_given_y * p_red_given_z

    # Therefore compound probability of 2 reds and 1 black, given X, Y and Z;-
    comp_prob = p_one + p_two + p_three

    return round(comp_prob, 4)


print(compound_prob())