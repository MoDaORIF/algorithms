import pygame as py
from random import randint
from visualizer import painter

width, height = 1280, 800

py.init()
screen = py.display.set_mode((width, height))
py.display.set_caption('Sorting Algorithms Visualizer')

arr = [i+1 for i in range(250)]

def resetArray():
    global arr
    for _ in range(500):
        a, b = randint(0, 249), randint(0, 249)
        aux = arr[a]
        arr[a] = arr[b]
        arr[b] = aux
    return

# initial sort [SELECTION, INSERTION, QUICK, MERGE]
sort = -1
    # NOTE: DEBUG !
    # Force the bars to be in the right order
# resetArray()
painter.drawarr(arr, screen)

# handle key inputs
def keyActions():
    keys = py.key.get_pressed()
    
    if keys[py.K_1]:
        return 0
    elif keys[py.K_2]:
        return 1
    elif keys[py.K_r]:
        resetArray()
        painter.drawarr(arr, screen)

    return -1

# initialize loop properties
clock = py.time.Clock()
running = True
framerate = 60

'''                                 MAIN LOOP                                       '''
while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            sort = keyActions()      # handle key inputs to select sorting algorithm
            while not py.KEYUP:
                continue

    if sort != -1:
        painter.visualize(sort, arr, screen)
        painter.drawarr(arr, screen)
        sort = -1

    clock.tick(framerate)

py.quit()
