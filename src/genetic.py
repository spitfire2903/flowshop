#!/usr/bin/env python
# -*- coding: utf-8 -*-

def genetic():
    i = 0
    # FIXME: usar um critério de parada descente
    while i < 10:
        i = i + 1
        new_population = []
        for individual in population:
            x = random_selection(population)
            y = random_selection(population)
            son = crossover(x, y)
            if mutation_probability:
               son = mutation(son) 
            population.append(son)
        population = new_population
            


        
