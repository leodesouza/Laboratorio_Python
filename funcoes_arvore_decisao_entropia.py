# -*- coding: utf-8 -*-
from __future__ import division
from collections import Counter, defaultdict
from functools import partial
import math, random

def entropy(classe_probabilidades):
    #dada a lista de possibilidades, computar a entropia
    '''Cálculo de entropioa para verificar o nível de impureza dos dados
    Consulte mais sobre o assunto aqui:
    https://www.maxwell.vrac.puc-rio.br/7587/7587_4.PDF
    '''
    return sum(-p*math.log(p,2) for p in classe_probabilidades)

def class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count for count in Counter(labels).values()]

def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets):
    #Encontrar a entropia dentro da partição de dados do subset
    total_count = sum(len(subset) for subset in subsets)
    return sum(data_entropy(subset) * len(subset) / total_count for subset in subsets)

def partition_by(inputs, attribute):
    # inputs = [({'level':'Senior','lang':'Java','tweets':'no','phd':'no'},False),
    #           ({'level':'Junior','lang':'.NET','tweets':'yes','phd':'yes'},True)  
    #          ]
    # attribue one in ['level','lang','tweets','phd']:
    # pay attention to the following example
    # x in lambda iqual to ({'level':'Senior','lang':'Java','tweets':'no','phd':'no'},False) 
    
    return group_by(inputs, lambda x:x[0][attribute])

def group_by(items, key_fn):
    # items = [({'level':'Senior','lang':'Java','tweets':'no','phd':'no'},False),
    #           ({'level':'Junior','lang':'.NET','tweets':'yes','phd':'yes'},True)  
    #          ]
    groups = defaultdict(list)
    for item in items:
        key = key_fn(item)
        groups[key].append(item)
    return groups




def partition_entropy_by(inputs, attribute):
    # inputs = [({'level':'Senior','lang':'Java','tweets':'no','phd':'no'},False),
    #           ({'level':'Junior','lang':'.NET','tweets':'yes','phd':'yes'},True)  
    #          ]

    # attribue one in ['level','lang','tweets','phd']:
    partitions = partition_by(inputs,attribute)
    return partition_entropy(partitions.values())

def classify(tree, input):
    if tree in [True, False]:
        return tree
    attribute, subtree_dict = tree
    subtree_key = input.get(attribute)

    if subtree_key not in subtree_dict:
        subtree_key = None
    subtree = subtree_dict[subtree_key]
    return classify(subtree, input)

def build_tree(inputs, split_candidates=None):
    if split_candidates is None:
        split_candidates = inputs[0][0].keys()
    
    num_inputs = len(inputs)
    num_trues = len([label for item, label in inputs if label])
    num_falses = num_inputs - num_trues
    
    if num_trues ==0:
        return False
    if num_falses == 0:
        return True

    if not split_candidates:
        return num_trues >= num_falses # return the majority leaf
    
    best_attribute = min(split_candidates, key=partial(partition_entropy_by, inputs))
    partitions = partition_by(inputs, best_attribute)
    new_candidates = [a for a in split_candidates if a != best_attribute]
    subtrees = {attribute:build_tree(subset, new_candidates) for attribute, subset in partitions.iteritems()}
    subtrees[None] = num_trues > num_falses
    return (best_attribute, subtrees)

def forest_clissify(trees, input):
    votes = [classify(tree, input) for tree in trees]
    vote_counts = Counter(votes)
    return vote_counts.most_common(1)[0][0]
