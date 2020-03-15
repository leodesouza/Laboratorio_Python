# -*- coding: utf-8 -*-
class No:
    def __init__(self, data):
        self.data = data
        self.esquerda = None
        self.direita = None
    
    def __str__(self):
        return str(self.data)

class ArvoreBinaria:
    def __init__(self, data=None):  
        if data:                  
            no = No(data)
            self.raiz = no
        else:
            self.raiz = None
    
    # Percurso em ordem simétrica (o correto é "inorder" em inglês)
    def simetric_traversal(self, no=None):
        "Nó"
        if no is None:
            no = self.raiz

        if no.esquerda:
            print('('),
            self.simetric_traversal(no.esquerda)

        print(no),

        if no.direita:
            self.simetric_traversal(no.direita)
            print(')'), #comma in the end to avoid breaking line
        
        #print('')#break line 
        

if __name__ =="__main__":
    # arvore_binaria = ArvoreBinaria(7)
    # arvore_binaria.raiz.esquerda = No(18)
    # arvore_binaria.raiz.direita = No(14)

    # print(arvore_binaria.raiz)
    # print(arvore_binaria.raiz.esquerda)
    # print(arvore_binaria.raiz.direita)
    # raw_input("Digite qualquer tecla para finalizar")
    
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
    n2.direita = n3
    arvore_binaria.raiz = n2

    arvore_binaria.simetric_traversal()


