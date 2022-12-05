from node import Node


class BinaryTree:
# construtor da raiz  
  def __init__(self ,value=None):
    self.root = None
# add
  def adicionar(self, value):
    # cria primeiro no 
    node = Node(value,None,None)
    atual = None
    root = self.root
    i = None
    # Raiz
    if self.root == None:
      self.root = node
    else:#quando não for raiz 
      atual = root#ponteiro valor atual 
      while i :
        atual = root 
        # crescer para esquerda
        if value < atual.value:
          atual = atual.esq
          # coloca no na esquerda 
          if atual  == None:
            root.esq = node 
        if value > atual.value:
          # cresce para direita 
          autal = atual.dir
          if atual == None:
            # coloca no na direita
            root.dir = node
        return i

  def buscar(self,value):
    if self.root == None:
      return None
      # se arvore vazia 
    atual=self.root
    # enquanto não encontrar 
    while atual.value != value:
      if value < atual.value:
        atual = atual.esq
      else:
        atual = atual.dir 
      if atual == None:
        return None
      return atual