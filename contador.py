import csv
import string

print("¿Cómo se llama el archivo?")
nombre = input()
text = open(nombre).read()
words = text.split()
num_words = len(words)
print("el archivo contiene: " + str(num_words) + "palabras")