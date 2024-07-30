from Produto import Produto

class LDE:
      
    def __init__ (self):
            #cabeca = atributo para representar o primeiro elemento
            self.cabeca=None
            #cauda = atributo para representar o último elemento
            self.cauda=None
            # atributo para definir o tamanho da lista
            self.tamanho=0

    def imprimir(self):
        if(self.cabeca==None):
            print ("Lista vazia")
            return 
        contador=0
        # aux = primeiro elemento, irá percorrer toda a lista
        aux = self.cabeca
        print(contador, aux.nome)
        # loop enquanto tiver um próximo elemento
        while (aux.prox != None):
            #aux será o próximo elemento
            aux=aux.prox
            contador+=1
            print(contador, aux.nome)

    def adicionarInicio(self, novo):
        #caso minha lista estiver vazia
        if self.cabeca == None:
            self.cabeca = novo
            self.cauda = novo
            self.tamanho+=1

        else:
            self.cabeca.ant = novo
            novo.prox = self.cabeca
            self.cabeca = novo
            self.tamanho+=1


    def adicionarFinal(self, novo):
        if self.cabeca == None:
            self.cabeca = novo
            self.cauda = novo
            self.tamanho+=1

        else:
            novo.ant = self.cauda
            self.cauda.prox = novo
            self.cauda = novo
            self.tamanho+=1 

    def adicionarIndice(self, novo, indice): #adicionar em qualquer índice
         # add no indice 0 é o mesmo que adicionar no início
        if indice == 0:
            self.adicionarNoInicio(novo)
        # condição de qualquer indice diferente de zero
        else:
            #criei uma variável aux para percorrer a lista
            aux=self.cabeca
            # variável para contar a posição
            posicao =0
            #enquanto a posicao for menor que o indice anterior
            #ao que quero adicionar, já que, precisamos apontar
            #o prox elemento do elemento anterior que irá add'''
            while posicao < (indice-1):
                #pulo
                aux=aux.prox
                posicao+=1

            novo.prox = aux.prox
            novo.ant = aux
            aux.prox = novo
            novo.prox.ant = novo
            self.tamanho+=1

    def imprimirInverso(self):
        if self.cabeca == None:
            print('Lista vazia')
            return
        
        contador = self.tamanho - 1
        aux = self.cauda
        print(contador, aux.nome)

        while aux.ant != None:
            aux = aux.ant
            contador-=1
            print(contador, aux.nome)

    def removerFinal(self):
        if self.tamanho ==0:
            print('Lista vazia')

        elif self.tamanho == 1: #método utilizado quando tem apenas um elemento.
            self.cabeca = None
            self.cauda = None
            self.tamanho -=1

        else: #método utilizado quando tem dois elementos ou mais.
            aux = self.cauda.ant
            self.cauda.ant = None
            aux.prox = None
            self.cauda = aux

    def removerIndice(self, indice): #remover em qualquer índice
        aux=self.cabeca
        posicao =0
        while (posicao < (indice-1)):
            aux=aux.prox
            posicao+=1

        remover = aux.prox
        aux.prox = remover.prox
        aux.prox.ant = aux
        remover.ant = None
        remover.prox = None
        self.tamanho-=1
