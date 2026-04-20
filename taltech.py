"""Add element to position."""


def add_element_to_position(elements: list, new_element: any, position: int) -> list:
    """
    Add a new element into the list in the specified position.

    All elements starting from the given position (included) are shifted right by one.

    add_element_to_position([1, 2, 3], 2, 2) => [1, 2, 2, 3]
    add_element_to_position([1], 9, 0) => [9, 1]
    add_element_to_position([1], 9, 1) => [1, 9]
    """
    # Write your code here
    prevElements = elements[:position]
    nextElements = elements[position:]
    return [*prevElements, new_element, *nextElements]
print(add_element_to_position([1, 2, 3], 2, 2))