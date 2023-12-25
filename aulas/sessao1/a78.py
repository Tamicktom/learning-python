

set1 = set()

set1.add(1)
set1.add(2)
set1.add(3)
set1.add(2)

print(set1)

set2 = set()

set2.add("limão")
set2.add("laranja")
set2.add("maçã")
set2.add("laranja")

set2.update(set1) # Adiciona os elementos de set1 em set2
set2.discard(2) # Remove o elemento 2 de set2

print(set2)