# IMPORT
import pygame, sys
from math import *
from random import *
from pygame.locals import *
import numpy
from os import path, environ
import ui

environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

# CONSTANT VARIABLES
# COLORS
WHITE = (255, 255, 255)
WHITE2 = (200, 200, 200)
GREEN = (150, 250, 150)
GREEN2 = (100, 250, 100)
GREEN3 = Color(30, 150, 50)
BLUE = Color(20, 130, 128)
BLUE2 = Color(20, 50, 80)
BLUE3 = Color(20, 150, 200)
RED = Color(205, 10, 10)
RED2 = Color(170, 40, 40)
RED3 = Color(50, 0, 20)
PURPLE = Color(180, 20, 200)
GRAY = Color(30, 30, 30)
GRAY2 = Color(50, 50, 50)
BLACK=Color(20, 20, 20)
GOLD = Color(165, 130, 70)
BACKGROUND_COLOR = GRAY
COLOR2 = GRAY2
COLOR3 = GOLD

# GAME SETTINGS

WORLD_SIZE_X = 2500
WORLD_SIZE_Y = 2500

SPAWN_POINT = (300, 300)

KILL_TIMER = 250
KILL_MESSAGE = ["KILL", "DOUBLE KILL", "TRIPLE KILL"]

CAM_RANGE_X = 250
CAM_RANGE_Y = 100
SCROLLING_SPEED = 1.5

# GUNS
GUN_DAMAGE = 270
GUN_SPEED = 26
GUN_RANGE = 1800
GUN_MAX_AMMO = 32
GUN_INTERVAL = 85
GUN_RELOAD = 90
GUN_SPREAD = 10

D_SCALE = 1
I_SCALE = 1


GUN91 = {"slot":"gun1", "damage":30*D_SCALE, "c_down":0 ,"interval":8*I_SCALE, "reload":40, "speed":29, "ammo":14, "max_ammo":14, "size":10,
        "range": 750, "price":12500, "name":"", "type":2, "rounds" : 2, "chamber":0, "burst_interval":2, "spread":2}

GUN92 = {"slot":"gun1", "damage": 18*D_SCALE, "c_down":0 ,"interval":5*I_SCALE, "reload":70, "speed":27, "ammo":18, "max_ammo":18, "size":10,
        "range": 650, "price":12500, "name":"", "type":0, "rounds" : 1, "spread":5}


GUN93 = {"slot":"gun1", "damage": 250*D_SCALE, "c_down":0 ,"interval":75*I_SCALE, "reload":75, "speed":30, "ammo":1, "max_ammo":1, "size":15,
        "range": 1800, "price":41500, "name":"", "type":4, "rounds" : 1, "spread":0}

GUN94 = {"slot":"gun1", "damage": 45*D_SCALE, "c_down":0 ,"interval":15*I_SCALE, "reload":60, "speed":27, "ammo":14, "max_ammo":14, "size":15,
        "range": 850, "price":26800, "name":"", "type":2, "rounds" : 2, "chamber":0, "burst_interval":3, "spread":2}

GUN95 = {"slot":"gun1", "damage": 45*D_SCALE, "c_down":0 ,"interval":20*I_SCALE, "reload":70, "speed":27, "ammo":18, "max_ammo":18, "size":15,
        "range": 850, "price":26800, "name":"", "type":2, "rounds" : 3, "chamber":0, "burst_interval":2, "spread":2}


GUN96 = {"slot":"gun1", "damage": 30*D_SCALE, "c_down":0 ,"interval":55*I_SCALE, "reload":55, "speed":28, "ammo":9, "max_ammo":9, "size":15,
        "range": 600, "price": 37250, "name":"", "type":3, "rounds" : 9, "spread":5}


GUN97= {"slot":"gun1", "damage": 30*D_SCALE, "c_down":0 ,"interval":5*I_SCALE, "reload":60, "speed":25, "ammo":28, "max_ammo":28, "size":15,
        "range": 650, "price": 12450, "name":"", "type":0, "rounds" : 1, "spread":4}

GUN999 = {"slot":"gun1", "damage": 34*D_SCALE, "c_down":0 ,"interval":3*I_SCALE, "reload":75, "speed":27, "ammo":32, "max_ammo":32, "size":15,
        "range": 625, "price": 0, "name":"", "type":0, "rounds" : 1, "spread":3}


# BOMBS

BOMB1 = {"slot":"bomb", "damage": 140*D_SCALE, "pos":[], "blast": 180, "radius":18, "range":700, "c_down":0,
         "reload":130, "life":100,  "speed":7,"slow":0.2, "slow_duration":200, "dir":[], "player":False, "active":False}

# SHIPS

SHIP_SPEED = 5
SHIP_HEALTH = 240
SHIP_DAMAGE = 5
SHIP_SIZE=32

SHIP1_COLOR = (110, 180, 110)
SHIP2_COLOR = (100, 160, 160)
SHIP3_COLOR = (130, 80, 80)
SHIP4_COLOR = (120, 110, 140)
SHIP5_COLOR = (100, 120, 180)
SHIP6_COLOR = (99,107,70)
SHIP7_COLOR = (120, 120, 240)
SHIP8_COLOR = (42, 89, 211)
SHIP9_COLOR = (93,83,94)
SHIP10_COLOR =(14,11,22)
SHIP11_COLOR = (89,77,70)
SHIP12_COLOR = (165,28,48)
SHIP13_COLOR = (229,236,233)
SHIP14_COLOR = (209,178,128)

SHIP1_COLOR2 = (220, 220, 255)
SHIP2_COLOR2 = (220, 220, 255)
SHIP3_COLOR2 = (220, 220, 255)
SHIP4_COLOR2 = (220, 220, 255)
SHIP5_COLOR2 = (220, 220, 255)
SHIP6_COLOR2 = (220, 220, 255)
SHIP7_COLOR2 = (40, 130, 155)
SHIP8_COLOR2 = (220, 120, 155)
SHIP9_COLOR2 = (236,150,164)
SHIP10_COLOR2 =(162,57,202)
SHIP11_COLOR2 = (209,178,128)
SHIP12_COLOR2 = (35, 75, 105)
SHIP13_COLOR2 = (105, 105, 105)
SHIP14_COLOR2 = (105, 105, 105)



SHIP1 = {"slot":"ship", "name": "", "price":0, "speed": 4, "base_speed": 4, "health":80, "max_health":80, "damage":1, "size":25, "color" : SHIP1_COLOR, "color2": SHIP1_COLOR2, "gun_amount":2}
SHIP2 = {"slot":"ship", "name": "", "price":4200, "speed": 4.3, "base_speed": 4.3, "health":120, "max_health":120, "damage":1.2, "size":28, "color" : SHIP2_COLOR, "color2": SHIP2_COLOR2, "gun_amount":2}

SHIP3= {"slot":"ship", "name": "", "price":8200, "speed": 4.3, "base_speed": 4.3, "health":100, "max_health":100, "damage": 1.6, "size":26, "color" : SHIP3_COLOR, "color2": SHIP3_COLOR2, "gun_amount":2}
SHIP4 = {"slot":"ship", "name": "", "price":8200, "speed": 4.3, "base_speed": 4.3, "health":130, "max_health":130, "damage": 1.4, "size": 29, "color" : SHIP4_COLOR, "color2": SHIP4_COLOR2, "gun_amount":2}

SHIP5 = {"slot":"ship", "name": "", "price":12500, "speed": 4.5, "base_speed": 4.5, "health":140, "max_health":140, "damage":1.7, "size":22, "color" : SHIP5_COLOR, "color2": SHIP5_COLOR2, "gun_amount":2}
SHIP6 = {"slot":"ship", "name": "", "price":12500, "speed": 4.5, "base_speed": 4.3, "health":140, "max_health":140, "damage": 1.9, "size": 26, "color" : SHIP6_COLOR, "color2": SHIP6_COLOR2, "gun_amount":2}

SHIP7= {"slot":"ship", "name": "", "price":23500, "speed": 5, "base_speed": 5, "health":160, "max_health":160, "damage":2.1, "size":25, "color" : SHIP7_COLOR, "color2": SHIP7_COLOR2, "gun_amount":2}
SHIP8 = {"slot":"ship", "name": "", "price":23500, "speed": 4.85, "base_speed": 4.85, "health":140, "max_health":140, "damage": 2.4, "size": 25, "color" : SHIP8_COLOR, "color2": SHIP8_COLOR2, "gun_amount":2}


SHIP9 = {"slot":"ship", "name": "", "price":48000, "speed": 5, "base_speed": 5, "health":160, "max_health":160, "damage": 2.3, "size":28, "color" : SHIP9_COLOR, "color2": SHIP9_COLOR2, "gun_amount":2}
SHIP10 = {"slot":"ship", "name": "", "price":48000, "speed": 5, "base_speed": 5, "health":160, "max_health":160, "damage": 2.75, "size":28, "color" : SHIP10_COLOR, "color2": SHIP10_COLOR2, "gun_amount":2}

SHIP11 = {"slot":"ship", "name": "", "price":48000, "speed": 5, "base_speed": 5, "health":180, "max_health":180, "damage": 2.5, "size":30, "color" : SHIP11_COLOR, "color2": SHIP11_COLOR2, "gun_amount":2}

SHIP12 = {"slot":"ship", "name": "", "price":128000, "speed": 6, "base_speed": 6, "health":220, "max_health":220, "damage": 2.25, "size":35, "color" : SHIP12_COLOR, "color2": SHIP12_COLOR2, "gun_amount":2}
SHIP13 = {"slot":"ship", "name": "", "price":128000, "speed": 5.5, "base_speed": 5.5, "health":240, "max_health":240, "damage": 2.5, "size":38, "color" : SHIP13_COLOR, "color2": SHIP13_COLOR2, "gun_amount":2}
SHIP14 = {"slot":"ship", "name": "", "price":128000, "speed": 6, "base_speed": 6, "health":260, "max_health":260, "damage": 2, "size":38, "color" : SHIP14_COLOR, "color2": SHIP14_COLOR2,"gun_amount":2}



# ENEMY GUNS

GUN1 = {"slot":"gun", "damage": 25, "c_down":0 ,"interval":10, "reload":35, "speed":22, "ammo":24, "max_ammo":24, "size":15,
        "range": 650, "price": 650, "name":"enemy gun 1", "type":1, "rounds" : 1, "spread":5}
GUN2 = {"slot":"gun", "damage": 70, "c_down":0 ,"interval":20, "reload":55, "speed":25, "ammo":12, "max_ammo":12, "size":15,
        "range": 900, "price": 650, "name":"enemy gun 2", "type":1, "rounds" : 1, "spread":2}
GUN3 = {"slot":"gun", "damage": 22, "c_down":0 ,"interval":13, "reload":25, "speed":23, "ammo":24, "max_ammo":24, "size":15,
        "range": 450, "price": 650, "name":"enemy gun 3", "type":3, "rounds" : 4, "spread":10}
GUN4 = {"slot":"gun2", "damage": 35, "c_down":0 ,"interval":10, "reload":60, "speed":24, "ammo":24, "max_ammo":24, "size":15,
        "range": 800, "price":1200, "name":"enemy gun 4", "type":2, "rounds" : 4, "chamber":0, "burst_interval":2, "spread":3}
GUN5 = {"slot":"gun", "damage": 40, "c_down":0 ,"interval":5, "reload":35, "speed":21, "ammo":20, "max_ammo":20, "size":15,
        "range": 600, "price": 650, "name":"enemy gun 1", "type":1, "rounds" : 1, "spread":7}
GUN6 = {"slot":"gun2", "damage": 55, "c_down":0 ,"interval":13, "reload":85, "speed":24, "ammo":28, "max_ammo":28, "size":15,
        "range": 750, "price": 0, "name":"Kammerjäger", "type":3, "rounds" : 7, "spread":8}

GUN11 = {"slot":"gun", "damage": 40, "c_down":0 ,"interval":8, "reload":25, "speed":24, "ammo":24, "max_ammo":24, "size":15,
        "range": 650, "price": 650, "name":"enemy gun 11", "type":1, "rounds" : 1, "spread":5}
GUN12 = {"slot":"gun", "damage": 130, "c_down":0 ,"interval":20, "reload":55, "speed":25, "ammo":12, "max_ammo":12, "size":15,
        "range": 950, "price": 650, "name":"enemy gun 12", "type":1, "rounds" : 1, "spread":2}
GUN13 = {"slot":"gun", "damage": 45, "c_down":0 ,"interval":13, "reload":25, "speed":25, "ammo":24, "max_ammo":24, "size":15,
        "range": 500, "price": 650, "name":"enemy gun 13", "type":3, "rounds" : 4, "spread":10}
GUN14 = {"slot":"gun2", "damage": 60, "c_down":0 ,"interval":15, "reload":60, "speed":25, "ammo":24, "max_ammo":24, "size":15,
        "range": 850, "price":1200, "name":"enemy gun 14", "type":2, "rounds" : 8, "chamber":0, "burst_interval":3, "spread":3}
GUN15 = {"slot":"gun", "damage": 45, "c_down":0 ,"interval":3, "reload":35, "speed":23, "ammo":20, "max_ammo":20, "size":15,
        "range": 650, "price": 650, "name":"enemy gun 15", "type":1, "rounds" : 1, "spread":7}
GUN16 = {"slot":"gun2", "damage": 100, "c_down":0 ,"interval":6, "reload":55, "speed":26, "ammo":21, "max_ammo":21, "size":15,
        "range": 850, "price": 0, "name":"Kammerjäger 2", "type":3, "rounds" : 7, "spread":6}

#ENEMIES

ENEMY1 = {"health" : 220, "max_health" : 220, "center" : [], "dir" : [], "value":80,
          "gun" : GUN1, "dead":False, "speed":3, "color":(200, 50, 50), "size":15, "base_speed":2.5, "slow_duration":0}

ENEMY2 = {"health" : 250, "max_health" : 250, "center" : [], "dir" : [], "value":100,
          "gun" : GUN3, "dead":False, "speed":3.5, "color":(200, 50, 150), "size":14, "base_speed":3, "slow_duration":0}

ENEMY3 = {"health" : 360, "max_health" : 360, "center" : [], "dir" : [], "value":120,
          "gun" : GUN2, "dead":False, "speed":3, "color":(20, 200, 100), "size":25, "base_speed":2.5, "slow_duration":0}

ENEMY4 = {"health" : 300, "max_health" : 300, "center" : [], "dir" : [], "value":140,
          "gun" : GUN4, "dead":False, "speed":4, "color":(200, 210, 220), "size":18, "base_speed":3.5, "slow_duration":0}

ENEMY5 = {"health" : 340, "max_health" : 340, "center" : [], "dir" : [], "value":150,
          "gun" : GUN5, "dead":False, "speed":3.4, "color":(120, 210, 40), "size":25, "base_speed":2.9, "slow_duration":0}

ENEMY6 = {"health" : 350, "max_health" : 350, "center" : [], "dir" : [], "value":170,
          "gun" : GUN2, "dead":False, "speed":3.8, "color":(50, 50, 150), "size":18, "base_speed":3.3, "slow_duration":0}

ENEMY7 = {"health" : 380, "max_health" : 380, "center" : [], "dir" : [], "value":190,
          "gun" : GUN3, "dead":False, "speed":3.5, "color":(70, 210, 240), "size":22, "base_speed":3, "slow_duration":0}

ENEMY8 = {"health" : 400, "max_health" : 400, "center" : [], "dir" : [], "value":250,
          "gun" : GUN4, "dead":False, "speed":3, "color":(150, 190, 20), "size":18, "base_speed":2.5, "slow_duration":0}

ENEMY9 = {"health" : 1500, "max_health" : 1500, "center" : [], "dir" : [], "value":300,
          "gun" : GUN5, "dead":False, "speed":2.7, "color":(205, 205, 40), "size":30, "base_speed":2.2, "slow_duration":0}

ENEMY10 = {"health" : 3000, "max_health" : 3500, "center" : [], "dir" : [], "value":2500,
          "gun" : GUN6, "dead":False, "speed":2.9, "color":(180, 20, 200), "size":45, "base_speed":2.4, "slow_duration":0}

ENEMY11 = {"health" : 400, "max_health" : 400, "center" : [], "dir" : [], "value":150,
          "gun" : GUN11, "dead":False, "speed":3.5, "color":(113,3,22), "size":20, "base_speed":3, "slow_duration":0}

ENEMY12 = {"health" : 480, "max_health" : 480, "center" : [], "dir" : [], "value":250,
          "gun" : GUN13, "dead":False, "speed":3.5, "color":(97,15,127), "size":19, "base_speed":3, "slow_duration":0}

ENEMY13 = {"health" : 500, "max_health" : 500, "center" : [], "dir" : [], "value":250,
          "gun" : GUN12, "dead":False, "speed":2.2, "color":(20, 200, 100), "size":30, "base_speed":1.7, "slow_duration":0}

ENEMY14 = {"health" : 400, "max_health" : 400, "center" : [], "dir" : [], "value":300,
          "gun" : GUN14, "dead":False, "speed":4.2, "color":(200, 210, 220), "size":23, "base_speed":3.7, "slow_duration":0}

ENEMY15 = {"health" : 440, "max_health" : 440, "center" : [], "dir" : [], "value":300,
          "gun" : GUN15, "dead":False, "speed":3.4, "color":(120, 210, 40), "size":28, "base_speed":2.9, "slow_duration":0}

ENEMY16 = {"health" : 350, "max_health" : 350, "center" : [], "dir" : [], "value":300,
          "gun" : GUN12, "dead":False, "speed":4.5, "color":(50, 50, 150), "size":16, "base_speed":4, "slow_duration":0}

ENEMY17 = {"health" : 580, "max_health" : 580, "center" : [], "dir" : [], "value":350,
          "gun" : GUN13, "dead":False, "speed":2.4, "color":(70, 210, 240), "size":31, "base_speed":1.9, "slow_duration":0}

ENEMY18 = {"health" : 650, "max_health" : 650, "center" : [], "dir" : [], "value":380,
          "gun" : GUN14, "dead":False, "speed":2.5, "color":(150, 190, 20), "size":27, "base_speed":2, "slow_duration":0}

ENEMY19 = {"health" : 2500, "max_health" : 2500, "center" : [], "dir" : [], "value": 2500,
          "gun" : GUN15, "dead":False, "speed":2.7, "color":(205, 205, 40), "size":35, "base_speed":2.2, "slow_duration":0}

ENEMY20 = {"health" : 8000, "max_health" : 8000, "center" : [], "dir" : [], "value":5000,
          "gun" : GUN16, "dead":False, "speed":3.2, "color":(120, 20, 140), "size": 50, "base_speed":2.7, "slow_duration":0}



LEVELS= [
["", ENEMY1],
["",ENEMY1, ENEMY1, ENEMY1,ENEMY1, ENEMY1,ENEMY2],
["",ENEMY1, ENEMY1, ENEMY2,ENEMY2,ENEMY2],
["",ENEMY2, ENEMY1, ENEMY1, ENEMY2, ENEMY2,ENEMY2,ENEMY2],
["",ENEMY2, ENEMY2, ENEMY2, ENEMY2, ENEMY2,ENEMY2,ENEMY2,ENEMY2],
["",ENEMY3, ENEMY1, ENEMY1, ENEMY1, ENEMY2],
["",ENEMY3, ENEMY3, ENEMY3, ENEMY3, ENEMY1, ENEMY2, ENEMY1, ENEMY2],
["",ENEMY1, ENEMY1, ENEMY2, ENEMY2, ENEMY3, ENEMY3, ENEMY3, ENEMY3, ENEMY3],
["",ENEMY1, ENEMY1, ENEMY3, ENEMY3, ENEMY3],
["",ENEMY1, ENEMY3, ENEMY3, ENEMY3, ENEMY1, ENEMY3, ENEMY3, ENEMY3, ENEMY4],
["",ENEMY4, ENEMY3,ENEMY4, ENEMY3,ENEMY4, ENEMY3, ENEMY2],
["",ENEMY4, ENEMY4, ENEMY3, ENEMY3, ENEMY2, ENEMY1, ENEMY1],
["",ENEMY4, ENEMY3, ENEMY3, ENEMY3, ENEMY4, ENEMY3, ENEMY3, ENEMY3],
["",ENEMY2, ENEMY2, ENEMY2, ENEMY5],
["",ENEMY5, ENEMY5, ENEMY3, ENEMY3],
["",ENEMY5, ENEMY3, ENEMY5, ENEMY3, ENEMY2, ENEMY1],
["",ENEMY5, ENEMY5, ENEMY4, ENEMY4, ENEMY3, ENEMY3, ENEMY5, ENEMY3,],
["",ENEMY6, ENEMY3, ENEMY3, ENEMY3, ENEMY3],
["",ENEMY6, ENEMY5,ENEMY5, ENEMY5, ENEMY5, ENEMY5],
["",ENEMY6, ENEMY6, ENEMY6],
["",ENEMY6, ENEMY1, ENEMY5, ENEMY6],
["",ENEMY6, ENEMY5],
["",ENEMY6, ENEMY5, ENEMY2, ENEMY2, ENEMY3],
["",ENEMY6, ENEMY6, ENEMY6, ENEMY5, ENEMY5, ENEMY2, ENEMY2],
["",ENEMY7,ENEMY7,ENEMY7,ENEMY7],
["",ENEMY7, ENEMY2, ENEMY2,ENEMY7,ENEMY7,ENEMY7],
["",ENEMY7, ENEMY5, ENEMY5, ENEMY5, ENEMY5, ENEMY5, ENEMY4,ENEMY1],
["",ENEMY7, ENEMY7, ENEMY7, ENEMY5, ENEMY5],
["",ENEMY8, ENEMY7, ENEMY5, ENEMY5],
["",ENEMY8, ENEMY2, ENEMY2],
["",ENEMY8, ENEMY3, ENEMY3, ENEMY3, ENEMY2],
["",ENEMY8, ENEMY8, ENEMY7, ENEMY7, ENEMY5, ENEMY4, ENEMY4, ENEMY3],
["",ENEMY9, ENEMY3, ENEMY3, ENEMY3],
["",ENEMY9, ENEMY3,  ENEMY5, ENEMY5],
["",ENEMY9, ENEMY5, ENEMY5, ENEMY8, ENEMY8, ENEMY5, ENEMY3],
["",ENEMY9, ENEMY9, ENEMY8, ENEMY8, ENEMY7, ENEMY7, ENEMY7, ENEMY7, ENEMY5],
["Boss battle",ENEMY10, ENEMY6, ENEMY6, ENEMY5, ENEMY5, ENEMY5, ENEMY6, ENEMY6, ENEMY5, ENEMY5, ENEMY5],
["", ENEMY11, ENEMY1, ENEMY8, ENEMY7, ENEMY7, ENEMY7, ENEMY7, ENEMY7, ENEMY7, ENEMY7, ENEMY7],
["",ENEMY11, ENEMY11, ENEMY11, ENEMY1, ENEMY1, ENEMY8, ENEMY7, ENEMY7, ENEMY7, ENEMY7],
["",ENEMY12, ENEMY5, ENEMY5, ENEMY5, ENEMY8, ENEMY7, ENEMY7, ENEMY7, ENEMY7],
["",ENEMY12, ENEMY11, ENEMY11, ENEMY1, ENEMY2, ENEMY8, ENEMY7, ENEMY7, ENEMY7, ENEMY7],
["",ENEMY12, ENEMY12, ENEMY12, ENEMY2, ENEMY2, ENEMY8, ENEMY7, ENEMY7, ENEMY7, ENEMY7],
["",ENEMY13, ENEMY1, ENEMY2, ENEMY3, ENEMY7, ENEMY7, ENEMY5, ENEMY4, ENEMY4],
["",ENEMY13, ENEMY13, ENEMY3, ENEMY3, ENEMY3, ENEMY6, ENEMY6, ENEMY6, ENEMY5, ENEMY5, ENEMY2, ENEMY2],
["",ENEMY11, ENEMY11, ENEMY12, ENEMY13, ENEMY5, ENEMY11, ENEMY1, ENEMY2, ENEMY8, ENEMY7, ENEMY7, ENEMY7, ENEMY7],
["",ENEMY11, ENEMY11, ENEMY13, ENEMY13, ENEMY6, ENEMY6, ENEMY6, ENEMY6, ENEMY6, ENEMY6, ENEMY6, ENEMY6],
["",ENEMY14, ENEMY7, ENEMY7, ENEMY5,ENEMY6, ENEMY6, ENEMY6, ENEMY5, ENEMY5, ENEMY2, ENEMY2],
["",ENEMY14, ENEMY13, ENEMY12, ENEMY7, ENEMY6, ENEMY11, ENEMY1, ENEMY2, ENEMY8, ENEMY7, ENEMY7, ENEMY7, ENEMY7],
["",ENEMY14, ENEMY13, ENEMY12, ENEMY11, ENEMY11],
["",ENEMY14, ENEMY13, ENEMY13, ENEMY13, ENEMY4],
["",ENEMY15, ENEMY12, ENEMY2, ENEMY2, ENEMY2,ENEMY6, ENEMY6, ENEMY6, ENEMY5, ENEMY5, ENEMY2, ENEMY2],
["",ENEMY15, ENEMY15, ENEMY13, ENEMY13, ENEMY11, ENEMY1, ENEMY2, ENEMY8, ENEMY7, ENEMY7, ENEMY7, ENEMY7],
["",ENEMY13, ENEMY13, ENEMY13, ENEMY12, ENEMY12],
["",ENEMY15, ENEMY3, ENEMY3, ENEMY3, ENEMY3, ENEMY3, ENEMY3, ENEMY3, ENEMY3, ENEMY3, ENEMY3, ENEMY3, ENEMY3, ENEMY3],
["",ENEMY16, ENEMY13, ENEMY13, ENEMY3,ENEMY6, ENEMY6, ENEMY6, ENEMY5, ENEMY5, ENEMY2, ENEMY2],
["",ENEMY16, ENEMY15, ENEMY14, ENEMY12, ENEMY11, ENEMY1, ENEMY2, ENEMY8, ENEMY7, ENEMY7, ENEMY7, ENEMY7],
["",ENEMY16, ENEMY16, ENEMY16, ENEMY12, ENEMY12, ENEMY16, ENEMY12, ENEMY12],
["",ENEMY16, ENEMY11, ENEMY15, ENEMY16, ENEMY2, ENEMY16, ENEMY12, ENEMY12],
["",ENEMY16, ENEMY15, ENEMY8, ENEMY8, ENEMY11, ENEMY1, ENEMY2, ENEMY8, ENEMY7, ENEMY7, ENEMY7, ENEMY7],
["",ENEMY16, ENEMY15, ENEMY12, ENEMY12, ENEMY3, ENEMY15, ENEMY12, ENEMY12, ENEMY3],
["",ENEMY16, ENEMY16, ENEMY16, ENEMY15, ENEMY15,ENEMY16, ENEMY13, ENEMY13, ENEMY3,ENEMY6, ENEMY6],
["",ENEMY17, ENEMY1, ENEMY3, ENEMY5, ENEMY7, ENEMY15, ENEMY12, ENEMY12, ENEMY3],
["",ENEMY17, ENEMY12, ENEMY3, ENEMY3, ENEMY3, ENEMY16, ENEMY12, ENEMY12],
["",ENEMY17, ENEMY15, ENEMY15, ENEMY5, ENEMY2, ENEMY15, ENEMY12, ENEMY12, ENEMY3],
["",ENEMY17, ENEMY17, ENEMY17, ENEMY15, ENEMY12,ENEMY16, ENEMY13, ENEMY13, ENEMY3,ENEMY6, ENEMY6],
["",ENEMY18, ENEMY12, ENEMY12, ENEMY12, ENEMY15, ENEMY12, ENEMY12, ENEMY3],
["",ENEMY18, ENEMY18, ENEMY18, ENEMY18, ENEMY9, ENEMY16, ENEMY12, ENEMY12],
["",ENEMY18, ENEMY13, ENEMY13, ENEMY13, ENEMY6, ENEMY6, ENEMY11, ENEMY11, ENEMY11],
["",ENEMY18, ENEMY18, ENEMY17, ENEMY17, ENEMY15, ENEMY8, ENEMY8,ENEMY16, ENEMY13, ENEMY13, ENEMY3,ENEMY6],
["",ENEMY19, ENEMY13, ENEMY13, ENEMY5, ENEMY5, ENEMY2, ENEMY2, ENEMY2, ENEMY5, ENEMY16, ENEMY12, ENEMY12],
["",ENEMY19, ENEMY13,  ENEMY15, ENEMY15, ENEMY12, ENEMY4, ENEMY3, ENEMY3, ENEMY16, ENEMY12, ENEMY12],
["",ENEMY19, ENEMY15, ENEMY15, ENEMY18, ENEMY18, ENEMY6, ENEMY4, ENEMY4, ENEMY16, ENEMY12, ENEMY12],
["",ENEMY19, ENEMY19, ENEMY18, ENEMY18, ENEMY17, ENEMY17, ENEMY7, ENEMY9, ENEMY9, ENEMY16, ENEMY12, ENEMY12],
["Boss battle",ENEMY20, ENEMY19, ENEMY5, ENEMY5, ENEMY12, ENEMY12, ENEMY11, ENEMY12, ENEMY2, ENEMY2, ENEMY3, ENEMY16, ENEMY12, ENEMY12, ENEMY16, ENEMY12, ENEMY12]
    ]

#BOOST

BOOST_CD = 100
BOOST_DUR = 12

print("aantal levels:" +str(len(LEVELS)))

##ENEMY_SPAWNS = [[int(GAME_SIZE_X/10), int(GAME_SIZE_Y/10)],
##                [int(GAME_SIZE_X/10), int(GAME_SIZE_Y - GAME_SIZE_Y/10)],
##                [int(GAME_SIZE_X - GAME_SIZE_X/10), int(GAME_SIZE_Y/10)],
##                [int(GAME_SIZE_X - GAME_SIZE_X/10), int(GAME_SIZE_Y - GAME_SIZE_Y/10)],
##                [int(GAME_SIZE_X/2), int(GAME_SIZE_Y/10)],
##                [int(GAME_SIZE_X/2), int(GAME_SIZE_Y-GAME_SIZE_Y/10)],
##                [int(GAME_SIZE_X/10), int(GAME_SIZE_Y/2)],
##                [int(GAME_SIZE_X-GAME_SIZE_X/10), int(GAME_SIZE_Y/2)],]
ENEMY_SPAWNS = [
                [2000, 2000],   [2000, 2100],   [2000, 2200],   [2000, 2300],   [2000, 2400],
                [2100, 2000],   [2100, 2100],   [2100, 2200],   [2100, 2300],   [2100, 2400],
                [2200, 2000],   [2200, 2100],   [2200, 2200],   [2200, 2300],   [2200, 2400],
                [2300, 2000],   [2300, 2100],   [2300, 2200],   [2300, 2300],   [2300, 2400],
                [2400, 2000],   [2400, 2100],   [2400, 2200],   [2400, 2300],   [2400, 2400],

                [100, 2000],   [100, 2100],   [100, 2200],   [100, 2300],   [100, 2400],
                [200, 2000],   [200, 2100],   [200, 2200],   [200, 2300],   [200, 2400],
                [300, 2000],   [300, 2100],   [300, 2200],   [300, 2300],   [300, 2400],
                [400, 2000],   [400, 2100],   [400, 2200],   [400, 2300],   [400, 2400],
                [500, 2000],   [500, 2100],   [500, 2200],   [500, 2300],   [500, 2400],

                [2000, 100],   [2100, 100],   [2200, 100],   [2300, 100],   [2400, 100],
                [2000, 200],   [2100, 200],   [2200, 200],   [2300, 200],   [2400, 200],
                [2000, 300],   [2100, 300],   [2200, 300],   [2300, 300],   [2400, 300],
                [2000, 400],   [2100, 400],   [2200, 400],   [2300, 400],   [2400, 400],
                [2000, 500],   [2100, 500],   [2200, 500],   [2300, 500],   [2400, 500]


                ]

#INIT
pygame.init()
d_surf = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
GAME_SIZE_X =pygame.display.get_surface().get_width()
GAME_SIZE_Y = pygame.display.get_surface().get_height()
pygame.display.set_caption('GAME 1')

font = pygame.font.Font(None, 20)
font2 = pygame.font.Font(None, 25)
font3 = pygame.font.Font(None, 35)
font4 = pygame.font.Font(None, 50)



pygame.mixer.init()

gun_effect = pygame.mixer.Sound('gunshot.wav')
explosion_effect = pygame.mixer.Sound('explosion.wav')
reload_effect = pygame.mixer.Sound('reload.wav')
enemy_dead_effect = pygame.mixer.Sound('enemy_dead.wav')
buy_item_effect = pygame.mixer.Sound('enemy_dead.wav')
equip_item_effect = pygame.mixer.Sound('reload.wav')
throw_bomb_effect = pygame.mixer.Sound('throw_bomb.wav')
laugh_effect = pygame.mixer.Sound('laugh.wav')
gong = pygame.mixer.Sound('gong.wav')

#pygame.mixer.music.load('soundtrack.wav')
#pygame.mixer.music.play(-1)
music_paused = False


#KEYS
KEY1 = K_z
KEY2 = K_s
KEY3 = K_q
KEY4 = K_d
KEY5 = K_SPACE
KEY6 = K_p
KEY7 = K_x
KEY8 = K_RIGHT
KEY9 = K_LEFT
KEY10 = K_b
KEY11 = K_e
KEY12 = K_r
KEY13 = K_f



#GAME PARAMETERS
start_pos = SPAWN_POINT


#FUNCTIONS
def calc_unit_vectors(c, m):
    cx, cy = c[0], c[1]
    mx, my = m[0], m[1]
    
    try:
        vr_abs = sqrt(((mx-cx)**2+(my-cy)**2))
        vt_abs = sqrt((-(my-cy)/(mx-cx))**2 + 1)
        vr = [(mx-cx)/vr_abs, (my-cy)/vr_abs]
        vt = [(-(my-cy)/(mx-cx))/vt_abs, 1/vt_abs]
        return vr, vt
    except ZeroDivisionError:
        if cy<my:
            return [0, 1], [1, 0]
        else:
            return [0, -1], [-1, 0]


def calc_triangle_points(c, m, size):
    cx, cy = c[0], c[1]
    mx, my = m[0], m[1]
    try:
        vr, vt = calc_unit_vectors([cx, cy], [mx, my])
        return [[cx + vr[0] * size, cy + vr[1] * size],
                [cx - vr[0] * (size / 2) - vt[0] * (size / 2), cy - vr[1] * (size / 2) - vt[1] * (size / 2)],
                [cx - vr[0] * (size / 2) + vt[0] * (size / 2), cy - vr[1] * (size / 2) + vt[1] * (size / 2)]]
    except TypeError:
        return [[0, 0], [0, 0], [0, 0]]


def calc_dist(p0, p1):
    x0, y0 = p0[0], p0[1]
    x1, y1 = p1[0], p1[1]
    return sqrt((x1-x0)**2+(y1-y0)**2)


def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])


def point_in_triangle(pt, v1, v2, v3):
    b1 = sign(pt, v1, v2) <= 0
    b2 = sign(pt, v2, v3) <= 0
    b3 = sign(pt, v3, v1) <= 0
    return (b1 == b2) and (b2 == b3)

def point_in_rectangle(pt, pt2, size):
    return Rect(pt2[0], pt2[1], size[0], size[1]).collidepoint(pt)

def message(t, y, size, color):
    font = pygame.font.Font(None, size)
    text = font.render(t, True, color)
    d_surf.blit(text, (GAME_SIZE_X/5, y ))


def msg1(text, time):
    u = time
    while not pygame.mouse.get_pressed()[0] or u>0:
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        u -= 1
        d_surf.fill(BACKGROUND_COLOR)
        for i in range(len(text)):
            t, t2, t3, t4 = text[i][0], text[i][1], text[i][2], text[i][3]
            message(t, t2, t3, t4)
        pygame.display.update()
        pygame.time.wait(10)

def show_user_manual(y):
    display_text = [
    ["INSTRUCTIONS", y, 60, WHITE],
    ["left click: shoot", y+120, 30, WHITE],
    ["[zqsd]: move", y+160, 30, WHITE],
    ["[space]: boost", y+200, 30, WHITE],
    ["[f]: bomb", y+240, 30, WHITE],
    ["click to continue.", y+400, 30, BLUE],
        ]
    msg1(display_text, 20)

def int_in(x, a, b):
    return int(max(min(x,b), a))

# CAMERA

CAM_X = 0
CAM_Y = 0
SCOPE = 0
cam_speed = 0.5*SCROLLING_SPEED

def set_scope(scope_dir):
    global SCOPE
    global cam_speed
    global CAM_X
    global CAM_Y
    m_pos = pygame.mouse.get_pos()

    if scope_dir:

        if cam_speed < 4:
            cam_speed += 1*SCROLLING_SPEED
            
        SCOPE += cam_speed
        x_dist = GAME_SIZE_X/2 - m_pos[0]  
        x_dist = x_dist/320
        y_dist = GAME_SIZE_Y/2 - m_pos[1]
        y_dist = y_dist/180
        CAM_X += x_dist*cam_speed
        CAM_Y += y_dist*cam_speed
        if CAM_X > CAM_RANGE_X:
            CAM_X = CAM_RANGE_X
        elif CAM_X < -CAM_RANGE_X:
            CAM_X = -CAM_RANGE_X
        if CAM_Y > CAM_RANGE_Y:
            CAM_Y = CAM_RANGE_Y
        elif CAM_Y < -CAM_RANGE_Y:
            CAM_Y = -CAM_RANGE_Y
            
            
            
    else:
        cam_speed = max(cam_speed - 0.2, 0.5)


def get_camera_offset(pos):
    global CAM_X
    global CAM_Y
    
    x, y = pos

    m_pos = pygame.mouse.get_pos()

    x2, y2 = GAME_SIZE_X/2-x+CAM_X, GAME_SIZE_Y/2-y+CAM_Y

##    x, y = pos
##
##    m_pos = pygame.mouse.get_pos()
##
##    x2, y2 = GAME_SIZE_X/2-x, GAME_SIZE_Y/2-y
##
##    vr, vt = calc_unit_vectors([GAME_SIZE_X/2, GAME_SIZE_Y/2], m_pos)
    
##    dist = calc_dist([GAME_SIZE_X/2, GAME_SIZE_Y/2], m_pos)
##    dist2 = max(dist-80, 0)
##    scalarx = min((dist2/200)*100, 100)
##    scalary = min((dist2/120)*120, 120)

    return int(x2 + CAM_X), int(y2 + CAM_Y)

# PARTICLE EFFECTS

particle_list = []
screen = pygame.sprite.Sprite()
screen.rect = pygame.Surface((GAME_SIZE_X, GAME_SIZE_Y)).get_rect()
screen.rect.x = 0
screen.rect.y = 0

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, size,color, p_dir):
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.image.convert_alpha()
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.x_velocity = dx
        self.y_velocity = dy
        self.rect.x = x
        self.rect.y = y
        self.p_dir = p_dir
 
    def update(self):
        self.rect.x += self.x_velocity * self.p_dir[0]
        self.rect.y += self.y_velocity * self.p_dir[1]
        self.image.set_alpha(self.image.get_alpha() - 5)
 
    def display(self, main_surface):
        main_surface.blit(self.image, (self.rect.x, self.rect.y))
 
def create_particles(p_list, position, size, color, p_dir):
    particle_count = randint(5,10)
    numbers = list(range(-6, 6))
    if p_dir != [0, 0]:
        for i in range(0, particle_count):
            p = Particle(position[0], position[1], choice(numbers), choice(numbers), randint(1, size), color, p_dir)
            p_list.append(p)
        else:
            p = Particle(position[0], position[1], p_dir[0], p_dir[1], randint(3, size), color, p_dir)
            p_list.append(p)
    return p_list
 
def remove_particles(p_list):
    for x in range(0, len(p_list)):
        try:
            if not pygame.sprite.collide_rect(screen, p_list[len(p_list) - x - 1]):
                del p_list[len(p_list) - x - 1]
        except:
            break
 
    return p_list
 
def update_all(u_list):
    for i in range(0, len(u_list)):
        u_list[i].update()
 
def display_all(d_list, main_surface):
    for i in range(0, len(d_list)):
        d_list[i].display(main_surface)


#GAME
class Game:
    def __init__(self):
        self._rockets = list()
        self._enemies = list()
        self._bombs = list()
        self._player = {"points" : calc_triangle_points(start_pos, [10, 10], SHIP1["size"]),
                        "center" : start_pos,
                        "dir" : [0, 0],
                        "gun1" : GUN92.copy(),
                        #"gun2": GUN263.copy(),
                        "kills" : 0,
                        "score": 5000000,
                        "bomb" : BOMB1,
                        "slow_duration":0,
                        "gun_index":1,
                        "shots_fired":0,
                        "shots_hit":0,
                        "deaths":0,
                        "ship": SHIP14}
        #self._shop = {"index":0, "shop_type":"gun1", "shop": {"gun1":SHOP1, "gun2":SHOP2, "ship":SHOP3}}
        self._level = 0
        self._over = True
        self._boost = False
        self._boost_cd = 0
        self._boost_duration = 0
        self._index = 0
        self._switch_cd = 0

        self.kill_count = 0
        self.kill_timer = 0
        self.kill_msg = ""
        self.multikill_show_duration = 0
        
        self.load_data()

    def load_data(self):
        d = path.dirname(sys.argv[0])
        data = []
        try:
            with open(path.join(d, "save"), 'r') as f:
                read_file = f.read()
                data = read_file.split()
        except Exception as E:
            print(E)
                
        #shop = self._shop["shop"]

        #if GUN999["name"].replace(" ", "_") in data:
        #    shop[GUN999["slot"]].append(GUN999)
        
        #for s in shop:
        #    for i in range(len(shop[s])):
        #        item = shop[s][i]
        #        if item["name"].replace(" ", "_") in data:
        #            item["price"] = 0
                    
        if data != []:
            p = self._player
            p["score"] = int(data[0])
            p["kills"] = int(data[1])
            p["deaths"] = int(data[2])
            self._level = int(data[3])
            p["shots_fired"] = int(data[4])
            p["shots_hit"] = int(data[5])

    def save_data(self):
        d = path.dirname(sys.argv[0])
        with open(path.join(d, "save"), 'w') as f:
            p = self._player
            A = [p["score"], p["kills"], p["deaths"], self._level, p["shots_fired"], p["shots_hit"]]
            #shop = self._shop["shop"]
            #for s in shop:
            #    for i in range(len(shop[s])):
            #        item = shop[s][i]
            #        if item["price"] == 0:
            #            A.append(item["name"].replace(" ", "_"))
                
            f.write(' '.join(map(str, A)))
            
    def move_player(self, d, m):
        center = self._player["center"]
        
        if self._boost:
            d = calc_unit_vectors(center, m)[0]
        
        l = sqrt(d[0]**2+d[1]**2)
        speed = self._player["ship"]["speed"]
        
        new_center = [center[0] + speed * d[0], center[1] + speed * d[1]]
        if l > 0 and 0 < new_center[0] < WORLD_SIZE_X and 0 < new_center[1] < WORLD_SIZE_Y:
            d[0] = d[0]/l
            d[1] = d[1]/l
            self._player["center"] = new_center
        self._player["points"] = calc_triangle_points(new_center, m, self._player["ship"]["size"])

    def set_player_dir(self, d):
        self._player["dir"] = d

    def set_player_gun(self, gun):
        self._player[gun["slot"]][1] = gun.copy()

    def add_rocket(self, pos0, pos1, gun, offset, player):
        ship = self._player["ship"]
        if self._player["ship"]["gun_amount"] == 1 or not player or self._player["gun_index"] == 2:
            vr, vt = calc_unit_vectors(pos0, pos1)
            spread = gun["spread"]
            pos1 = [pos0[0] + vr[0]*100 + randint(-spread, spread)*vt[0],
                            pos0[1] + vr[1]*100 + randint(-spread, spread)*vt[1]]

            vr, vt = calc_unit_vectors(pos0, pos1)
            gun_effect.play()
            rocket = {"end":[int(pos0[0] + offset*vr[0]), int(pos0[1] + offset*vr[1])],
                                  "start":[pos0[0] + (offset + gun["size"])*vr[0], pos0[1] + (offset + gun["size"])*vr[1]],
                                  "dir":vr,
                                  "life":gun["range"]/gun["speed"],
                                  "damage":gun["damage"]*self._player["ship"]["damage"],
                                  "speed":gun["speed"],
                                  "player":player,
                                  "size":gun["size"],
                                  "penetrate":(gun["type"]==4),
                                  "hit_list":[],
                                  "gun" : gun
                                  }
            self._rockets.append(rocket)

        else:
            vr, vt = calc_unit_vectors(pos0, pos1)
            pos0_a = self._player["points"][1]
            pos0_b = self._player["points"][2]

            spread = gun["spread"]
            pos1 = [pos1[0] + 5*randint(-spread, spread)*vt[0],
                            pos1[1] + 5*randint(-spread, spread)*vt[1]]

            vr_a, vt_a = calc_unit_vectors(pos0_a, pos1)
            vr_b, vt_b = calc_unit_vectors(pos0_b, pos1)
            
            gun_effect.play()
            rocket1 = {"end":[int(pos0_a[0] + offset*vr_a[0]), int(pos0_a[1] + offset*vr_a[1])],
                                  "start":[pos0_a[0] + (offset + gun["size"])*vr_a[0], pos0_a[1] + (offset + gun["size"])*vr_a[1]],
                                  "dir":vr_a,
                                  "life":gun["range"]/gun["speed"],
                                  "damage":gun["damage"]*self._player["ship"]["damage"],
                                  "speed":gun["speed"],
                                  "player":player,
                                  "size":gun["size"],
                                  "penetrate":(gun["type"]==4),
                                  "hit_list":[],
                                  "gun" : gun
                                  }
            rocket2 = {"end":[int(pos0_b[0] + offset*vr_b[0]), int(pos0_b[1] + offset*vr_b[1])],
                                  "start":[pos0_b[0] + (offset + gun["size"])*vr_b[0], pos0_b[1] + (offset + gun["size"])*vr_b[1]],
                                  "dir":vr_b,
                                  "life":gun["range"]/gun["speed"],
                                  "damage":gun["damage"]*self._player["ship"]["damage"],
                                  "speed":gun["speed"],
                                  "player":player,
                                  "size":gun["size"],
                                  "penetrate":(gun["type"]==4),
                                  "hit_list":[],
                                  "gun" : gun
                                  }
            self._rockets.append(rocket1)
            self._rockets.append(rocket2)
            

        if player:
            self._player["shots_fired"] += 1

    def reload_gun(self, gun):
        if gun["ammo"] < gun["max_ammo"]:
            reload_effect.play()
            gun["c_down"] = gun["reload"]
            gun["ammo"] = gun["max_ammo"]

    def fire_gun(self, shooter_pos, gun, target_pos, player):
        try:
            gun_type = gun["type"]
            rounds = gun["rounds"]
            if gun["ammo"] > 0 and gun["c_down"] < 1:
                if gun_type < 2 or gun_type == 4:
                    gun["ammo"] -= 1
                    gun["c_down"] = gun["interval"]
                    self.add_rocket(shooter_pos, target_pos, gun, SHIP_SIZE, player)

                elif gun_type == 2:
                    if gun["chamber"] < 1:
                        gun["ammo"] -= 1
                        gun["chamber"] = gun["rounds"]
                        gun["c_down"] = gun["burst_interval"]
                        self.add_rocket(shooter_pos, target_pos, gun, SHIP_SIZE, player)
                        gun["chamber"] -= 1
                elif gun_type == 3:
                    #vr, vt = calc_unit_vectors(shooter_pos, target_pos)
                    for i in range(rounds):
                        if gun["ammo"]>0:
                            self.add_rocket(shooter_pos,
                                               target_pos,
                                                gun, SHIP_SIZE, player)
                            gun["ammo"] -= 1
                    gun["c_down"] = gun["interval"]
            if gun["c_down"] < 1 and gun_type==2 and gun["chamber"]>0:
                gun["ammo"] -= 1
                gun["chamber"] -= 1
                if gun["chamber"]<1 or gun["ammo"]<1:
                    gun["c_down"] = gun["interval"]
                else:
                    gun["c_down"] = gun["burst_interval"]
                self.add_rocket(shooter_pos, target_pos, gun, SHIP_SIZE, player)

        except Exception as E:
            print(E)

        if gun["ammo"] < 1:
            game.reload_gun(gun)
                

    def add_enemy(self, pos, enemy_dir, en):
        enemy = en.copy()
        enemy["center"] = pos
        enemy["dir"] = enemy_dir
        self._enemies.append(enemy)

    def next_level(self):
        if self._level >= len(LEVELS):
            print("game won")
            msg1([["Game won", y, 40, COLOR3]], 20)
            #if GUN999 in self._shop["shop"]["gun2"]:
            #    reward_index = randint(1, 200)
            #    print("player has diablo: ", reward_index)
            #    GAME_REWARD = 10000 + randint(1, 10000)
            #    if reward_index > 195:
            #        GAME_REWARD += 100000 + randint(1, 100000)
            #    elif reward_index > 190:
            #        GAME_REWARD += randint(20000, 30000)
            #    elif reward_index > 150:
            #        GAME_REWARD += randint(10000, 20000)
            #    elif reward_index >100:
            #        GAME_REWARD += randint(5000, 10000)
            #    y = int(GAME_SIZE_Y/2)
            #    msg1(
            #        [["You won again", y, 40, COLOR3]],
            #        20
            #        )
            #    self._player["score"] += GAME_REWARD
##            else:
##                reward_index = randint(1, 200)
##                print("no diablo", reward_index)
##                GAME_REWARD = 10000 + randint(1, 10000)
##                if reward_index < 20:
##                    y = int(GAME_SIZE_Y/2)
##                    msg1(
##                    [["You won", y, 40, COLOR3]],
##                    20
##                    )
##                    self._shop["shop"]["gun2"].append(GUN999)
##                elif reward_index > 195:
##                    GAME_REWARD += 100000 + randint(1, 100000)
##                elif reward_index > 190:
##                    GAME_REWARD += randint(20000, 30000)
##                elif reward_index > 150:
##                    GAME_REWARD += randint(10000, 20000)
##                elif reward_index >100:
##                    GAME_REWARD += randint(5000, 10000)
##                if reward_index >= 10:
##                    y = int(GAME_SIZE_Y/2)
##                    msg1(
##                    [["Winner", y, 40, COLOR3]],
##                    20
##                    )
##                self._player["score"] += GAME_REWARD

            accuracy = 0
            try:
                accuracy = round(100*self._player["shots_hit"]/self._player["shots_fired"], 2)
            except ZeroDivisionError:
                print("z d e")
            msg1(
                [["results:", y, 40, COLOR3],
                ["kills:  "+ str(self._player["kills"]), y+50, 20, WHITE],
                ["score: " + str(self._player["score"]), y+70, 20, WHITE],
                ["accuracy: " +  str(accuracy) + "%", y+90, 20, WHITE],
                 ["deaths: "+ str(self._player["deaths"]), y+110, 20, WHITE],
                ["click to return home", y+150, 20, PURPLE]],
                20
                )
            self._level = 0
            self._over = True
        elif len(self._enemies)==0:
            global CAM_X, CAM_Y
            CAM_X, CAM_Y = 0, 0
            self._over = False
            p = self._player
            p["center"] = start_pos
            p["slow_duration"]=0
            p["gun1"]["ammo"] = self._player["gun1"]["max_ammo"]
            #p["gun2"]["ammo"] = self._player["gun2"]["max_ammo"]
            p["gun1"]["c_down"]= 0
            #p["gun2"]["c_down"]=0
            p["ship"]["health"] = self._player["ship"]["max_health"]

            p["ship"]["speed"] = p["ship"]["base_speed"]
            p["bomb"]["c_down"]=0
            self._enemies.clear()
            self._bombs.clear()
            self._rockets.clear()
            for i in range(1,len(LEVELS[self._level])):
                self.add_enemy(ENEMY_SPAWNS[randint(0, len(ENEMY_SPAWNS) - 1)],
                               [randint(-1, 1), randint(-1, 1)],
                               LEVELS[self._level][i])
                
            
            intro_text = [
            [LEVELS[self._level][0], GAME_SIZE_Y/2 +15, 30, WHITE],
            ["mission " + str(self._level+1), GAME_SIZE_Y/2 - 30, 50, GOLD],
            ["click to continue.", GAME_SIZE_Y/2+200, 30, WHITE2]
            ]
            msg1(intro_text, 20)
            if self._level < len(LEVELS):
                self._level += 1
            pygame.mouse.set_cursor(*pygame.cursors.broken_x)




    def is_game_over(self):
        if len(self._enemies) == 0 and not self._over:
            if self._level < len(LEVELS):
                self._boost_cd = 0
                self._boost_duration = 0
                self._boost = False
                self.kill_msg = ""
                self.kill_count = 0
                self.kill_timer = 0
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                outro_text = [
                ["mission complete", GAME_SIZE_Y/2 - 30, 50, GOLD],
                ["click to continue.", GAME_SIZE_Y/2+200, 30, WHITE2]
                ]
                msg1(outro_text, 20)

            self._over = True
            explosion_effect.play()
        return self._over

    def draw_player(self):
        p = self._player
        points = p["points"]
        d = p["dir"]
        color = p["ship"]["color"]
        color2 = p["ship"]["color2"]
        x, y = get_camera_offset(p["center"])
        offset_points = [[], [], []]
        offset_points[0] = [points[0][0] + x, points[0][1] + y]
        offset_points[1] = [points[1][0] + x, points[1][1] + y]
        offset_points[2] = [points[2][0] + x, points[2][1] + y]
        m = pygame.mouse.get_pos()
        if p["ship"]["gun_amount"] == 1 or p["gun_index"] == 2:
            vr, vt = calc_unit_vectors(offset_points[0], m)
            pygame.draw.line(d_surf, color2, [offset_points[0][0]- 5*vr[0], offset_points[0][1] - 5*vr[1]], [offset_points[0][0] + 5*vr[0], offset_points[0][1] + 5*vr[1]], 4)
            pygame.draw.line(d_surf, color2, [offset_points[0][0]+ 5*vr[0], offset_points[0][1] + 5*vr[1]], [offset_points[0][0] + 8*vr[0], offset_points[0][1] + 8*vr[1]], 8)
        else:
            vr, vt = calc_unit_vectors(offset_points[1], m)
            pygame.draw.line(d_surf, color2, [offset_points[1][0]- 2*vr[0], offset_points[1][1]- 2*vr[1]], [offset_points[1][0] + 18*vr[0], offset_points[1][1] + 18*vr[1]], 4)
            pygame.draw.line(d_surf, color2, [offset_points[1][0]+ 18*vr[0], offset_points[1][1]+ 18*vr[1]], [offset_points[1][0] + 21*vr[0], offset_points[1][1] + 21*vr[1]], 8)
            vr, vt = calc_unit_vectors(offset_points[2], m)
            pygame.draw.line(d_surf, color2, [offset_points[2][0]- 2*vr[0], offset_points[2][1]- 2*vr[1]], [offset_points[2][0] + 18*vr[0], offset_points[2][1] + 18*vr[1]], 6)
            pygame.draw.line(d_surf, color2, [offset_points[2][0]+ 18*vr[0], offset_points[2][1]+ 18*vr[1]], [offset_points[2][0] + 21*vr[0], offset_points[2][1] + 21*vr[1]], 8)
        q = self._boost_cd
        l = ((p["ship"]["max_health"] - p["ship"]["health"])/p["ship"]["max_health"])*100
        color = (int_in(color[0]-q-l/3, 0, 255), int_in(color[1]-q-l, 0, 255), int_in(color[2]-q/3-l, 0, 255))
        pygame.draw.polygon(d_surf, color, offset_points)

        pygame.draw.circle(d_surf, color2, [int(p["center"][0]+x), int(p["center"][1]+y)], int(p["ship"]["size"]/4))

        ship = p["ship"]
        pygame.draw.rect(d_surf, GREEN,
            (p["center"][0]+x-ship["size"],
            p["center"][1]+y-ship["size"]-5,
            ship["health"]*2*ship["size"]/ship["max_health"],
            2))

    def draw_interface(self, x, y):
        text = font.render("mission: " + str(self._level), True, WHITE)
        d_surf.blit(text, (x+20, y+30))
        p = self._player
        ship = p["ship"]
        health = ship["health"]

        pygame.draw.rect(d_surf, GREEN,
                         (x+10, y+10, health*4, 15)
                         )

        gun1 = p["gun1"]
        #gun2 = p["gun2"]
        if gun1["ammo"] == gun1["max_ammo"] and gun1["c_down"]>0:
            text = font.render("0 - " + str(gun1["max_ammo"]), True, WHITE)
        else:
            text = font.render(str(gun1["ammo"]) + " - " + str(gun1["max_ammo"]), True, WHITE)
        d_surf.blit(text, (x+120, y+88))
        
        #if gun2["ammo"] == gun2["max_ammo"] and gun2["c_down"]>0:
        #    text = font.render("0 - " + str(gun2["max_ammo"]), True, WHITE)
        #else:
        #    text = font.render(str(gun2["ammo"]) + " - " + str(gun2["max_ammo"]), True, WHITE)
        #d_surf.blit(text, (x+120, y+128))

                    # SELECTION
        gun_index = p["gun_index"]
        gun_index=1
        x_o, y_o = get_camera_offset(p["center"])
        #if gun_index == 1:
        pygame.draw.rect(
            d_surf,
            GRAY2,
            (x+10, y+80, 75, 30))
        pygame.draw.circle(d_surf, (85, 85, 85, 150), (int(p["center"][0]+x_o), int(p["center"][1]+y_o)), gun1["range"], 3)
        #else:
        #    pygame.draw.rect(
        #        d_surf,
        #        GRAY2,
        #        (x+5, y+120, 75, 30))
        #    pygame.draw.circle(d_surf, (85, 85, 85, 150), (int(p["center"][0]+x_o), int(p["center"][1]+y_o)), gun2["range"], 3)


        #text = font.render(gun2["name"], True, WHITE)
        #d_surf.blit(text, (x+10, y+128))
        

        amt = 50*gun1["c_down"]/gun1["reload"]
        if gun1["c_down"]>=gun1["interval"]:
            pygame.draw.rect(d_surf,
                             (BLUE2.r+amt, BLUE2.g+amt, BLUE2.b),
                             (x+10, y+80, 75-75*(gun1["c_down"]/gun1["reload"]), 30))
        elif gun1["c_down"]>0:
            pygame.draw.rect(d_surf,
                             (BLUE2.r+amt, BLUE2.g+amt, BLUE2.b),
                             (x+10, y+80, 75*(gun1["ammo"]/gun1["max_ammo"]), 30))
        else:
            pygame.draw.rect(d_surf,
                             BLUE,
                             (x+10, y+80, 75*(gun1["ammo"] / gun1["max_ammo"]), 30 ))
        text = font.render("bomb", True, WHITE)
        d_surf.blit(text, (x+10, y+168))

        text = font.render("boost", True, WHITE)
        d_surf.blit(text, (x+10, y+208))

        text = font.render(gun1["name"], True, WHITE)
        d_surf.blit(text, (x+10, y+88))
            
            # GUN2
##        amt = 50*(gun2["c_down"]/gun2["reload"])
##        if gun2["c_down"]>=gun2["interval"]:
##            pygame.draw.rect(d_surf,
##                             (BLUE2.r+amt, BLUE2.g+amt, BLUE2.b),
##                             (x+80, y+120, 30-30*(gun2["c_down"]/gun2["reload"]), 30))
##        elif gun2["c_down"]>0:
##            pygame.draw.rect(d_surf,
##                             (BLUE2.r+amt, BLUE2.g+amt, BLUE2.b),
##                             (x+80, y+120, 30*(gun2["ammo"]/gun2["max_ammo"]), 30))
##        else:
##            pygame.draw.rect(d_surf,
##                             BLUE,
##                             (x+80, y+120, 30 *(gun2["ammo"] / gun2["max_ammo"]), 30))

            # BOMB
        if p["bomb"]["c_down"]>0:
            amt = 200 * p["bomb"]["c_down"] / p["bomb"]["reload"]
            pygame.draw.rect(d_surf, (RED.r-amt, 0, amt),(x+80, y+160, 30, 30))
        else:
            pygame.draw.rect(d_surf,
                             RED2,
                             (x+80, y+160, 30, 30))


        # BOOST
        if self._boost_cd>0:
            amt = 200 * self._boost_cd/BOOST_CD
            pygame.draw.rect(d_surf, (RED.r-amt, 0, amt),(x+80, y+200, 30, 30))
        elif self._boost_duration > 0:
            amt = 200 * self._boost_duration/BOOST_DUR
            pygame.draw.rect(d_surf, (170-amt, 0, 20+amt),(x+80, y+200, 30, 30))
        else:
            pygame.draw.rect(d_surf,
                             GREEN,
                             (x+80, y+200, 30, 30))
            

            # RADAR
        radar_y = GAME_SIZE_Y-y-100
        pygame.draw.rect(d_surf, WHITE2, (x+25, radar_y, 100, 100), 2)
        p_pos = p["center"]
        for enemy in self._enemies:
            e_pos = enemy["center"]
            d = calc_dist(p_pos, e_pos)
            if d<1700:
                pygame.draw.rect(d_surf, enemy["color"], (x+25+int(e_pos[0]/25), radar_y+int(e_pos[1]/25), 5, 5))
        pygame.draw.rect(d_surf, p["ship"]["color"], (x+25+int(p_pos[0]/25), radar_y+int(p_pos[1]/25), 5, 5))

    def get_p_pos(self):
        return self._player["center"]

    def get_p_gun(self):
        return self._player["gun" + str(self._player["gun_index"])]

    def next_gun(self):
        if self._switch_cd < 1:
            gun_index = self._player["gun_index"]
            if gun_index==2:
                self._player["gun_index"]= 1
            else:
                self._player["gun_index"]+= 1
            self._switch_cd = 5
            gun = self._player["gun" + str(gun_index)]
            if gun["c_down"] <= gun["interval"] and gun["ammo"]>0 and gun["reload"] > gun["interval"]:
                gun["c_down"] = 0

    def move_rocket(self, i):
        rocket = self._rockets[i]
        rocket["start"][0] = rocket["start"][0] + rocket["speed"] * rocket["dir"][0]
        rocket["end"][0] = rocket["end"][0] + rocket["speed"] * rocket["dir"][0]
        rocket["start"][1] = rocket["start"][1] + rocket["speed"] * rocket["dir"][1]
        rocket["end"][1] = rocket["end"][1] + rocket["speed"] * rocket["dir"][1]

    def step_rocket(self):
        rem = list()
        rem2 = list()
        for i in range(len(self._rockets)):
            self.move_rocket(i)
            rocket = self._rockets[i]
            x, y = get_camera_offset(self._player["center"])
            pygame.draw.line(d_surf, BLUE, [rocket["start"][0]+x, rocket["start"][1]+y], [rocket["end"][0]+x, rocket["end"][1]+y], 4)
            r_pos = rocket["start"]
            r_pos2 = rocket["end"]
            rocket["life"] -= 1
            points = self._player["points"]
            if rocket["life"] < 0:
                rem.append(i)

            if point_in_triangle(r_pos, points[0], points[1], points[2]):
                r = g = b = 0
                if rocket["gun"]["name"] == "Gambit" or rocket["gun"]["name"] == "D.I.A.B.L.O." or rocket["gun"]["name"] == "Buddha 9":
                    r = randint(0, 80)
                    g = 0
                    b = randint(20, 40)
                else:
                    r = int(180*((rocket["gun"]["damage"]*rocket["gun"]["rounds"])/(GUN_DAMAGE)))
                    g =100-int(100*rocket["gun"]["range"]/(GUN_RANGE))
                    b = int(80*(rocket["gun"]["reload"]/GUN_RELOAD))
                particle_color = Color(0, 0, 0)
                try:
                    particle_color = Color(r, g, b)
                except:
                    particle_color = Color(randint(0, 80), 0, randint(20, 40))
                global particle_list
                x, y = get_camera_offset(self._player["center"])
                r_pos2 = [r_pos[0] + x, r_pos[1]+y]
                particle_list = create_particles(particle_list, r_pos2, 8, particle_color, [1, 1])
                self._player["ship"]["health"] -= rocket["damage"]
                d_surf.fill(BLACK)
                rocket["damage"]=0
                rem.append(i)

            enemies = self._enemies
            for j in range(len(enemies)):
                enemy = enemies[j]

                dist = calc_dist(r_pos, enemy["center"])
                dist2 = calc_dist(r_pos2, enemy["center"])

                if (dist <= enemy["size"]+1 or dist2 <= enemy["size"]+1 )and rocket["damage"]>0 and not enemy in rocket["hit_list"]:
                    rocket["hit_list"].append(enemy)
                    enemy["health"] -= rocket["damage"]
                    #ENEMY HIT
                    r = g = b = 0
                    if rocket["gun"]["name"] == "Gambit" or rocket["gun"]["name"] == "D.I.A.B.L.O." or rocket["gun"]["name"] == "Buddha 9":
                        r = randint(0, 80)
                        g = 0
                        b = randint(20, 40)
                    else:
                        r = int(180*((rocket["gun"]["damage"]*rocket["gun"]["rounds"])/(GUN_DAMAGE)))
                        g =100-int(100*rocket["gun"]["range"]/(GUN_RANGE))
                        b = int(80*(rocket["gun"]["reload"]/GUN_RELOAD))
                    particle_color = Color(0, 0, 0)
                    try:
                        particle_color = Color(r, g, b)
                    except:
                        particle_color = Color(randint(0, 80), 0, randint(20, 40))
                    x, y = get_camera_offset(self._player["center"])
                    r_pos2 = [r_pos[0] + x, r_pos[1]+y]
                    particle_list = create_particles(particle_list, r_pos2, 8, particle_color, [1, 1])
                    if rocket["player"]:
                        self._player["shots_hit"] += 1
                    if rocket["penetrate"]:
                        rocket["damage"] = rocket["damage"] - enemy["health"]
                        if rocket["damage"] <= 0:
                            if not i in rem:
                                rem.append(i)
                    else:
                        rocket["damage"]=0
                        if not i in rem:
                            rem.append(i)
                    if enemy["health"] < 1:
                        if not enemy["dead"]:
                            enemy["dead"] = True
                            enemy_dead_effect.play()
                            if rocket["player"]:
                                self._boost_cd = 0
                                self._player["kills"] += 1
                                self.kill_count += 1
                                self.kill_timer = KILL_TIMER
                                kill_count = self.kill_count
                                reward = min(10, kill_count) *enemy["value"]
                                self._player["score"] += reward
                                
                                if kill_count >= len(KILL_MESSAGE):
                                    self.kill_msg = str(self.kill_count) + " KILLS"
                                else:
                                    self.kill_msg = KILL_MESSAGE[kill_count-1]
                                    
                                self.kill_msg += "! [" + str(min(10, kill_count)) + "x" +str(enemy["value"]) + " POINTS]"
                                if self.kill_count >= len(KILL_MESSAGE):
                                    gong.play()
        for j in range(len(rem)):
            try:
                self._rockets.pop(rem[j])
            except IndexError as a:
                print("Index error")
        for j in range(len(rem2)):
            try:
                self._enemies.pop(rem2[len(rem2)-j-1])
            except IndexError as a:
                print("Index error")

    def update_enemy(self, i):
        self.move_enemy(i)
        enemy = self._enemies[i]
        ec = enemy["color"]
        health = enemy["health"]
        max_health = enemy["max_health"]
        x, y= get_camera_offset(self._player["center"])
        x, y = int(x), int(y)
        pygame.draw.circle(d_surf, ec, (int(enemy["center"][0]+x), int(enemy["center"][1]+y)), enemy["size"])
        pygame.draw.rect(d_surf, GREEN,
            (enemy["center"][0]+x-enemy["size"],
            enemy["center"][1]+y-enemy["size"]-5,
            health*2*enemy["size"]/max_health,
            2))

        kill_count = self.kill_count

        if self.kill_timer > 1:
            textbox = ui.TextBox(self.kill_msg, [210, 500], [300, 60], BLACK, WHITE)
            q = int(self.kill_timer*(200/KILL_TIMER))
            if self.kill_msg not in KILL_MESSAGE:
                textbox.text_color = GOLD
            textbox.color = (200-q, 200-q, 200-q)
            textbox.text_color = (255-int(q/3), 255-int(q/3), 255-int(q/3))
            textbox.draw(d_surf)
                

        if self.kill_timer == 1:
            self.kill_count = 0

        self.kill_timer = max(self.kill_timer - 1, 0)
        kill_timer = self.kill_timer

    def set_boost(self, b):
        self._boost = b

    def boost(self):
        if not self._boost and self._boost_cd <= 0:
            self._boost_duration = BOOST_DUR
            self._boost_cd = BOOST_CD
            self._boost = True


    def step_boost(self):
        if (not self._boost) and self._boost_cd >= 0:
            self._boost_cd -= 1
        elif self._boost:
            self._boost_duration -= 1
            self._player["ship"]["speed"] = 8*self._player["ship"]["base_speed"]
            if self._boost_duration <= 0:
                self._player["ship"]["speed"] = self._player["ship"]["base_speed"]
                self._boost = False

    def get_boost(self):
        return self._boost

    def draw_enemies(self):
        for i in range(len(self._enemies)):
            self.update_enemy(i)

    def move_enemy(self, i):
        enemy = self._enemies[i]
        gun = enemy["gun"]
        p = self._player
        r = randint(1, 64)

        dist = calc_dist(enemy["center"], p["center"])

        R = gun["range"]
        if dist > R:
            R = int(R/2)
            vr, vt = calc_unit_vectors(enemy["center"], [p["center"][0]+randint(-R, R), p["center"][1]+randint(-R, R)])
            enemy["dir"] = vr
        elif r<2:
            self.fire_gun(enemy["center"], gun, p["center"], False)
            
        if enemy["center"][0] <= 0:
            enemy["dir"][0] = randint(0,1)
        elif enemy["center"][0] >= WORLD_SIZE_X:
            enemy["dir"][0] = randint(-1,0)
        elif r<5:
            enemy["dir"][0] = randint(-1,1)
        if enemy["center"][1] <= 0:
            enemy["dir"][1] = randint(0,1)
        elif enemy["center"][1] >= WORLD_SIZE_Y:
            enemy["dir"][1] = randint(-1,0)
        elif r<5:
            enemy["dir"][1] = randint(-1,1)


        try:
            enemy["center"] = [int(enemy["center"][0] + enemy["dir"][0]*enemy["speed"]),
                               int(enemy["center"][1] + enemy["dir"][1]*enemy["speed"])]
        except TypeError:
            print("type error")
            


    def update_c_down(self):
        for g in range(len(self._enemies)):
            self._enemies[g]["gun"]["c_down"] -= 1

        self._player["gun" + str(self._player["gun_index"])]["c_down"] -= 1

    def enemy_count(self):
        return len(self._enemies)

    def check_player_health(self):
        if self._player["ship"]["health"] < 1:
            self._over = True

    def draw_player_stats(self, refx, refy):
        kills = self._player["kills"]
        deaths = self._player["deaths"]
        score = self._player["score"]
        level = self._level
        
        text = font3.render("STATS" , True, COLOR3)
        d_surf.blit(text, (refx, refy))

        m = 20
        text = font.render("kills: " + str(kills), True, WHITE)
        d_surf.blit(text, (refx+m, refy+50))
        text = font.render("deaths: " + str(deaths), True, WHITE)
        d_surf.blit(text, (refx+m, refy+80))
        text = font.render("score: " + str(score), True, WHITE)
        d_surf.blit(text, (refx+m, refy+110))
        text = font.render("mission: " + str(level), True, WHITE)
        d_surf.blit(text, (refx+m, refy+140))
        if self._player["shots_fired"]>0:
            text = font.render("accuracy: " + str(round(100*self._player["shots_hit"]/self._player["shots_fired"], 2)) + "%", True, WHITE)
            d_surf.blit(text, (refx+m, refy+170))
            
    def draw_stat(self, gun, stat_name, value ,pos, scale, m, invert):
        x, y = pos[0], pos[1]
        text = font.render(stat_name + " : ", True, WHITE)
        d_surf.blit(text, (x, y))
        points =[list(), list()]
        if not invert:
            length = (value/m)*scale
            points = [[x+100, y,
                              length, text.get_height()],
                              [x+100+length, y,
                               (scale-length), text.get_height()]]

        elif invert:
            length = (value/m)*scale
            points[0] = [x+100, y, scale-length, text.get_height()]
            points[1] = [x+100+(scale-length), y, length, text.get_height()]
        if value <= m:
            pygame.draw.rect(d_surf, BLUE, points[0])
            pygame.draw.rect(d_surf, BLUE2, points[1])
        else:
            text = font.render("very high", True, WHITE)
            d_surf.blit(text, (x+100, y))

    def draw_gun_frame(self, pos, gun, scale, space):
        self.draw_stat(gun, "damage", gun["damage"]*gun["rounds"],pos, scale, GUN_DAMAGE, False)
        self.draw_stat(gun, "rate of fire",gun["interval"],[pos[0], pos[1]+space], scale, GUN_INTERVAL, True)
        self.draw_stat(gun, "reload speed", gun["reload"],[pos[0], pos[1]+2*space], scale, GUN_RELOAD, True)
        self.draw_stat(gun, "ammo", gun["max_ammo"],[pos[0], pos[1]+3*space], scale, GUN_MAX_AMMO, False)
        self.draw_stat(gun, "range", gun["range"],[pos[0], pos[1]+4*space], scale, GUN_RANGE, False)
        self.draw_stat(gun, "accuracy", gun["spread"],[pos[0], pos[1]+5*space], scale, GUN_SPREAD, True)

    def draw_ship_frame(self, pos, ship, scale, space, Q):
        self.draw_stat(ship, "speed", ship["speed"],pos, scale, SHIP_SPEED, False)
        self.draw_stat(ship, "health", ship["max_health"],[pos[0], pos[1]+space], scale, SHIP_HEALTH, False)
        self.draw_stat(ship, "damage", ship["damage"],[pos[0], pos[1]+2*space], scale, SHIP_DAMAGE, False)
        self.draw_stat(ship, "size", ship["size"],[pos[0], pos[1]+3*space], scale, SHIP_SIZE, False)

        points = list()
        game_time = pygame.time.get_ticks()
        color = ship["color"]
        color2 = ship["color2"]
        x1, y1 = 0, 0
        if Q:
            x1, y1 = pos[0]+135, pos[1]+5*space
            points = calc_triangle_points([x1, y1] , [x1+25*cos(game_time/500), y1+25*sin(game_time/500)], ship["size"])
        else:
            x1, y1 = pos[0]+190, pos[1]-35
            points = calc_triangle_points([x1, y1] , [x1-100, y1], ship["size"])

        
        pygame.draw.polygon(d_surf, color, points)
        pygame.draw.circle(d_surf, color2, [x1, y1], int(ship["size"]/4))
        
    def draw_loadout(self, refx, refy):
        p = self._player
        gun1 = p["gun1"]
        #gun2 = p["gun2"]
        ship = p["ship"]

        text = font3.render("LOADOUT" , True, COLOR3)
        d_surf.blit(text, (refx, refy))
        
        m = 20
        d = 300
        space= 35
        text = font2.render("primary gun: " + gun1["name"] , True, WHITE)
        d_surf.blit(text, (refx, refy+50))
        self.draw_gun_frame([refx+m, refy+100], gun1, 100, space)

        #text = font2.render("secondary gun: " + gun2["name"] , True, WHITE)
        #d_surf.blit(text, (refx+d, refy+50))
        #self.draw_gun_frame([refx+m+d, refy+100], gun2, 100, space)

        text = font2.render("ship: " + ship["name"] , True, WHITE)
        d_surf.blit(text, (refx, refy+350))
        self.draw_ship_frame([refx+m, refy+400], ship, 150, space, False)

    def draw_shop(self, refx, refy):
        shop = self._shop
        shop_type = shop["shop_type"]
        item = shop["shop"][shop_type][self._shop["index"]]
        price = item["price"]
        shop_name = ""
        
        space = 35
        
        if shop_type == "ship":
            shop_name="ship"
            pygame.draw.rect(d_surf, GRAY2, (GAME_SIZE_X/5+240, GAME_SIZE_Y/5+390, 310, 200))
        elif shop_type == "gun1":
            shop_name = "primary gun"
            pygame.draw.rect(d_surf, GRAY2, (GAME_SIZE_X/5+240, GAME_SIZE_Y/5+90, 260, 260))
        elif shop_type == "gun2":
            shop_name = "secondary gun"
            pygame.draw.rect(d_surf, GRAY2, (GAME_SIZE_X/5+540, GAME_SIZE_Y/5+90, 260, 260))
            
        text = font3.render("SHOP" , True, COLOR3)
        d_surf.blit(text, (refx, refy))

        text = font3.render(shop_name , True, WHITE2)
        d_surf.blit(text, (refx+100, refy))

        text = font2.render(item["name"], True, WHITE)
        d_surf.blit(text, (refx+110-text.get_width(), refy+50))

        if shop_type != "ship":
            if item["type"]==0:
                text = font.render("auto", True, RED2)
                d_surf.blit(text, (refx+110-text.get_width(), refy+35))
            elif item["type"]==1:
                text = font.render("semi", True, RED2)
                d_surf.blit(text, (refx+110-text.get_width(), refy+35))
            elif item["type"]==2:
                text = font.render("burst", True, RED2)
                d_surf.blit(text, (refx+110-text.get_width(), refy+35))
            elif item["type"]==3:
                text = font.render("shotgun", True, RED2)
                d_surf.blit(text, (refx+110-text.get_width(), refy+35))
            elif item["type"]==4:
                text = font.render("sniper", True, RED2)
                d_surf.blit(text, (refx+110-text.get_width(), refy+35))


        if shop["index"]+1<len(shop["shop"][shop_type]):
            #BUTTON RIGHT
            pygame.draw.rect(d_surf, BLUE2, (refx+235, refy+40, 35, 35))
            text = font2.render(">", True, WHITE)
            d_surf.blit(text, (refx+245, refy+50))
        if shop["index"]>0:
            pygame.draw.rect(d_surf, BLUE2, (refx+195, refy+40, 35, 35))
            text = font2.render("<", True, WHITE)
            d_surf.blit(text, (refx+205, refy+50))

        if item["price"]==0:
            pygame.draw.rect(d_surf, BLUE2, (refx+120, refy+40, 70, 35))
            text = font2.render("EQUIP", True, WHITE)
            d_surf.blit(text, (refx+130, refy+50))
        else:
            pygame.draw.rect(d_surf, BLUE2, (refx+120, refy+40, 70, 35))
            text = font2.render("BUY", True, WHITE)
            d_surf.blit(text, (refx+135, refy+50))
            text = font2.render(str(item["price"]) + " points", True, GOLD)
            d_surf.blit(text, (refx+200, refy+320))
        
        if item["slot"] != "ship":
            self.draw_gun_frame([refx+10, refy+100], item, 150, space)
        else:
            self.draw_ship_frame([refx+10, refy+100], item, 150, space, True)
        
    
    def draw_lobby(self, x, y):
            #STATS
        if self._over == True:
            #self.draw_shop(x+850, y+50)
            self.draw_player_stats(x+50, y+50)
            #self.draw_loadout(x+250, y+50)

            pygame.draw.rect(d_surf, BLUE2, (x+875, y+450, 200, 50))
            text = font3.render("PLAY MISSION", True, WHITE)
            d_surf.blit(text, (x+875+(100-text.get_width()/2), y+450+(25-text.get_height()/2)))

            pygame.draw.rect(d_surf, BLUE2, (x+875, y+510, 200, 50))
            text = font3.render("PLAY ONLINE", True, WHITE)
            d_surf.blit(text, (x+875+(100-text.get_width()/2), y+510+(25-text.get_height()/2)))

            pygame.draw.rect(d_surf, BLUE2, (x+875, y+570, 200, 50))
            text = font3.render("CONTROLS", True, WHITE)
            d_surf.blit(text, (x+875+(100-text.get_width()/2), y+570+(25-text.get_height()/2)))

            pygame.draw.rect(d_surf, GRAY2, (x+875, y+630, 200, 50))
            text = font3.render("SAVE & QUIT", True, WHITE)
            d_surf.blit(text, (x+875+(100-text.get_width()/2), y+630+(25-text.get_height()/2)))


            #pygame.draw.rect(d_surf, COLOR2, (refx, refy, 600, 440))

##            text = font2.render("SHOP" , True, COLOR3)
##            d_surf.blit(text, (refx+625, refy-50))
##
##            
##        
##            text = font2.render("gun 1: " + str(gun1["name"]), True, WHITE)
##            d_surf.blit(text, (refx, refy+300))
##            self.draw_stats_frame([refx, refy], gun1)
##            text = font2.render("gun 2 : " + str(gun2["name"]), True, WHITE)
##            d_surf.blit(text, (refx+300, refy+300))
##            self.draw_stats_frame([refx+300, refy], gun2)
##            if self._player["gun_index"] == 0:
##                pygame.draw.rect(d_surf, WHITE2, (refx, refy+350, text.get_width(), 10))
##            else:
##                pygame.draw.rect(d_surf, WHITE2, (refx+300, refy+350, text.get_width(), 10))
##            price = ["price"]
##            text = font2.render("buy " + GUNS[i]["name"] + " : " + str(price) + " [b]", True, WHITE)
##            if price == 0:
##                text = font2.render("equip " + GUNS[i]["name"] + " [b]" , True, WHITE)
##            d_surf.blit(text, (refx+625, refy+300))
##            self.draw_stats_frame([refx+625, refy], GUNS[i])
##
##            text = font2.render("press [p] to start level " + str(self._level+1), True, WHITE)
##            d_surf.blit(text, (refx+100, refy+400))
##            
##            text = font.render("use arrow keys to view other guns", True, WHITE)
##            d_surf.blit(text, (refx+625, refy+380))
##            g = "primary"
##            if self._player["gun_index"]==1:
##                g = "secondary"
##            text = font.render("as " + g + " weapon    ([e] to change)", True, RED)
##            d_surf.blit(text, (refx+625, refy+340))

    def won(self):
        if len(self._enemies) == 0 and self._level >= len(LEVELS):
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            self._over = True
            return True
        else:
            return False

    def add_health(self, amt):
        if self._player["score"] >= 10 and self._player["health"]<self._Fplayer["max_health"]:
            self._player["health"] += amt
            if self._player["health"] >  self._player["max_health"]:
                self._player["health"] = self._player["max_health"]

    def get_gun_type(self):
        i = str(self._player["gun_index"])
        return self._player["gun" + i]["type"], self._player["gun"+i]["rounds"]

    def get_p_bomb(self):
        return self._player["bomb"]

    def throw_bomb(self, pos0, bomb, pos1, player):
        if self._player["bomb"]["c_down"] <1:
            vr, vt = calc_unit_vectors(pos0, pos1)
            b = bomb.copy()
            throw_bomb_effect.play()
            b["pos"] = pos0
            b["dir"] = vr
            b["player"] = player
            self._bombs.append(b)
            self._player["bomb"]["c_down"] = self._player["bomb"]["reload"]

    def step_slow_duration(self):
        self._switch_cd -= 1
        for i in range(len(self._enemies)):
            enemy = self._enemies[i]
            try:
                if enemy["slow_duration"]>0:
                    enemy["slow_duration"] -= 1
                else:
                    enemy["speed"]=enemy["base_speed"]
            except Exception as e:
                print(e)
            self._player["slow_duration"] -= 1
            if self._player["slow_duration"]  < 1 and not self._boost:
                self._player["ship"]["speed"] = self._player["ship"]["base_speed"]  
                    
    def step_bomb(self):
        if self._player["bomb"]["c_down"]>0:
            self._player["bomb"]["c_down"] -= 1

        p = self._player
        x, y = get_camera_offset(p["center"])
        bombs = self._bombs
        rem = list()
        for i in range(len(bombs)):
            b = bombs[i]
            b["life"] -= 1
            if b["life"] < 10 and not b['active']:
                b["active"] = True
                explosion_effect.play()
            if b["life"] < 1:
                rem.append(i)
            if b["active"]:
                size = b["blast"]
                pygame.draw.circle(d_surf, (50, 5*b["life"], 50), [int(b["pos"][0]+x), int(b["pos"][1]+y)], b["blast"])
                for k in range(len(self._enemies)):
                    enemy = self._enemies[k]
                    enemy_size = enemy["size"]
                    dist = calc_dist(enemy["center"], b["pos"])
                    if dist <= size+enemy_size and b["life"]>8:
                        enemy["health"] -= b["damage"] * p["ship"]["damage"]
                        #ENEMY HIT
                        enemy["speed"] = enemy["base_speed"]*b["slow"]
                        enemy["slow_duration"] = b["slow_duration"]
                        if enemy["health"]<1 and b["player"] and not enemy["dead"]:
                            self._player["kills"] += 1
                            self.kill_count += 1
                            self.kill_timer = KILL_TIMER
                            enemy["dead"] = True
                            enemy_dead_effect.play()
                            kill_count = self.kill_count
                            reward = min(10, kill_count) *enemy["value"]
                            self._player["score"] += reward
                            
                            if kill_count >= len(KILL_MESSAGE):
                                self.kill_msg = str(self.kill_count) + " KILLS"
                            else:
                                self.kill_msg = KILL_MESSAGE[kill_count-1]
                                
                            self.kill_msg += "! [" + str(min(10, kill_count)) + "x" +str(enemy["value"]) + " POINTS]"
                            if self.kill_count >= len(KILL_MESSAGE):
                                gong.play()
                d = calc_dist(p["center"], b["pos"])
                ship = p["ship"]
                if d<=size+ship["size"]/3 and b["life"]>8:
                    ship["health"] -= int(b["damage"]/2)
                    ship["speed"] = ship["base_speed"]*b["slow"]
                    p["slow_duration"] = b["slow_duration"]

            else:
                b["pos"] = [
                    b["pos"][0] + b["dir"][0] * b["speed"],
                    b["pos"][1] + b["dir"][1] * b["speed"]
                ]
                size = b["radius"]
                pygame.draw.circle(d_surf, RED2, [int(b["pos"][0]+x), int(b["pos"][1]+y)], b["radius"])
                for j in range(len(self._rockets)):
                    r = self._rockets[j]
                    pos0 = r["start"]
                    pos1 = r["end"]
                    d0 = (pos0[0] - b["pos"][0])**2 + (pos0[1] - b["pos"][1])**2
                    d1 = (pos1[0] - b["pos"][0])**2 + (pos1[1] - b["pos"][1])**2
                    if d0 <= size**2 or d1 <= size**2 or (b["life"]<2 and b["active"]==False):
                        b["active"]=True
                        explosion_effect.play()
                        b["life"] = 10
        for j in range(len(rem)):
            try:
                self._bombs.pop(rem[j])
            except IndexError as a:
                print(a)

    def remove_dead(self):
        enemies = self._enemies
        for j in range(len(enemies)):
            try:
                if enemies[j]["dead"]:
                    enemies.pop(j)
            except IndexError:
                return
            
    def set_level(self, step):
                self._level += step
                self._over = True
                self._player["deaths"] -=step
                self._enemies = list()
                self._rockets = list()
                self._bombs = list()

    def buy_item(self):
        shop_type = self._shop["shop_type"]
        item = self._shop["shop"][shop_type][self._shop["index"]]
        price = item["price"]
        if self._player["score"] >= price:
            if price == 0:
                equip_item_effect.play()
            else:
                buy_item_effect.play()
            self._player["score"] -= price
            item["price"]=0
            self._player[shop_type] = item.copy()

    def next_item(self, amt):
        shop_type = self._shop["shop_type"]
        if 0 <= self._shop["index"]+ amt < len(self._shop["shop"][shop_type]):
            self._shop["index"] += amt
            

##    def set_shop_type(self, amt):
##        current_shop_type = self._shop["shop_type"]
##        self._shop["index"]=0
##        if amt == 1:
##            if current_shop_type == "gun1":
##                self._shop["shop_type"] = "gun2"
##            elif current_shop_type == "gun2":
##                self._shop["shop_type"] = "ship"
##            elif current_shop_type == "ship":
##                self._shop["shop_type"] = "gun1"
##        elif amt == -1:
##            if current_shop_type == "gun2":
##                self._shop["shop_type"] = "gun1"
##            elif current_shop_type == "ship":
##                self._shop["shop_type"] = "gun2"
##            elif current_shop_type == "gun1":
##                self._shop["shop_type"] = "ship"
            
    def set_shop_type(self, shop_type):
        self._shop["shop_type"]=shop_type
        self._shop["index"]=0

    def make_stars(self, amt):
        for i in range(amt):
            self._stars.append([randint(0, WORLD_SIZE_X), randint(0, WORLD_SIZE_Y), randint(1, 4)])

    def clear_stars(self):
        self._stars = list()

    def draw_stars(self):
        for star in self._stars:
            x, y = get_camera_offset(self._player["center"])
            pygame.draw.circle(d_surf, WHITE2, [int(star[0]+x), int(star[1]+y)], star[2])



                                


started = False

y = 350

display_text = [
["SPACE RAMBO", GAME_SIZE_Y/2-40, 100, GOLD],
["click to play", y+400, 30, BLUE],
]
msg1(display_text, 20)

game = Game()

print("let's go")

# MAIN LOOP

while True:
            
    d_surf.fill(BACKGROUND_COLOR)
    p_pos = game.get_p_pos()
    m_pos = pygame.mouse.get_pos()
    x,y = get_camera_offset(p_pos)
    m_pos2 = [m_pos[0] - x, m_pos[1] - y]
    
    keys = pygame.key.get_pressed()

    e_count = game.enemy_count()
    over = game.is_game_over()
    gun_type, rounds = game.get_gun_type()
    if e_count>0 and not over:
        update_all(particle_list)
        display_all(particle_list, d_surf)
        particle_list = remove_particles(particle_list)
        game.draw_stars()
        p_gun = game.get_p_gun()
        p_bomb = game.get_p_bomb()
        
        # movement
        direction = [0, 0]
        if not game.get_boost():
            if keys[KEY1]:
                direction[1] = -1
            if keys[KEY2]:
                direction[1] = 1
            if keys[KEY3]:
                direction[0] = -1
            if keys[KEY4]:
                direction[0] = 1
        if keys[KEY12]:
            game.reload_gun(p_gun)
        
        if pygame.mouse.get_pressed()[0]:
            if gun_type == 0:
                game.fire_gun(p_pos, p_gun, m_pos2, True)
        elif keys[K_SPACE]:
            game.boost()
        if gun_type == 2 and p_gun["chamber"]>0:
            game.fire_gun(p_pos, p_gun, m_pos2, True)

        if keys[KEY13]:
            game.throw_bomb(p_pos, p_bomb, m_pos2, True)
        #print(m_pos)
        if m_pos[0] < 220 or m_pos[0]> GAME_SIZE_X-220 or m_pos[1] < 170 or m_pos[1] > GAME_SIZE_Y-170:
            print("scope true")
            set_scope(True)
        else:
            set_scope(False)
            

        game.step_boost()
        game.move_player(direction, m_pos2)
        game.update_c_down()
        game.step_bomb()
        game.step_slow_duration()
        game.step_rocket()
        game.draw_interface(0, 0)
        game.draw_player()
        game.draw_enemies()
        game.remove_dead()
        game.check_player_health()

    elif e_count>0 and over:
        game.set_level(-1)
        game.clear_stars()
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        laugh_effect.play()
        
    elif e_count==0 and over and not game.won():
        game.draw_lobby(int(GAME_SIZE_X/5), int(GAME_SIZE_Y/5))
        #game.draw_lobby(0,0)
        game.clear_stars()
    elif game.won():
        game.next_level()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            button_pos = (1600, 850)
            button_size = (30, 30)
            if point_in_rectangle(m_pos, button_pos, button_size):
                if not music_paused:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                music_paused = not music_paused
        if event.type == QUIT:
            game.save_data()
            pygame.quit()
            sys.exit()
            
        if (event.type is KEYDOWN and event.key == K_p):
            if d_surf.get_flags() and pygame.FULLSCREEN:
                pygame.display.set_mode((1250, 700))
                GAME_SIZE_X = 1250
                GAME_SIZE_Y = 700
            else:
                pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                GAME_SIZE_X = pygame.display.get_surface().get_width()
                GAME_SIZE_Y = pygame.display.get_surface().get_height()
        
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            if gun_type in [1,2,3, 4] and not over:
                try:
                    game.fire_gun(p_pos, p_gun, m_pos2, True)
                except NameError:
                    print("error")
            refx = int(GAME_SIZE_X/5)
            refy =  int(GAME_SIZE_Y/5)
            if over:
##                button_pos = (refx+970, refy+90)
##                button_size = (70, 35)
##                if point_in_rectangle(m_pos, button_pos, button_size):
##                    game.buy_item()
##                    
##                button_pos = (refx+1085, refy+90)
##                button_size = (35, 35)
##                if point_in_rectangle(m_pos, button_pos, button_size):
##                    game.next_item(1)
##                    
##                button_pos = (refx+1045, refy+90)
##                button_size = (35, 35)
##                if point_in_rectangle(m_pos, button_pos, button_size):
##                    game.next_item(-1)
##                    
##                button_pos = (refx+240, refy+90)
##                button_size = (260, 260)
##                if point_in_rectangle(m_pos, button_pos, button_size):
##                    game.set_shop_type("gun1")
##                    
##                button_pos = (refx+540, refy+90)
##                button_size = (260, 260)
##                if point_in_rectangle(m_pos, button_pos, button_size):
##                    game.set_shop_type("gun2")
##
##                button_pos = (refx+240, refy+390)
##                button_size = (310, 200)
##                if point_in_rectangle(m_pos, button_pos, button_size):
##                    game.set_shop_type("ship")

                button_pos = (refx+875, refy+450)
                button_size = (200, 50)
                if point_in_rectangle(m_pos, button_pos, button_size):
                    game.next_level()
                    particle_list= []
                    game.make_stars(500)

                button_pos = (refx+875, refy+510)
                button_size = (200, 50)
                if point_in_rectangle(m_pos, button_pos, button_size):
                    msg1([["server unavailable", int(GAME_SIZE_Y/2), 40, WHITE]],
                         20)

                button_pos = (refx+875, refy+570)
                button_size = (200, 50)
                if point_in_rectangle(m_pos, button_pos, button_size):
                    show_user_manual(350)

                button_pos = (refx+875, refy+630)
                button_size = (200, 50)
                if point_in_rectangle(m_pos, button_pos, button_size):
                    game.save_data()
                    pygame.quit()
                    sys.exit()


 


    button_pos = (1600, 850)
    button_size = (30, 30)
    if music_paused:
        pygame.draw.rect(d_surf, WHITE2,
                         (button_pos[0],  button_pos[1], button_size[0], button_size[1])
                         )
    else:
        pygame.draw.rect(d_surf, WHITE,
                         (button_pos[0],  button_pos[1], button_size[0], button_size[1])
                         )

    pygame.display.flip()
    pygame.time.Clock().tick(100)

