# -*- coding: utf-8 -*-
from funcoes_arvore_decisao_entropia import partition_entropy_by, build_tree, classify
def create_inputs():
    inputs = [ 
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'no'},   False), 
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'yes'},  False), 
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'no'},     True), 
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'no'},  True), 
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'no'},      True), 
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'yes'},    False), 
        ({'level':'Mid','lang':'R','tweets':'yes','phd':'yes'},        True), 
        ({'level':'Senior','lang':'Python','tweets':'no','phd':'no'}, False), 
        ({'level':'Senior','lang':'R','tweets':'yes','phd':'no'},      True), 
        ({'level':'Junior','lang':'Python','tweets':'yes','phd':'no'}, True), 
         ({'level':'Senior','lang':'Python','tweets':'yes','phd':'yes'},True), 
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'yes'},    True), 
        ({'level':'Mid','lang':'Java','tweets':'yes','phd':'no'},      True), 
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'yes'},False) 
    ] 
    return inputs



if __name__ == "__main__":

    inputs = create_inputs()
    
    for key in ['level','lang','tweets','phd']:
        print key, partition_entropy_by(inputs,key)
    print

    senior_inputs = [(input,label) for input,label in inputs if input["level"] == "Senior"]
    for key in ['lang','tweets','phd']:
        print key,partition_entropy_by(senior_inputs, key)
    
    print "Construindo a Arvore"
    raw_input()
    tree = build_tree(inputs)
    print tree
    raw_input()
    
    print "Junior / Java / tweets / no phd",classify(tree,{
        "level":"Junior",
        "lang":".NET",
        "tweets":"yes",
        "phd":"yes"
    })
    print "Senior", classify(tree,{"level":"Senior"})
    raw_input()



