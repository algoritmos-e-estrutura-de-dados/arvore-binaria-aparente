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
        if value < root:
          root = root.direita
          if root == None:
            anterior.direita = node
          return
      else:
        # crescer para esquerda 
        if value > root:
          root = root.esquerda
          if root == None:
            anterior.esquerda = node
          return

  def _remove(self, value, node):
    if value < node.value:
      node.left = self._remove(value, node.left)
    elif value > node.value:
      node.right = self._remove(value, node.right)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left
      else:
        def _menorFolha(node=None):
          while node.left:
            node = node.left
          return node.value
        organize = _menorFolha(node.right)
        node.data = organize
        node.right = self._remove(organize, node.right)
    return node
  
  def buscar(self, value):
    if self.root == None:
      return None
    atual = self.root # começa a procurar desde raiz
    while atual.item != value: # enquanto nao encontrou
      if value < atual.item:
        atual = atual.esq # caminha para esquerda
      else:
        atual = atual.dir # caminha para direita
        if atual == None:
          return None # encontrou uma folha -> sai
      return atual  # terminou o laço while e chegou aqui é pq encontrou item   
# posordem
  def imprimir(self,root):
    self.root = root
    if root != None:
     self.imprimir(root.esquerda)
     self.imprimir(root.direita)
     print(root.value,end="")
    
    return
