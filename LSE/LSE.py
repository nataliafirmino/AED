from Animal import Animal

class LSE:

    
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

    # recebe como parametro um novo elemento
    def adicionarNoInicio(self, novo):
        novo.prox=self.cabeca #1º passo do quadro
        # verificar se é a primeira inserção, se for 
        # o primeiro elemento (cabeca) também será o último
        # (cauda)
        if (self.cabeca==None):
            self.cauda = novo
        self.cabeca=novo #2º passo do quadro
        self.tamanho+=1#aumentando o tamnho da lista depois de add
        
    def adicionarEmQualquerIndice(self, novo,indice):
        # add no indice 0 é o mesmo que adicionar no início
        if (indice == 0 ):
            self.adicionarNoInicio(novo)
        # condição de qualquer indice diferente de zero
        else:
            #criei uma variável aux para percorrer a lista
            aux=self.cabeca
            # variável para contar a posição
            posicao =0
            #enquanto a posicao for menor que o indice anterior
            #ao que quero adicionar, já que, precisamos apontar
            #o prox elemento do elemento anterior que irá add
            while (posicao< (indice-1)):
                #pulo
                aux=aux.prox
                posicao+=1
            
            novo.prox = aux.prox
            aux.prox=novo
            self.tamanho+=1#aumentando o tamnho da lista depois de add
        
        
    def adicionarNoFim(self,novo):
        self.cauda.prox = novo
        self.cauda = novo
        self.tamanho+=1#aumentando o tamanho da lista depois de add
        

    def removerInicio(self):
        aux = self.cabeca
        self.cabeca = aux.prox # seria a mesma coisa de 
        #self.cabeca = self.cabeca.prox
        aux.prox = None
        self.tamanho-=1#aumentando o tamnho da lista depois de add


    def getTamanho(self):
        return self.tamanho   

    def removerFinal(self):
        aux = self.cabeca
        while aux.prox.prox !=None:
            aux = aux.prox
        aux.prox = None
        self.cauda = aux
        self.tamanho -= 1
        
    def removerIndice(self,indice):
        aux=self.cabeca
        posicao =0

        while (posicao< (indice-1)):
            aux=aux.prox
            posicao+=1
            
        rem=aux.prox
        aux.prox=rem.prox
        rem.prox=None
        self.tamanho-=1
        

listaDeAnimais = LSE()
'''peixe = Animal("Tilápia")
gato = Animal("Gato")
leao = Animal("Leão")
passaro = Animal("Pássaro")

listaDeAnimais.adicionarNoInicio(leao)
listaDeAnimais.adicionarNoInicio(gato)
listaDeAnimais.adicionarNoInicio(peixe)
listaDeAnimais.adicionarEmQualquerIndice(passaro,3)
listaDeAnimais.imprimir()
print ("O tamanho é: ",listaDeAnimais.getTamanho())
listaDeAnimais.removerInicio()
listaDeAnimais.removerFinal()

print ("------------------")
listaDeAnimais.imprimir()
print ("O tamanho é: ",listaDeAnimais.getTamanho())'''