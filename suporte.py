from arvore_binaria import ArvoreBinaria, No 
#     '+'
#   /    \                   
# 'a'    '*'
#        /  \
#      'b'  '-'
#          /   \
#        '/'  'e'
#       /  \  
#     'c'  'd'

#(a + (b * ((c/d)-e)))

if __name__ == "__main__":
    arvore_binaria = ArvoreBinaria()
    n1 = No('a')
    n2 = No('+')
    n3 = No('*')
    n4 = No('b')
    n5 = No('-')
    n6 = No('/')
    n7 =  No('c')
    n8 = No('d')
    n9 = No('e')

    n6.esquerda = n7
    n6.direita = n8
    n5.esquerda = n6
    n5.direita = n9
    n3.esquerda = n4
    n3.direita = n5
    n2.esquerda = n1
    n3.direita = n3
    arvore_binaria.raiz = n2
