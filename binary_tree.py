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
          atual = atual.dir
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


      
  def printre(self,root):
    root = self.root
    if root ==None:
      pass
    else:
      self.printre(root.esq)
      print("(",root.value,")")
      self.printre(root.dir)


  # def printtree(self, value):
  #   atual = None  
  #   root = self.root 
      
      
  #   # self.printtree(atual.esq)
  #   # print(atual.item,end=" ")
  #   # self.printtree(atual.dir)