"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    items = [str(x) for x in items]
    frequencies = dict.fromkeys(items)
    for key in frequencies.keys():
        frequencies[key] = items.count(key)
    return frequencies
