#!/usr/bin/env python
# -*- coding: utf8 -*-

import random

def create_individual(size):
    sequence = range(0, size)
    random.shuffle(sequence)

    return sequence
    

class population(object):
    def __init__(self):
        self.size = size
        


# testes
print create_individual(10)
