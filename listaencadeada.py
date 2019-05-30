from No import No

class ListaEncadeada:
    """Implementa a classe que opera uma lista encadeada"""

    def __init__(self):
        """Inicia a lista"""
        self.head = None
        self.tail = None

    def prepend(self, v):
        """Adiciona um nó no começo da lista"""
        #criar um nó com v
        no = No(v)
        #apontar para head
        if self.head is None:
            self.head = self.tail = no
        else: 
            no.next = self.head
        #head apontar para novo nó
        self.head = no
        
    def append(self, v):
        """Adiciona um nó no final da lista"""
        #criar nó com v
        no = No(v)
        #final = tail
        if self.head is None:
            self.head = self.tail = no
        final = self.tail
        #final aponta para novo nó
        final.next = no
        #tail é o novo nó
        self.tail = no

    def printLista(self):
        if self.head is None:
            return None
        iter = self.head
        while iter.next is not None:
            print (iter.value)
            iter = iter.next

prepend(0)
append(1)
append(2)
append(3)
prepend(4)
prepend(5)
printLista()