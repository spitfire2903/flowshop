#!/usr/bin/env python
# -*- coding: utf8 -*-

import random
from fitness import fitness
from flowshop import Problem, read_problem
from globals_settings import PROBLEM_FILE

class Individual:
    def __init__(self, sequence, makespan):
        self.sequence = sequence
        self.makespan = makespan
    def show(self):
        return (self.sequence, self.makespan)

#XXX: mover a função para a classe Individual
def create_individual(Problem):
    N, M, data = Problem.show()
    sequence = range(0, N)
    random.shuffle(sequence)
    makespan = fitness(sequence, Problem)
    return (sequence, makespan)

#XXX: ordenar população por ordem de makespan
class Population:
    def __init__(self, size):
        self.size = size
        self.population = []
    def create_population(self, Problem):
        i = 0
        while i < self.size:
            sequence, makespan = create_individual(Problem)
            I = Individual(sequence, makespan)
            self.population.append(I)
            i = i + 1
    def get_population(self):
        return self.population
        
# testes
P = read_problem(PROBLEM_FILE)

#print create_individual(P)

pop = Population(10)
pop.create_population(P)
#print pop.get_population()



