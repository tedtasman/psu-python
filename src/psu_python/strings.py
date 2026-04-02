from typing import Optional


def split(string: str, sep: Optional[str] = None, maxsplit: int = -1) -> list[str]:
    """Create a list of words in `string` separated by `sep`.

    Args:
        string (str): The string to split.
        separator (str, optional): The separator delimiting words. If not specified or `None`, splits at whitespace.
        maxsplit (int, optional): The maximum number of splits to complete. If not specified or `-1`, all possible splits are made.

    Returns:
        list: A list containing the words after splitting.
    """
    if not isinstance(string, str):
        raise TypeError("string must be of type str")
    if not isinstance(sep, str) and sep is not None:
        raise TypeError("separator must be of type str")
    
    return string.split(sep, maxsplit)