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

    def adicionar(self,novo): #fila
        self.cauda.prox = novo
        self.cauda = novo
        self.tamanho+=1#aumentando o tamanho da lista depois de add
    
    def remover(self):
        aux = self.cabeca
        self.cabeca = aux.prox # seria a mesma coisa de 
        #self.cabeca = self.cabeca.prox
        aux.prox = None
        self.tamanho-=1#aumentando o tamnho da lista depois de add


    def getTamanho(self):
        return self.tamanho   