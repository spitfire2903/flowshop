#!/usr/bin/env python
# -*- coding: utf-8 -*-

from globals_settings import PROBLEM_FILE
from array import array

class Problem:
    def __init__(self, N, M, data):
        self.N = N
        self.M = M
        self.data = data
    def show(self):
        return (self.N, self.M, self.data)

#XXX: Isso tá estranho acho melhor botar na classe esta função
def read_problem(problem_file):
    f =  open(problem_file)
    N, M = map(int, f.readline().split())
    data = [map(int, line.split()) for line in f]
    P = Problem(N, M, data)
    return P


#FIXME: retirar os testes
# testes
"""
P = read_problem(PROBLEM_FILE)
print P.show()    
"""
