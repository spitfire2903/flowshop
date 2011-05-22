#!/usr/bin/env python
# -*- coding: utf8 -*-

import random

class individual:
    def __init__(self, sequence, makespan):
        self.sequence = sequence
        self.makespan = makespan
    def show(self):
        return (self.sequence, self.makespan)

def create_individual(size):
    sequence = range(0, size)
    random.shuffle(sequence)
    return sequence

class population:
    def __init__(self):
        self.size = size
        


# testes
print create_individual(10)
