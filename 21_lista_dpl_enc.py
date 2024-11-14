from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()

print(lista)

lista.insert(0, 'manga')

print(lista)

lista.insert(1, 'abacaxi')

print(lista)

lista.insert(2, 'caju')
lista.insert(3, 'laranja')
lista.insert(4, 'maçã')

print(lista)

lista.insert(3, 'banana')

print(lista)