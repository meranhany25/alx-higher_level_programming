#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'
    """


___slots___ = ["first_name"]
