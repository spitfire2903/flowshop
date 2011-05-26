#!/usr/bin/env python
# -*- coding: utf8 -*-

import random

# Constantes
NULL = -1

def ux(individual_1, individual_2, individual_size, percentage):
    """
        Uniform crossover
    """
    if percentage == 0:
        return "Error, percentage equal zero!"
    else:
        p = int(percentage * individual_size)
    choices = random.sample(range(0, individual_size), p)
    choices.sort()
    son_1 = []
    son_2 = []
    piece_1 = {} # parte do individual_1 que vai para o son_2
    piece_2 = {} # parte do individual_2 que vai para o son_1
    for i in range(0, individual_size):
        if i in choices:
            son_1.append(individual_1[i])
            piece_2[individual_1.index(individual_2[i])] = individual_2[i]
            son_2.append(NULL)
        else:
            son_2.append(individual_2[i])
            piece_1[individual_2.index(individual_1[i])] = individual_1[i]
            son_1.append(NULL)

    for i in piece_1:
        j = son_1.index(NULL)
        son_1[j] = piece_1[i]
    
    for i in piece_2:
        j = son_2.index(NULL)
        son_2[j] = piece_2[i]
    
    return (son_1, son_2)

# XXX: remover testes no final
# testes        
        
# ux:
"""size = 15
a = range(0, size)
b = range(0, size)
random.shuffle(a)
random.shuffle(b)
s1, s2 =  ux(a, b, size, .7)

print a, b
print s1, s2
"""

