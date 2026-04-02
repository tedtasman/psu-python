from typing import Any, Optional

# "join list by separator"
def join(lst: list, separator: str) -> str:
    """Join elements of a list into a single string, separated by a delimiter.

    Args:
        lst (list): the list to join
        separator (str): string to separate list elements
        
    Returns:
        str: a joined string of the list elements
    """
    if not isinstance(separator, str):
        raise TypeError("separator must be of type str")
    if not isinstance(lst, list):
        raise TypeError("lst must be of type list")

    return separator.join(lst)

# "append element to list"
def append(element: Any, lst: list) -> None:
    """Append `element` to the end of `lst`. Modifies `lst`.

    Args:
        lst (list): the list to append to
        element (Any): the item to append
    """
    if not isinstance(lst, list):
        raise TypeError("lst must be of type list")
    lst.append(element)

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
    if not isinstance(lst, list):
        raise TypeError("lst must be of type list")
    if not isinstance(index, int) and index is not None:
        raise TypeError("index must be None or of type int")
    
    if index is not None and (index > len(lst) - 1 or -1 * index > len(lst)):
        raise IndexError("pop index out of range")
    
    if index is None:
        return lst.pop()
    
    return lst.pop(index)