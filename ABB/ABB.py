from No import No 

class ABB:
    def __init__(self) -> None:
        self.raiz = None
    
    def inserir(self, subArvore, novoElemento):
        # se a árvore estiver vazia
        if (self.raiz == None):
            self.raiz = novoElemento
            return
        
        # árvore não vazia
        if (subArvore.conteudo > novoElemento.conteudo):
            if (subArvore.esquerda == None):
                self.raiz.esquerda = novoElemento

            else:
                self.inserir(subArvore.esquerda, novoElemento)

        else:
            if (subArvore.direita == None):
                self.raiz.direita = novoElemento

            else:
                self.inserir(subArvore.direita, novoElemento)

    def imprimirEmOrdem(self, subArvore):
        if subArvore.esquerda != None:
            self.imprimirEmOrdem(subArvore.esquerda)
        print(subArvore.conteudo)

        if subArvore.direita != None:
            self.imprimirEmOrdem(subArvore.direita)
           
    def imprimirPreOrdem(self, subArvore): #visualização de como a árvore realmente é.
        print(subArvore.conteudo)
        if subArvore.esquerda != None:
            self.imprimirPreOrdem(subArvore.esquerda)

        if subArvore.direita != None:
            self.imprimirPreOrdem(subArvore.direita)
        

    def imprimirPosOrdem(self, subArvore):
        if subArvore.esquerda != None:
            self.imprimirPosOrdem(subArvore.esquerda)

        if subArvore.direita != None:
            self.imprimirPosOrdem(subArvore.direita)
        print(subArvore.conteudo)

    def pesquisar(self, subArvore):
        if subArvore == None:
            return 
        else:
            if subArvore.conteudo == self.pesquisar:
                return subArvore
            else:
                if subArvore.conteudo >= subArvore.esquerda:
                    return self.pesquisar (subArvore.esquerda)
                else:
                    return self.pesquisar (subArvore.direita)
