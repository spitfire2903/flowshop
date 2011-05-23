#!/usr/bin/env python
# -*- coding: utf8 -*-

import flowshop

def fitness(sequence, P):
    N, M, data = P.show()
    makespan = 0
    last_machine = [0] * M
    last_job = [0] * N
    for j in sequence:
        m = 0
        while m < M:
            last_machine[m] = last_machine[m] + data[j][m]
            last_job[j] = last_job[j] + data[j][m]
            if last_machine[m] > last_job[j]:
                last_job[j] = last_machine[m]
            else:
                last_machine[m] = last_job[j]       
            m = m + 1
    return max(last_machine)


