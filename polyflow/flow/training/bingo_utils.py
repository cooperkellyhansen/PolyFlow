"""
Helper functions needed for Bingo implementation
"""

def get_agraph_similarity(ag_1, ag_2):
    """
    function to determine the similarity of two acyclic graphs
    from bingo population

    Parameters:
    -----------
    ag_1: Bingo acyclic graph
    ag_2: Bingo acyclic graph

    Return:
    -------
    bool value based on fitness and complexity of agraphs
    """

    return ag_1.fitness == ag_2.fitness and ag_1.get_complexity() == ag_2.get_complexity()

def print_pareto_front(hall_of_fame):
    """
    Terminal friendly output of the hall of fame 
    equations from Bingo population

    Parameters:
    -----------
    hall_of_fame: List of Bingo member objects

    """
    print("    FITNESS    COMPLEXITY    EQUATION")

    for member in hall_of_fame:
        print('%.3e    ' % member.fitness, member.get_complexity(), '    f(X_0) =', member)

