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

def binarySearch(bars: list[int], left: int, right: int, window: Surface) -> None:

    # `x` is the value we want to find
    x = 9
    max = right

    while left <= right:

        mid = left + (right - left) // 2

        # Check if x is present at mid
        if bars[mid] == x:
            draw_algorithm.drawrect(x, bars, window, "red")
            return

        # If x is greater, ignore left half
        elif bars[mid] < x:
            draw_algorithm.drawrect(mid, bars, window, "yellow")
            i = mid-1

            while i >= left:
                draw_algorithm.drawrect(i, bars, window, "black")
                i -=1

            left = mid + 1

        # If x is smaller, ignore right half
        else:
            draw_algorithm.drawrect(mid, bars, window, "blue")
            i = mid+1

            if right == max:
                right -= 1

            while (i < right+1):
                draw_algorithm.drawrect(i, bars, window, "black")
                i +=1
            right = mid - 1

        pygame.time.delay(1000)

    # If we reach here, then the element
    # was not present
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

    # INFO: Used to display in the window some cool stats
    # This is not important for the exercice
    global comparisons, array_access
    comparisons = 0
    array_access = 0

    binarySearch(random_numbers, 0, len(random_numbers), window)
    return
