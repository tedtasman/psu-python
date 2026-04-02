from typing import Any, Optional

# "join list by separator" 
# should really take any iterable, not specifically a list
def join(lst: list, separator: str) -> str:
    """Join elements of a list into a single string, separated by a delimiter.

    Args:
        lst (list): the list to join
        separator (str): string to separate list elements
        
    Returns:
        str: a joined string of the list elements
    """
    try:
        return separator.join(lst)
    except AttributeError:
        raise TypeError("separator must be of type str")
    except TypeError:
        raise TypeError("lst must be of type list")


# "append element to list"
def append(element: Any, lst: list) -> None:
    """Append `element` to the end of `lst`. Modifies `lst`.

    Args:
        lst (list): the list to append to
        element (Any): the item to append
    """
    try:
        lst.append(element)
    except AttributeError:
        raise TypeError("lst must be of type list")


# "pop list[index]"
def pop(lst: list, index: Optional[int] = None) -> Any:
    """Remove and return the element at position `index` from `lst`. 

    Args:
        lst (list): The list to remove from.
        index (int, optional): The list index for the element to remove. If not specified or `None`, pops last element.

    Raises:
        IndexError: `index` must exist within `lst`.

    Returns:
        Any: The popped element.
    """
    # explicitly check type to prevent passing dict which has .pop attribute
    if not isinstance(lst, list):
        raise TypeError("lst must be of type list")
    
    try:
        return lst.pop() if index is None else lst.pop(index)
    except IndexError:
        raise IndexError("pop index out of range")
    except TypeError:
        raise TypeError("index must be None or of type int")