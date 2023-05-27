# Ignoring some linting rules in tests
# pylint: disable=redefined-outer-name
# pylint: disable=missing-docstring
import random
import numpy as np
import sympy
from mpi4py import MPI
import pandas as pd

# Bingo imports
from bingo.evolutionary_algorithms.age_fitness import AgeFitnessEA
from bingo.evolutionary_optimizers.serial_archipelago import SerialArchipelago
from bingo.evolutionary_optimizers.parallel_archipelago import ParallelArchipelago
from bingo.evaluation.evaluation import Evaluation
from bingo.evolutionary_optimizers.island import Island
#from bingo.local_optimizers.continuous_local_opt import ContinuousLocalOptimization
from bingo.local_optimizers.local_opt_fitness import LocalOptFitnessFunction
from bingo.local_optimizers.scipy_optimizer import ScipyOptimizer
from bingo.symbolic_regression.agraph.agraph import AGraph
from bingo.symbolic_regression.agraph.component_generator import ComponentGenerator
from bingo.symbolic_regression import AGraphGenerator, AGraphCrossover, AGraphMutation, ExplicitRegression, ExplicitTrainingData
from bingo.stats.pareto_front import ParetoFront

#seed generator
from research.GenerateSeeds import SubgraphSeedGenerator

def main():
    
    parser = argparser.ArgumentParser()
    parser.add_argument('--store_path', required=True)

    #
    # Open Kosh store
    #

    #
    # Parse hyperparameters from yaml
    #
    #hyperparams
    POP_SIZE = 512
    STACK_SIZE = 32
    MAX_GENERATIONS = 100000
    FITNESS_THRESHOLD = 1.0E-10
    CHECK_FREQUENCY = 1000
    MIN_GENERATIONS = 1000
    
    ########################################################################################################################
    def equation_eval(x):
        # like 4.0 * X^2 + X but X is X_0 - X_1
        return 4.0 * (x[:, 0] - x[:, 1]) ** 2 + (x[:, 0] - x[:, 1])
    ########################################################################################################################
    def agraph_similarity(ag_1, ag_2):
        return ag_1.fitness == ag_2.fitness and ag_1.get_complexity() == ag_2.get_complexity()
    ########################################################################################################################
    def print_pareto_front(hall_of_fame):
        print("  FITNESS    COMPLEXITY    EQUATION")

        for member in hall_of_fame:
            #eq = member.get_formatted_string("sympy")
            print('%.3e    ' % member.fitness, member.get_complexity(),'   f(X_0) =', member)
    ########################################################################################################################
    def execute_generational_steps(X_in,y_in):

        communicator = MPI.COMM_WORLD
        rank = MPI.COMM_WORLD.Get_rank()

        X = np.asarray(X_in)
        y = np.asarray(y_in)

        #set-up input and output
        if rank == 0:
            X = np.asarray(X_in)
            y = np.asarray(y_in)

        x = MPI.COMM_WORLD.bcast(X, root=0)
        y = MPI.COMM_WORLD.bcast(y, root=0)

        training_data = ExplicitTrainingData(x, y)

        # you'll probably have to tune these probabilities/load statements
        # to you particular problem
 component_generator = ComponentGenerator(x.shape[1],
                                             terminal_probability=0.1,
                                             operator_probability=0.7,
                                             equation_probability=0.2,
                                             num_initial_load_statements=3)
    component_generator.add_operator("+")
    component_generator.add_operator("-")
    component_generator.add_operator("*")
    component_generator.add_operator("/")
    component_generator.add_operator("exp")
    component_generator.add_operator("log")
    component_generator.add_operator("sqrt")

    #using grain_data_A_soa.csv
    #component_generator.add_equation('-17.6929 - 0.00*(0.0070*(0.9929*(0.3111*x_6/0.5529*x_4) - 0.1987*log(0.6411*x_5))*(0.0266*(0.1155*x_4*x_4)/0.1672*log(0.6558*x_8))) - 2.89*exp(0.2032*(0.1037*log(0

    #eq = '-17.6929 - 0.00*(0.0070*(0.9929*(0.3111*x_6/0.5529*x_4) - 0.1987*log(0.6411*x_5))*(0.0266*(0.1155*x_4*x_4)/0.1672*log(0.6558*x_8))) - 2.89*exp(0.2032*(0.1037*log(0.0889*x_0) + 1.4393*log(0.13    #eq = AGraph(equation=eq)
    #seeds = SubgraphSeedGenerator.get_seed_strs(eq.command_array)
    #for seed in seeds:
    #    component_generator.add_equation(seed)

    #using grain_data_A_soa.csv with E11
    eq = '-17.6929 - 0.00*(0.0070*(0.9929*(0.3111*x_6/0.5529*x_4) - 0.1987*log(0.6411*x_5))*(0.0266*(0.1155*x_4*x_4)/0.1672*log(0.6558*x_8))) - 2.89*exp(0.2032*(0.1037*log(0.0889*x_0) + 1.4393*log(0.137    component_generator.add_equation(eq)

    eq = AGraph(equation=eq)
    seeds = SubgraphSeedGenerator.get_seed_strs(eq.command_array)
    for seed in seeds:
        component_generator.add_equation(seed)


    #using grain_data_infinitesimal_A.csv
    #component_generator.add_equation('-17.6817 - 2.97*exp(0.0259*(0.0996*X_9 - 0.0360*X_2))')
    #component_generator.add_equation('2.41*(0.9444*X_3 - 0.2512*(0.1056*X_3 + 0.2339*X_4))')
    #component_generator.add_equation('1.15*sqrt(abs(0.4356*exp(0.1536*(0.0696*X_2 + 7.6660*log(0.6649*X_4)))))')
    #component_generator.add_equation('-0.23*exp(0.1063*(0.2034*X_8*X_10))')
    #component_generator.add_equation('-0.14*exp(1.7967*X_4)')


    agraph_generator = AGraphGenerator(STACK_SIZE, component_generator,
                                       use_simplification=False)
    #test_agraph = agraph_generator()
    #print("Example of agraph generated with equation as component:", test_agraph)

    crossover = AGraphCrossover()
    mutation = AGraphMutation(component_generator)

    fitness = ExplicitRegression(training_data=training_data, metric='mse',relative=False)
    #local_opt_fitness = ContinuousLocalOptimization(fitness, algorithm='lm')
    local_opt_fitness = LocalOptFitnessFunction(fitness, ScipyOptimizer(fitness, method='lm'))
    evaluator = Evaluation(local_opt_fitness)

    ea = AgeFitnessEA(evaluator, agraph_generator, crossover,
                      mutation, 0.4, 0.4, POP_SIZE)

    island = Island(ea, agraph_generator, POP_SIZE)

    pareto_front = ParetoFront(secondary_key=lambda ag: ag.get_complexity(),
            similarity_function=agraph_similarity)

    archipelago = ParallelArchipelago(island,hall_of_fame=pareto_front)
    #archipelago = SerialArchipelago(island,hall_of_fame=pareto_front)

    opt_result = archipelago.evolve_until_convergence(MAX_GENERATIONS,
                                                      FITNESS_THRESHOLD,
