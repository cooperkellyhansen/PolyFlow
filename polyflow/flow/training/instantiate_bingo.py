"""
"""

def main(features, labels):
    """

    """
    #
    # Instantiate explicit training data
    #
    training_data = ExplicitTrainingData

    #
    # Build component generator
    #
    component_generator = ComponentGenerator(features.shape[1],
                                             terminal_probability        = 0.1,
                                             operator_probability        = 0.7,
                                             equation_probability        = 0.2,
                                             num_initial_load_statements = 3)
    #
    # Add operators
    #
    for op in operator_list:
        component_generator.add_operator(op)

    
    #
    # Conduct seeding if toggled
    #
    if seed:
        eq
        # Transform to agraph
        eq = AGraph(equation=eq)
        # Use built-in seed generator to get seed strings
        seeds = SubgraphSeedGenerator.get_seed_strs(eq.command_array)
        # Add seeds to component generator
        for seed in seeds:
            component_generator.add_equation(seed)

