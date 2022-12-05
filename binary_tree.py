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
    # Raiz
    if self.root == None:
      self.root = node
    else:#quando não for raiz 
      atual = root#ponteiro valor atual 
      while root :
        atual = root 
        # crescer para esquerda
        if value < atual.value:
          atual = atual.esq
          # coloca no na esquerda 
          if atual  == None:
            root.esq = node 
        else:
          # cresce para direita 
          autal.value = atual.dir
          if atual == None:
            # coloca no na direita
            root.dir = node
        return root

             

#   def _remove(self, value, node):
#     if value < node.value:
#       node.left = self._remove(value, node.left)
#     elif value > node.value:
#       node.right = self._remove(value, node.right)
#     else:
#       if node.left is None:
#         return node.right
#       elif node.right is None:
#         return node.left
#       else:
#         def _menorFolha(node=None):
#           while node.left:
#             node = node.left
#           return node.value
#         organize = _menorFolha(node.right)
#         node.data = organize
#         node.right = self._remove(organize, node.right)
#     return node
  
#   def buscar(self, value):
#     if self.root == None:
#       return None
#     atual = self.root # começa a procurar desde raiz
#     while atual.item != value: # enquanto nao encontrou
#       if value < atual.item:
#         atual = atual.esq # caminha para esquerda
#       else:
#         atual = atual.dir # caminha para direita
#         if atual == None:
#           return None # encontrou uma folha -> sai
#       return atual  # terminou o laço while e chegou aqui é pq encontrou item   
# # posordem
#   def imprimir(self,root):
#     self.root = root
#     if root != None:
#      self.imprimir(root.esquerda)
#      self.imprimir(root.direita)
#      pend="")print(root.value,
    
#     return
