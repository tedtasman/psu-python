from typing import Any
from collections.abc import KeysView, ValuesView, ItemsView

# I don't love using `d` for the dictionary parameter but I'm not sure what would be better

# delete key from d
# this is really just d.pop(key), but I can't call it pop because that collides with the list version
def delete(key: Any, d: dict) -> Any:
    """Remove `key` from dictionary `d` and return its value.

    Args:
        key (Any): The list index for the element to remove.
        d (dict): The dictionary to remove from.

    Raises:
        KeyError: `key` must exist within `d`.

    Returns:
        Any: The value of the popped key.
    """
    # explicitly check type to prevent passing list which has .pop attribute
    if not isinstance(d, dict):
        raise TypeError("d must be of type dict")

    try:
        value = d.pop(key)
    except KeyError:
        raise KeyError(f"Key \"{key}\" not in dictionary")
    
    return value


def get_keys(d: dict) -> KeysView:
    """Get a dynamic view object of the dictionary `d`'s keys that reflects changes to `d`.

    Args:
        d (dict): the dictionary.

    Returns:
        KeysView: A view of the keys in `d`.
    """
    try:
        return d.keys()
    except AttributeError:
        raise TypeError("d must be of type dict")


def get_values(d: dict) -> ValuesView:
    """Get a dynamic view object of the dictionary `d`'s values that reflects changes to `d`.

    Args:
        d (dict): the dictionary.

    Returns:
        ValuesView: A view of the values in `d`.
    """
    try:
        return d.values()
    except AttributeError:
        raise TypeError("d must be of type dict")


def get_items(d: dict) -> ItemsView:
    """Get a dynamic view object of the dictionary `d`'s key, value pairs that reflects changes to `d`

    Args:
        d (dict): the dictionary.

    Returns:
        ValuesView: A view of the (key, value) tuple pairs in `d`.
    """
    try:
        return d.items()
    except AttributeError:
        raise TypeError("d must be of type dict")


# get key from d
def get_value(key: Any, d: dict, default: Any = None) -> Any:
    """Get the value corresponding to `key` from `d`. If `key` is not in `d`, returns `default`.

    Args:
        key (Any): the key to get from `d`.
        d (dict): the dictionary to check for `key`.
        default (Any, optional): the value to return if `key` is not in `d`. If not specified, defaults to `None`.

    Returns:
        Any: The value corresponding to `key`, or `default` if not in `d`.
    """
    try:
        return d.get(key, default)
    except AttributeError:
        raise TypeError("d must be of type dict")