# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 12:13:06 2022

@author: mmoec
"""

import sys 
import pygame as pg
class AlienInvation:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(1200,800)
        pg.display.set_caption('Alien Invation')
    def run_game(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                    pg.display.flip()
