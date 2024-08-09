import pygame
from visualizer import visual as draw_algorithm

# TODO: faire des aides pour les personnes en difficulté

# INFO: Define `Surface` to statically type the variable `window`.
# This is not important for the exercice
Surface = pygame.surface.Surface

# INFO: Used to display in the window some cool stats
# This is not important for the exercice
comparisons = 0
array_access = 0


def swap(bars: list[int], i: int, pivot: int) -> None:
    """ Swap bars' places

    Swap the position of the pivot and the bar at position `i` if 
    `bars[i]` < pivot. This organizes the bars from smaller to biggest

    Args:
        bars (list[int]): random_numbers to sort. Previously nammed 'random_numbers'
        i (int): Position of the bar that we need to swap with the pivot
        pivot (int): Position of the pivot bar

    Return:
        None
    """
    global array_access
    array_access += 4

    temporary = bars[i]
    bars[i] = bars[pivot]
    bars[pivot] = temporary


def partition(bars: list[int], left: int, right: int, window: Surface) -> int:
    """ 

    First, it defines the pivot as the first element of `bars`.
    Then, for each bar, compare it's height with the pivot's.
    If the bar at position `i` if smaller than the pivot: it calls swap() to
    swap the places of the two bars.

    Args:
        bars (list[int]): random_numbers to sort. Previously nammed 'random_numbers'
        left (int): The bar located at the far LEFT of the `bars` list
        right (int): The bar located at the far RIGHT of the `bars` list
        window (Surface): The window in which we'll visualize the algorithm

    Return:
        pivot (int):
    """

    global comparisons, array_access
    pivot = left

    draw_algorithm.drawrect(pivot, bars, window, "red")

    for i in range(left + 1, right):
        if bars[i] < bars[left]:
            draw_algorithm.drawrect(i, bars, window, "blue")

            pivot += 1
            swap(bars, i, pivot)

        else:
            draw_algorithm.drawrect(i, bars, window, "yellow")

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
        left (int): The bar located at the far LEFT of the `bars` list
        right (int): The bar located at the far RIGHT of the `bars` list
        window (Surface): The window in which we'll visualize the algorithm
    """
    if left < right:
        pivot = partition(bars, left, right, window)

        draw_algorithm.drawarr(bars, window)
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