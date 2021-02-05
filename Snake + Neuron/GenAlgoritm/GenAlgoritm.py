import random
import numpy as np


def roulette(cum_sum):
    chance = random.random()
    veriable = list(cum_sum.copy())
    veriable.append(chance)
    veriable = sorted(veriable)
    return veriable.index(chance)


def listmerge3(lstlst):
    all=[]
    for lst in lstlst:
      all.extend(lst)
    return all


def mating(parents):
    res = [[],[]]
    for k in range(len(parents[0])):
        temp_list_first = []
        temp_list_second = []
        for l in range(len(parents[0][0])):
            if random.randint(0, 1) == 0:
                temp_list_first.append(parents[0][k][l])
                temp_list_second.append(parents[1][k][l])
            else:
                temp_list_second.append(parents[0][k][l])
                temp_list_first.append(parents[1][k][l])
        res[0].append(temp_list_first)
        res[1].append(temp_list_second)
    return res


def mutation(individual):
    m_ind = individual
    for j in range(len(m_ind)):
        for k in range(len(m_ind[0])):
            for l in range(len(m_ind[0][0])):
                r = random.randint(0, 100)
                if r == 0:
                    m_ind[j][k][l] = np.random.rand()

    return m_ind


def fitness(time, food_count):
    return time*time * 2**food_count
