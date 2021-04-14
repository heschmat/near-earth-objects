""" Represent models for near-Earth objects and their close approaches.
"""

from .helpers import cd_to_datetime, datetime_to_str

class NearEarthObject:
    """ Represents Near-Earth Object (NEO).

    """
    def __init__(self, info_dict) -> None:
        """ Initialize a near-Earth object (NEO).

        :info_dict {dict}
        """
        name = info_dict['name']
        d = info_dict['diameter']
        # Initialize the NEO object.
        self.name = None if len(name) == 0 else name
        self.designation = info_dict['pdes']
        self.diameter = float('nan') if len(d) == 0 else float(d)
        self.hazardous = True if info_dict['pha'] == 'Y' else False

        # Every NEO is connected to a set of `CloseApproach` objects.
        # Initialize as empty list. Gets populated when calling `NEODatabase`.
        self.close_approaches = []
    
    def __repr__(self):
        """Return a computer-readable string representation of the NEO object."""
        return(
            f'NearEarthObject(name={self.name!r}, '
            f'designation={self.designation!r}, diameter={self.diameter:.3f}, '
            f'hazardous={self.hazardous!r})'
        )

class CloseApproach:
    """ Represents close approach to Earth by an NEO.

    """
    def __init__(self, info_dict) -> None:
        """ Initialize a new `CloseApproach`.
        
        :info_dict {dict} contains information of a close approach.
        """
        self.designation = info_dict['des']
        self.time = cd_to_datetime(info_dict['cd'].strip())
        self.distance = float(info_dict['dist'])
        self.velocity = float(info_dict['v_rel'])

        # Every `CloseApproach` is associated with a `NEO`.
        # Gets populated when calling `NEODatabase`.
        self.neo = None
    
    def __repr__(self) -> str:
        """ Return a computer-readable string representation of
        `CloseApproach` object.
        """
        return (
            f'CloseApproach(designation={self.designation!r}, '
            f'time={datetime_to_str(self.time)!r}, '
            f'distance={self.distance:.2f}, velocity={self.velocity:.2f})'
        )
