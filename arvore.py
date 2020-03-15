from __future__ import division
from collections import Counter, defaultdict
from functools import partial
import math, random

def entropy(classe_probabilidades):
    return sum(-p*math.log(p,2) for p in classe_probabilidades)

def class_probabilities(labels):
    total_count = len(labels)
    return [count / total_count for count in Counter(labels).values()]

def data_entropy(labeled_data):
    labels = [label for _, label in labeled_data]
    probabilities = class_probabilities(labels)
    return entropy(probabilities)

def partition_entropy(subsets):
    total_count = sum(len(subset) for subset in subsets)
    return sum(data_entropy(subset * len(subset) / total_count for subset in subsets))

def group_by(items, key_fn):
    groups = defaultdict(list)
    for item in items:
        key = key_fn(item)
        groups[key].append(item)

def partition_by(inputs, attribute):
    return group_by(inputs, lambda x:x[0][attribute])


def partition_entropy_by(inputs, attribute):
    partitions = partition_by(inputs,attribute)
    return partition_entropy(partitions)

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
    



if __name__ == "__main__":
    inputs = [({'level':'Senior','lang':'Java','tweets':'no','php':'no'},False),
              ({'level':'Senior','lang':'.NET','tweets':'yes','php':'yes'},False)  
             ]
    
    for key in ['level','lang','tweets','phd']:
        print key, partition_entropy(inputs,key)


