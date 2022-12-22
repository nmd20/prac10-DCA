import csv
import string

text = open('declaration.txt').read()
words = text.split()
num_words = len(words)
print("el archivo contiene: " + str(num_words) + "palabras")