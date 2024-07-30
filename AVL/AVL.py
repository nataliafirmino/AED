from Filme import Filme

class AVL:
    def __init__(self):
        self.raiz = None

    def altura (self, subArvore):
        if subArvore == None:
            return 0
        return 1 + max (self.altura(subArvore.esquerdo), self.altura(subArvore.direita))
    
    def fatorBalanceamento (self, subArvore):
        if subArvore == None:
            return 0
        return self.altura(subArvore.esquerdo) - subArvore.altura(subArvore.direito)
    
    def rotacaoSimplesDireita(self, subArvore):
        aux = subArvore.esquerdo
        subArvore.esquerdo = aux.direito
        return aux #setar com filho a esquerda do pai

    def rotacaoSimplesEsquerda (self, subArvore):
        aux = subArvore.direito
        subArvore.direito = aux.esquerdo
        return aux #setar com filho a direita do pai
    




