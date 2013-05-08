import json
import os

from itertools import izip, chain, repeat

# -*- coding: utf-8 -*-

"""
link.utils
~~~~~~~~~~~~

Commonly used utility functions in the link code

:copyright: (c) 2013 by David Himrod
:license: Apache2, see LICENSE for more details.

"""

def load_json_file(file_name):
    """Given a file name this function will json decode it and
    return a dictionary.

    """
    return json.load(file(file_name))

def list_to_dataframe(rows, names):
    """
    Turns an array of rows of data into a dataframe and gives them the column names
    specified.

    :params rows: the data you want to put in the dataframe
    :params names: the column names for the dataframe
    """
    from pandas import DataFrame
    try:
        import pandas._tseries as lib
    except ImportError:
        import pandas.lib as lib

    if isinstance(rows, tuple):
        rows = list(rows)

    columns = dict(zip(names, lib.to_object_array_tuples(rows).T))

    for k,v in columns.iteritems():
        columns[k] = lib.convert_sql_column(v)

    return DataFrame(columns, columns=names)

def array_paginate(n, iterable, padvalue=None, pad=True):
    """Takes an array like [1,2,3,4,5] and splits it into evenly-sized
    chunks.

    If pad is True, The last chunk is padded with the specified padvalue to
    ensure its length equals that of the other chunks.

    """
    return izip(*[chain(iterable, repeat(padvalue, n-1))]*n)
