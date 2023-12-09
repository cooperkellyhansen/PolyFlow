"""
This file sets up and trains Bingo. Note that most command line
args are not required and a default Bingo model will be run if 
none specified.

"""
# Ignoring some linting rules in tests
# pylint: disable=redefined-outer-name
# pylint: disable=missing-docstring
import random
import numpy as np
import sympy
from mpi4py import MPI

# Bingo imports for customizable version
from bingo.evolutionary_algorithms.age_fitness import AgeFitnessEA
from bingo.evolutionary_optimizers.serial_archipelago import SerialArchipelago
from bingo.evolutionary_optimizers.parallel_archipelago import ParallelArchipelago
from bingo.evaluation.evaluation import Evaluation
from bingo.evolutionary_optimizers.island import Island
from bingo.local_optimizers.continuous_local_opt import ContinuousLocalOptimization
from bingo.local_optimizers.local_opt_fitness import LocalOptFitnessFunction
from bingo.local_optimizers.scipy_optimizer import ScipyOptimizer
from bingo.symbolic_regression.agraph.agraph import AGraph
from bingo.symbolic_regression.agraph.component_generator import ComponentGenerator
from bingo.symbolic_regression import AGraphGenerator, AGraphCrossover, AGraphMutation, ExplicitRegression, ExplicitTrainingData
from bingo.stats.pareto_front import ParetoFront
# Seed generator
from research.GenerateSeeds import SubgraphSeedGenerator
# For 'nofuss' implementation
from bingo.symbolic_regression.symbolic_regressor import SymbolicRegressor

def main():
    parser = argparser.ArgumentParser()
    parser.add_argument('--store_path', required=True)
    parser.add_argument('--population_size', default=500)
    parser.add_argument('--stack_size', default=32)
    parser.add_argument('--operators', type=list, default=None)
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
        # Instantiate explicit training data
        #
        training_data = ExplicitTrainingData(features, labels)

        #
        # Build component generator
        # FIXME: These should probably exist in the config file
        component_generator = ComponentGenerator(
                                features.shape[1],
                                terminal_probability        = 0.1,
                                operator_probability        = 0.7,
                                equation_probability        = 0.2,
                                num_initial_load_statements = 3)
        #
        # Add operators
        # FIXME: add in all possible operators
        possible_operators = ['+']
        for op in operators:
            msg = f'Operator {op} not a valid operator'
            assert op in possible_operators
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
                component_generator.add_equation(seed)i
        

        #
        # Build agrapg generator
        #
        agraph_generator = AGraphGenerator(
                            stack_size          = stack_size, 
                            component_generator = component_generator,
                             use_simplification  = use_simplification)
        
        #
        # Set up crossover and mutation
        #
        crossover = AGraphCrossover()
        mutation  = AGraphMutation(component_generator)
    
        #
        # Set up fitness
        # NOTE: We only support explicity regression right now
        fitness = ExplicitRegression(
                    training_data = training_data,
                    metric        = metric,
                    relative      = False)

        #local_opt_fitness = ContinuousLocalOptimization(fitness, algorithm='lm')
        local_opt_fitness = LocalOptFitnessFunction(
                                fitness = fitness, 
                                ScipyOptimizer(
                                    fitness = fitness, 
                                    method  = clo_alg))
        evaluator          = Evaluation(local_opt_fitness)

        #
        # Parse evolutionary algorithm
        #FIXME: arguments and map completion
        ea_map = {age_fitness: AgeFitnessEA(),
                  }
        ea = AgeFitnessEA(evaluator        = evaluator, 
                          agraph_generator = agraph_generator, 
                          crossover        = crossover,
                          mutation         = mutation, 
                          crossover_prob   = crossover_prob, 
                          mutation_prob    = mutation_prob,
                          population_size  = population_size)

        island = Island(ea, agraph_generator, POP_SIZE)

        pareto_front = ParetoFront(secondary_key=lambda ag: ag.get_complexity(),
                similarity_function=agraph_similarity)

        archipelago = ParallelArchipelago(island,hall_of_fame=pareto_front)
        #archipelago = SerialArchipelago(island,hall_of_fame=pareto_front)

        opt_result = archipelago.evolve_until_convergence(MAX_GENERATIONS,
                                                          FITNESS_THRESHOLD,


