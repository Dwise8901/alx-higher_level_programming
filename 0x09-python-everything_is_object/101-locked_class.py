#!/usr/bin/python3
"""Define a locked class."""


class LockClass:
    """
    Prevent the user from the instantiating new LockClock attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
