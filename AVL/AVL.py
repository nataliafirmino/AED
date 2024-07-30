from Filme import Filme

class AVL:
    def __init__(self):
        self.raiz = None

    def altura (self, subArvore):
        if subArvore == None:
            return 0
        return 1 + max (self.altura(subArvore.esquerdo), self.altura(subArvore.direito))
    
    def fatorBalanceamento (self, subArvore):
        if subArvore == None:
            return 0
        return self.altura(subArvore.esquerdo) - self.altura(subArvore.direito)
    
    def rotacaoSimplesDireita(self, subArvore):
        aux = subArvore.esquerdo
        subArvore.esquerdo = aux.direito
        aux.direito = subArvore
        return aux #setar com filho a esquerda do pai

    def rotacaoSimplesEsquerda (self, subArvore):
        aux = subArvore.direito
        subArvore.direito = aux.esquerdo
        return aux #setar com filho a direita do pai
    
    def imprimirPreOrdem(self, subArvore):
        print(subArvore.id)
        if subArvore.esquerdo != None:
            self.imprimirPreOrdem(subArvore.esquerdo)
        if subArvore.direito != None:
            self.imprimirPreOrdem(subArvore.direito)

    def inserir(self, novoElemento, subArvore):
        if self.raiz == None:
            self.raiz = novoElemento
            return self.raiz
        
        elif novoElemento.id < subArvore.id:
            if subArvore.esquerdo != None:
                self.inserir(novoElemento, subArvore.esquerdo)
            else:
                subArvore.esquerdo = novoElemento
                return novoElemento
            #faltou adicionar a direita da arvore, lembre-se...

        fb = self.fatorBalanceamento(subArvore)
        if (fb > 1 or fb < -1):
            #vai ocorrer algum tipo de rotação
            if (fb > 1):
                #rotação simples a direita
                print("Rotação simples a direita do nó", subArvore.esquerdo)
                noDoTopoRotacao = self.rotacaoSimplesDireita(subArvore)
                if (noDoTopoRotacao.direito == self.raiz):
                    self.raiz = noDoTopoRotacao
                    #falta mais teste e dupla

            if (fb < -1):
                print("Rotação simples a esquerda do nó", subArvore.direito)
                if (noDoTopoRotacao.esquerdo == self.raiz):
                    self.raiz = noDoTopoRotacao
                    

                

        
avl = AVL()
a1 = Filme(50)
a2 = Filme (25)
a3 = Filme (10)    
avl.inserir(a1, avl.raiz)
avl.inserir(a2, avl.raiz)
avl.inserir(a3,avl.raiz)
print("------------\n Imprimindo...")
avl.imprimirPreOrdem(avl.raiz)










