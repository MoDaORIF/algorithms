import pygame
from visualizer import visual as render

# INFO: Define `Surface` to statically type the variable `window`.
# This is not important for the exercice
Surface = pygame.surface.Surface

# INFO: Used to display in the window some cool stats
# This is not important for the exercice
comparisons = 0
array_access = 0


def swap(bars, i, j):
    global array_access
    array_access += 4

    temporary = bars[i]
    # NOTE: make user write
    # bars[i] = bars[j]
    # ?
    bars[i] = bars[j]
    bars[j] = temporary


def partition(bars: list[int], left: int, right: int, window: Surface) -> int:
    """

    First, it defines the pivot as the last element of `bars`.
    Then, divide
    Args:
        bars ():
        left ():
        right ():
        window ():
    """

    global comparisons, array_access
    pivot = left

    render.drawrect(pivot, bars, window, "green")

    for i in range(left + 1, right):
        if bars[i] < bars[left]:
            render.drawrect(i, bars, window, "blue")
            pivot += 1
            render.swap(bars, i, pivot)
        else:
            render.drawrect(i, bars, window, "red")

        array_access += 2
        comparisons += 1
        pygame.time.delay(1)

    swap(bars, left, pivot)
    return pivot


def quickSort(bars: list[int], left: int, right: int, window: Surface) -> None:
    """Sort the bars by their height values

        Sort all the number in the `bars` list using a quick sort algorithm.

    Args:
        bars (list[int]): random_numbers to sort. Previously nammed 'random_numbers'
        left (int):
        right (int):
        window (Surface):
    """
    if left < right:
        pivot = partition(bars, left, right, window)

        render.drawarr(bars, window)
        pygame.time.delay(10)

        quickSort(bars, left, pivot, window)
        quickSort(bars, pivot + 1, right, window)
    return


def main(random_numbers: list[int], window: Surface) -> None:
    """Function that is called to execute the quicksort algorithm

        No need to change anything

    Args:
        random_numbers (list[int]): Auto generated values that you will sort
        window (Surface): The window in which we'll visualize the algorithm

    Return:
        None
    """
    global comparisons, array_access
    comparisons = 0
    array_access = 0

    quickSort(random_numbers, 0, len(random_numbers), window)
    return
