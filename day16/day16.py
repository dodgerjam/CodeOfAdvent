import itertools
from functools import reduce 
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
import numpy as np

def day16pt1(x):
    rules = set.union(*[cleanUpRules(i.strip()) for i in x[:x.index('\n')]])
    my_ticket = [int(j) for j in  x[x.index('\n')+2].split(',')]
    other_tickets = [[int(j) for j in i.strip().split(',')] for i in x[x.index('\n') + 5:]]
    return sum([sum([number for number in ticket if number not in rules]) for ticket in other_tickets])


def day16pt2(x):
    rules = [cleanUpRules(i.strip()) for i in x[:x.index('\n')]]
    my_ticket = [int(j) for j in  x[x.index('\n')+2].split(',')]
    required_rules = [x.index(i) for i in x[:x.index('\n')] if "departure" in i]
    other_tickets = [[int(j) for j in i.strip().split(',')] for i in x[x.index('\n') + 5:]]
    other_tickets = discardInvalidTickets(other_tickets, set.union(*rules))

    possible_rules = {}
    for i in range(len(other_tickets[0])):
        entries = [ticket[i] for ticket in other_tickets]
        possible_rules[i] = [rules.index(rule) for rule in rules if all([entry in rule for entry in entries])]
    possible_rules = np.zeros((len(rules), len(rules)))
    for i in range(len(rules)):
        entries = [ticket[i] for ticket in other_tickets]
        for j in [rules.index(rule) for rule in rules if all([entry in rule for entry in entries])]:
            possible_rules[i,j] = 1
    perfect_matching = maximum_bipartite_matching(csr_matrix(possible_rules))
    return reduce(lambda x,y: x*y, [my_ticket[perfect_matching[i]] for i in required_rules])
   
def discardInvalidTickets(other_tickets, rules):
    return [ticket for ticket in other_tickets if len([number for number in ticket if number not in rules])==0]

def cleanUpRules(rule):
    return set.union(*[set(range(int(i.split('-')[0]), int(i.split('-')[1])+1)) for i in rule.split(': ')[-1].split(' or ')])

def hallsTheorem(possible_rules):
    for i in range(1,len(possible_rules.keys())):
        for combination in itertools.combinations(possible_rules.keys(), i):
            if len(combination) > len(set.union(*[set(possible_rules[key]) for key in combination])):
                print(combination, set.union(*[set(possible_rules[key]) for key in combination]))
                return False
    return True 
if __name__ == "__main__":
    text_file = open("day16/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day16pt1(x))
    print(day16pt2(x))
