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

class Population:
    def __init__(self):
        self.size = size
        
# testes
P = read_problem(PROBLEM_FILE)
print create_individual(P)
