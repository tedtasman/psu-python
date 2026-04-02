from typing import Any
from collections.abc import KeysView, ValuesView, ItemsView


def pop_key(d: dict, key: Any) -> Any:
    """Remove `key` from dictionary `d` and return its value.

    Args:
        d (dict): The dictionary to remove from.
        key (Any): The list index for the element to remove.

    Raises:
        KeyError: `key` must exist within `d`.

    Returns:
        Any: The value of the popped key.
    """
    if not isinstance(d, dict):
        raise TypeError("d must be of type dict")
    
    value = d.pop(key)

    if value is None:
        raise KeyError(f"Key \"{key}\" not in dictionary")
    
    return value


def get_keys(d: dict) -> KeysView:
    """Get a dynamic view object of the dictionary `d`'s keys that reflects changes to `d`.

    Args:
        d (dict): the dictionary.

    Returns:
        KeysView: A view of the keys in `d`.
    """
    if not isinstance(d, dict):
        raise TypeError("d must be of type dict")
    
    return d.keys()


def get_values(d: dict) -> ValuesView:
    """Get a dynamic view object of the dictionary `d`'s values that reflects changes to `d`.

    Args:
        d (dict): the dictionary.

    Returns:
        ValuesView: A view of the values in `d`.
    """
    if not isinstance(d, dict):
        raise TypeError("d must be of type dict")
    
    return d.values()


def get_items(d: dict) -> ItemsView:
    """Get a dynamic view object of the dictionary `d`'s key, value pairs that reflects changes to `d`

    Args:
        d (dict): the dictionary.

    Returns:
        ValuesView: A view of the (key, value) tuple pairs in `d`.
    """
    if not isinstance(d, dict):
        raise TypeError("d must be of type dict")
    
    return d.items()


def get_value(d: dict, key: Any, default: Any = None) -> Any:
    """Get the value corresponding to `key` from `d`. If `key` is not in `d`, returns `default`.

    Args:
        d (dict): the dictionary to check for `key`.
        key (Any): the key to get from `d`
        default (Any, optional): the value to return if `key` is not in `d`. If not specified, defaults to `None`.

    Returns:
        Any: The value corresponding to `key`, or `default` if not in `d`.
    """
    if not isinstance(d, dict):
        raise TypeError("d must be of type dict")
    
    return d.get(key, default)