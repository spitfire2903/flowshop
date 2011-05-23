#!/usr/bin/env python
# -*- coding: utf8 -*-

import random
from fitness import fitness
from flowshop import Problem, read_problem
from globals_settings import PROBLEM_FILE
from operator import attrgetter

class Individual:
    def __init__(self, sequence, makespan):
        self.sequence = sequence
        self.makespan = makespan
    def __repr__(self):
        return repr((self.sequence, self.makespan))

#XXX: mover a função para a classe Individual
def create_individual(Problem):
    N, M, data = Problem.show()
    sequence = range(0, N)
    random.shuffle(sequence)
    makespan = fitness(sequence, Problem)
    return (sequence, makespan)

def create_population(size, Problem):
    i = 0
    population = []
    while i < size:
        sequence, makespan = create_individual(Problem)
        I = Individual(sequence, makespan)
        population.append(I)
        i = i + 1
    return sorted(population, key=lambda individual: individual.makespan)

# testes
P = read_problem(PROBLEM_FILE)

#print create_individual(P)

pop = create_population(10, P)
print pop



