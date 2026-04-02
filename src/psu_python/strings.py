from typing import Optional

# split string by sep
def split(string: str, sep: Optional[str] = None, maxsplit: int = -1) -> list[str]:
    """Create a list of words in `string` separated by `sep`.

    Args:
        string (str): The string to split.
        separator (str, optional): The separator delimiting words. If not specified or `None`, splits at whitespace.
        maxsplit (int, optional): The maximum number of splits to complete. If not specified or `-1`, all possible splits are made.

    Returns:
        list: A list containing the words after splitting.
    """
    # explicitly check argument types since they cannot be differentiated via duck typing (both TypeError)
    if sep is not None and not isinstance(sep, str):
        raise TypeError("separator must be of type str")
    if not isinstance(maxsplit, int):
        raise TypeError("maxsplit must be of type int")

    try:
        return string.split(sep, maxsplit)
    except AttributeError as exc:
        raise TypeError("string must be of type str") from exc


def strip(string: str, chars: Optional[str] = None) -> str:
    """Remove characters in `chars` from beginning and end of `string`.

    Args:
        string (str): the string to strip.
        chars (str, optional): string of characters to strip. If not specified or `None`, strips whitespace.

    Returns:
        str: a new string with characters stripped.
    """
    try:
        return string.strip(chars)
    except AttributeError:
        raise TypeError("string must be of type str")
    except TypeError:
        raise TypeError("chars must be None or of type str")
