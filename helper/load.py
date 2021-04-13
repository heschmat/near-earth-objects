"""
"""

import csv
import json

from models import NearEarthObject

def load_neos(path_neo):
    """ Read near-Earth object information.
    
    Arguments:
    :path_neo {str} the path to the CSV file containing near-Earth info.

    Returns:
    :neos {list} a list of `NearEarthObject` objects.
    This will include relevant information from the CSV file.
    """
    neos = []
    with open(path_neo, 'r') as f:
        rows = csv.DictReader(f)
        for row in rows:
            neo = NearEarthObject(row)
            neos.append(neo)

    return neos
