# -*- coding: utf-8 -*-
"""
Created on Sat May  7 13:13:29 2022

@author: mmoec
"""
import numpy as ny
import pygame as pg
from itertools import product
import random as rdn

geheim = rdn.choice(list(product(range(1,7), repeat = 4)))
print(geheim)
print(len(geheim))
master = []
guessgesm = []
position = 0
i = 1
versuche = 1 # Anzahl der Versuche
while i < 5: # Routine zur Generierung der Zufallszahl
        master.append(str(ny.random.randint(0,9)))
        i = i + 1
i = 1
while position != 4: # Solange die Anzahl der richtigen Positionen nicht erraten wurde
    rzahl = 0 # Anzahl der richtigen Zahlen im der Zahlenkette
    position = 0 # Anzahl der richtigen Positionen
    guess = []
    i = 1
    l = 0 # Anzahl der Schreifen für master auslese
    while i < 5: # Routine für Eingabe von vier Zahlen
              zahl = input('Bitte gib eine Zahl zwischen 0 - 9 ein:')
              guess.append(zahl)
              i = i + 1 
    for x in guess: # Auswertung der eingegebenen Zahlen 
        if x == master[l]: # Vergleiche Zahl aus Liste mit Zufallszahl
            position = position + 1 
        else:
            if x in master:
                rzahl = rzahl +1
        l = l + 1
    guessgesm.append(guess)
    print('Anzahl der richtigen Positionen:', position, 'Anzahl der richtigen Zahlen:', rzahl, 'Anzahl der Versuche', versuche)
    xprint = len(guessgesm)
    nprint = 0
    while nprint < xprint:
        print(nprint, guessgesm[nprint])
        nprint = nprint + 1
    versuche = versuche + 1
print('Hurra, du hast die richtige Zahl gefunden und hast', versuche, ' Versuche gebraucht')