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
        while iter is not None:
            print (iter.value)
            iter = iter.next

    def remove_if(self, value):
        v = value
        iter = self.head
        if iter is None:
            return 
        elif iter.next is None:
            self.head = None
            self.tail = None
        elif iter == v:
            self.head = iter.next
        else:
            while iter is not v:
                ant = iter
                iter = iter.next
                if iter == v and iter.next is not None:
                    ant = iter.next
                if iter == v and iter.next is None:
                    self.tail = ant


lista = ListaEncadeada()
lista.remove_if(4)
lista.prepend(0)
lista.append(1)
lista.append(2)
lista.append(3)
lista.prepend(4)
lista.prepend(5)
lista.remove_if(4)
lista.printLista()
