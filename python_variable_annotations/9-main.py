#!/usr/bin/env python3

element_length =  __import__('9-element_length').element_length

lista = ["hola", (1, 2, 3, 4), ['h', 'o', 'l', 'a']]
print(element_length.__annotations__)
print(element_length(lista))
