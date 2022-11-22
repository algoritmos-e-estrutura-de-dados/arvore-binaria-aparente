from node import Node


class BinaryTree:

  def __init__(self):
    self.root = Node(None, None, None)
    self.root = None

  def adicionar(self, value):
    node = Node(value)
    # Raiz
    if self.root is None:
      self.root = node
    # root = atual valor
    else:
      root = self.root
      while True:
        # adubo
        anterior = root
        # crescer para direita
        if value < root.value:
          root = root.direita
          if root == None:
            anterior.direita = node
          return
      else:
        # crescer para esquerda 
        if value > root.value:
          root = root.esquerda
          if root == None:
            anterior.esquerda = node
          return

  def remover(self, value):
    root = self.root
    # prucurar
    while root.value != value:
      if value < root.value:
        root = root.esquerda
      return
      if value > root.value:
        root = root.direita
      return
    # remover
    if root.value == value:
      root.volue == None

  def percorer(self, value):
    root = self.root
    while root.value != value:
      if value < root.value:
        root = root.esquerda
      return
      if value > root.value:
        root = root.direita
      return
# posordem
  def imprimir(self,root):
    self.root = root
    if root != None:
     self.imprimir(root.esquerda)
     self.imprimir(root.direita)
     print(root.value,end="")
    
    return
