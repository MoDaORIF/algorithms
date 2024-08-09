import pygame as py
from algorithmes import quicksort

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
    elif sort == 1:
        sort_alg = "Bubble"
        drawarr(arr, scr)
        bubbleSort(arr, scr)

    greenPass(arr, scr)
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

# Swap elements at index i and j
def swap(arr, i, j):
    global array_access
    array_access += 4
    aux = arr[i]
    arr[i] = arr[j]
    arr[j] = aux


#          ╭──────────────────────────────────────────────────────────╮
#          │                        QUICK SORT                        │
#          ╰──────────────────────────────────────────────────────────╯

def partition(arr, lft, rgt, scr):

    # NOTE (exemple): my method as an exemple
    # quicksort.coucou()

    global comparisons, array_access
    piv = lft

    drawrect(piv, arr, scr, "green")

    for i in range(lft+1, rgt):
        if arr[i] < arr[lft]:
            drawrect(i, arr, scr, "blue")
            piv += 1
            swap(arr, i, piv)
        else:
            drawrect(i, arr, scr, "red")
        
        array_access += 2
        comparisons += 1
        py.time.delay(1)

    swap(arr, lft, piv)
    return piv

def qsort(arr, lft, rgt, scr):
    if (lft < rgt):
        piv = partition(arr, lft, rgt, scr)

        drawarr(arr, scr)
        py.time.delay(10)

        qsort(arr, lft, piv, scr)
        qsort(arr, piv+1, rgt, scr)
    return

def quickSort(array, scr):
    qsort(array, 0, len(array), scr)
    return


#          ╭──────────────────────────────────────────────────────────╮
#          │                       BUBBLE SORT                        │
#          ╰──────────────────────────────────────────────────────────╯

def bubbleSort(array, scr):
    global comparisons, array_access

    n = len(array)
    for i in range(1,n):
        for j in range(n-i):

            if array[j] > array[j+1]:
                swap(array, j, j+1)

            comparisons += 1
            array_access += 2

        drawarr(array, scr)
        drawrect(n-i, array, scr, "blue")
        py.time.delay(20)

    return
