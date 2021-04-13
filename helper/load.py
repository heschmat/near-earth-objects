"""
"""

import csv
import json

from .models import NearEarthObject, CloseApproach

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

def load_approaches(path_cad):
    """ Read close approach data.

    Arguments:
    :path_cat {str} path to JSON file containing close-approach data.

    Returns:

    """
    capps = []

    with open(path_cad, 'r') as f:
        data = json.load(f)

    fields = data['fields']
    for capp in data['data']:
        capp_info = {k: v for k, v in zip(fields, capp)}
        capps.append(CloseApproach(capp_info))
    
    return capps
