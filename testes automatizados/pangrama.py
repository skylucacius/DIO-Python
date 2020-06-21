# coding: utf-8
import string

def pangrama(frase):
    for letra in string.ascii_lowercase:
        return letra in frase

