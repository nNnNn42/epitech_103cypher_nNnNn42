#!/usr/bin/python3

from math import *
import sys

#si le nombre d'arguments est inférieur à 2, renvoyer une erreur (./103cipher + -h)
if len(sys.argv) < 2:
    exit(84)

#flag de description -h
if sys.argv[1] == '-h':
    print("USAGE\n\t./103cipher message key flag\n")
    print("DESCRIPTION\n\tmessage\ta message, made of ASCII characters")
    print("\tkey    \tthe encryption key, made of ASCII characters")
    print("\tflag   \t0 for the message to be encrypted, 1 to be decrypted")

#si le nombre d'arguments n'est pas égal à 4 renvoyer une erreur (103cipher, message, key, flag)
if len(sys.argv) != 4:
    exit (84)

#si le troisième argument n'est pas égal à 0 ou 1 renvoyer une erreur
if sys.argv[3] != '0' and sys.argv[3] != '1':
   exit (84)

#rajouter 1 à c s'il n'est pas égal à la racine carrée de la longueur du message
a = len(sys.argv[2])
b = float(sqrt(a))
c = int(b)

if c != b:
    c = c + 1

#définit la variable clé au deuxième élement et string au premier puis met les autres à 0
#calcul de la matrice à partir de c, "_" = pas besoin d'un nombre particulier d'iterations
key = sys.argv[2]
string = sys.argv[1]
a = 0
x = 0
nbr = 0
res = 0
matrix = [[0] * c for _ in range(c)]

#imprime la clé de la matrice
#ord = ordinal
print("key matrix:")

while nbr < len(key):
    matrix[a][x] = ord(key[nbr])
    if c - 1 == x:
        a += 1
        x = 0
    else :
        x += 1
    nbr += 1

a = 0
x = 0

for loop in range(c):
    for loop in range(c - 1):
        print("%d\t" %matrix[a][x], end='')
        x += 1
    print("%d" %matrix[a][x], end='')
    print()
    a += 1
    x = 0
print()

a = 0
x = 0
nbr = 0

#imprime le message encrypté
print("Encrypted message:")
while nbr < len(string) :
    if (nbr + 3 > len(string)) and c != 1: 
        if len(string) - nbr == 1 :
            for loop in range(c):
                res = res + matrix[0][x] * ord(string[nbr])
                x += 1
                if x == 3:
                    print("%d" %res, end='')
                else :
                    print("%d" %result, end='')
                result = 0
            nbr = len(string)
        else :
            for loop in range(len(string) - nbr):
                while a < len(string) - nbr :
                    res = res + matrix[a][x] * ord(string[nbr + a])
                    a += 1
                x =+ 1
                if (x == len(string) - nbr):
                    print("%d" %result, end='')
                else:
                    print("%d" %result, end='')
                a = 0
                res = 0
            x = 0
            nbr += len(string) - nbr
    else:
        for loop in range(c):
            while a < c:
                res = res + matrix[a][x] * ord(string[nbr + a])
                a += 1
            x =+ 1
            print("%d" %(res), end='')
            i = 0
            result = 0
        x = 0
        nbr += c
    print()
