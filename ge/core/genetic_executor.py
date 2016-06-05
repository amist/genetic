from .environment import Environment
from .utils.utils import *

class GeneticExecutor:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.validate_kwargs()
        self.environments = [Environment(**kwargs['environment_kwargs'])]         # TODO: configurate
        
        
    def validate_kwargs(self):
        # print(self.kwargs)
        if 'problem' not in self.kwargs:
            raise ValueError('GeneticExecutor kwargs must contain a "problem" key')
        if 'environment_kwargs' not in self.kwargs:     # TODO: consider removing this - use default values
            raise ValueError('GeneticExecutor kwargs must contain a "environment_kwargs" key')
        if 'individual_kwargs' not in self.kwargs['environment_kwargs']:     # TODO: consider removing this - use default values
            raise ValueError('GeneticExecutor kwargs must contain a "individual_kwargs" key')
        
        
    def get_solution(self):
        # TODO: replace with a real implementation
        problem_class = get_problem_class(self.kwargs['problem'])
        
        for environment in self.environments:
            environment.initialize_population(problem_class)
            # TODO: number of generations
            for _ in range(10):
                environment.process_generation()
            
        print(len(self.environments[0].population))
        print(self.environments[0].population[0])
        print(self.environments[0].population[0].chromosome)
        print(self.environments[0].population[0].get_fitness_value())
        
        for individual in self.environments[0].population:
            print(individual.get_fitness_value())
        
        return self.environments[0].population[0]
        