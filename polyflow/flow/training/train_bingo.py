"""
This file sets up and trains Bingo. Note that most command line
args are not required and a default Bingo model will be run if 
none specified.

"""
from bingo.symbolic_regression.symbolic_regressor import SymbolicRegressor
from bingo.evolutionary_algorithms.age_fitness import AgeFitnessEA 

def main():
    parser = argparser.ArgumentParser()
    parser.add_argument('--store_path', required=True)
    parser.add_argument('--population_size', default=500)
    parser.add_argument('--stack_size', default=32)
    parser.add_argument('--operators', default=None)
    parser.add_argument('--use_simplification', default=False)
    parser.add_argument('--crossover_prob', default=0.4)
    parser.add_argument('--mutation_prob', default=0.4)
    parser.add_argument('--metric', default='mse')
    parser.add_argument('--parallel', default=False)
    parser.add_argument('--clo_alg', default='lm')
    parser.add_argument('--generations', default=1e16)
    parser.add_argument('--fitness_threshold', default=1e-16)
    parser.add_argument('--max_time', default=1800)
    parser.add_argument('--max_evals', default=1e16)
    parser.add_argument('--evolutionary_algorithm', default=AgeFitnessEA())
    parser.add_argument('--clo_threshold', default=1e-8)
    parser.add_argument('--scale_max_evals', default=False)
    parser.add_argument('--random_state', default=None)
    parser.add_argument('--nofuss', default=True)
    
    store_path             = args.store_path
    population_size        = args.population_size,
    stack_size             = args.stack_size,
    operators              = args.operators,
    use_simplification     = args.use_simplification,
    crossover_prob         = args.crossover_prob,
    mutation_prob          = args.mutation_prob,
    metric                 = args.metric,
    parallel               = args.parallel,
    clo_alg                = args.clo_alg,
    generations            = args.generations,
    fitness_threshold      = args.fitness_threshold,
    max_time               = args.max_time,
    max_evals              = args.max_evals,
    evolutionary_algorithm = args.evolutionary_algorithm,
    clo_threshold          = args.clo_threshold,
    scale_max_evals        = args.scale_max_evals,
    random_state           = args.random_state


    #
    # Collect training data from kosh
    #
    # Open store
    store = kosh.connect(store=store_path)
    
    # Query for train/test/validation splits


    if nofuss:
        #
        # Set up Bingo symbolic regressor. This is the simplest 
        # method of training a Bingo model but does lack some 
        # customizability.
        #
        regressor = SymbolicRegressor(
                        population_size        = population_size,
                        stack_size             = stack_size,
                        operators              = operators,
                        use_simplification     = use_simplification,
                        crossover_prob         = crossover_prob,
                        mutation_prob          = mutation_prob,
                        metric                 = metric,
                        parallel               = parallel,
                        clo_alg                = clo_alg,
                        generations            = generations,
                        fitness_threshold      = fitness_threshold,
                        max_time               = max_time,
                        max_evals              = max_evals,
                        evolutionary_algorithm = evolutionary_algorithm,
                        clo_threshold          = clo_algorithm,
                        scale_max_evals        = scale_max_evals,
                        random_state           = random_state)

        #
        # Run Bingo
        #
        regressor.fit(features, labels)

        #
        # Get best individual found using grid search
        #
        model = regressor.get_best_individual()

        #
        # Predict using the best individual
        #
        pred_y = regressor.predict(X)
        pred_y = model.evaluate_equation_at(features)

        #
        # Load the nofuss predictions into Kosh
        #


    else:




        #
        # Cache Pareto front
        #


