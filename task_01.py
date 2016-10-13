#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Synthesizing task 1"""


def get_party_stats(families, table_size=6):
    """This function will calculate total number of guests and table
    Args:
        families (list): a list of families members
        table_size (int, optional): number of seats available Default: 6
    Returns:
        tuple: includes total numbers of guests and seats
    Examples:
        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']])
        (6, 3)
        >>> get_party_stats([['Jan'], ['Jen', 'Jess'], ['Jem', 'Jack', 'Janis']], 2)
        (6, 4)
    """
    mytotal_guests = sum([len(family) for family in families]) 
    mytotal_tables = sum([-(-len(family) // table_size) for family in families])
    
    return (mytotal_guests, mytotal_tables)


