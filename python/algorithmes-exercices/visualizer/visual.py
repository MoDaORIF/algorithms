import pygame as py
from algorithmes import quicksort, binary_search

py.font.init()
my_font = py.font.SysFont('Comic Sans MS', 30)
comparisons = 0
array_access = 0
sort_alg = ""

def greenPass(arr, scr):
    l = len(arr)
    for i in range(l):
        drawrect(i, arr, scr, "green")
    return

def visualize(sort, arr, scr):
    global comparisons, array_access, sort_alg
    comparisons = 0
    array_access = 0

    if sort == 0:
        sort_alg = "Quick"
        drawarr(arr, scr)
        quicksort.main(arr, scr)
        greenPass(arr, scr)
    elif sort == 1:
        sort_alg = "binary search"
        drawarr(arr, scr)
        binary_search.main(arr, scr)
        input("Press Enter to continue...")

    return

def printStats(scr):
    stats = my_font.render("{} Sort, Comparisons: {}, Array Accesses: {}".format(sort_alg, comparisons, array_access), False, "white")
    scr.blit(stats, (5,5))

# Draw the rectangle that corresponds to array[r] with any color.
def drawrect(r, array, screen, color):
    h = array[r]
    py.draw.rect(screen, color, py.Rect(15+r*5, 780-h*3, 5, h*3))
    py.display.flip()
    return

def drawarr(array, screen):
    l = len(array)
    screen.fill("black")
    printStats(screen)
    for i in range(l):
        h = array[i]
        py.draw.rect(screen, (50+h*0.35, 255-h*0.8, 100+h*0.3), py.Rect(15+i*5, 780-h*3, 5, h*3))
    py.display.flip()
    return
