#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Week 6 Synthesizing task 2"""

import data

def prepare_email(appointments):
    """ This function finds appointment time and sends emails
    Args:
        appointments(tuple): This will include client name and time
    Return:
        Returns email mormat 
    Examples:
        >>> prepare_email([('Jen', '2015'), ('Max', 'March 3')])
        ['Dear Jen,\nI look forward to meeting with you on 2015.\nBest,\nMe',
        'Dear Max,\nI look forward to meeting you on March 3.\nBest\nMe']
    """
    my_email_format = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'
    my_email = []
    
    for list_item in appointments:
        name = list_item[0]
        date = list_item[1]
        my_email.append(my_email_format.format(name, date))

    return my_email
